from uuid import UUID

from sqlalchemy import String, ForeignKey, types
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class AccountDao(Base):
    __tablename__ = "accounts"

    id: Mapped[UUID] = mapped_column(types.Uuid, primary_key=True)
    email: Mapped[str] = mapped_column(String(64))

    cellphones: Mapped[list["CellphoneDao"]] = relationship(
        back_populates="account", cascade="all, delete, delete-orphan"
    )


class CellphoneDao(Base):
    __tablename__ = "cellphones"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("accounts.id"), primary_key=True)
    cellphone: Mapped[str] = mapped_column(String(64), primary_key=True)

    account: Mapped["AccountDao"] = relationship(back_populates="cellphones")
