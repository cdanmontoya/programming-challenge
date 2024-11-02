from typing import override

from injector import singleton, inject
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.error import Error, DomainError
from src.domain.model.account import Account, AccountId
from src.infrastructure.adapters.output.repositories.accounts.sqlalchemy.account_mapper import (
    AccountMapper,
)
from src.infrastructure.adapters.output.repositories.accounts.sqlalchemy.account_model import (
    Base,
    AccountDao,
    CellphoneDao,
)


@singleton
class AccountRepositorySQLAlchemy(AccountRepository):
    __engine: Engine

    @inject
    def __init__(self, engine: Engine) -> None:
        self.__engine = engine
        Base.metadata.create_all(engine)

    @override
    def get(self, key: AccountId) -> Account | None:
        with Session(self.__engine) as session:
            statement = select(AccountDao).where(AccountDao.id.__eq__(str(key.id)))
            account_dao = session.scalar(statement)

            return AccountMapper.from_account_dao(account_dao) if account_dao else None

    @override
    def get_all(self) -> list[Account]:
        with Session(self.__engine) as session:
            statement = select(AccountDao)

            return [
                AccountMapper.from_account_dao(account_dao)
                for account_dao in session.scalars(statement)
            ]

    @override
    def insert(self, account: Account) -> Account:
        with Session(self.__engine) as session:
            account_dao = AccountMapper.from_account(account)
            session.add(account_dao)
            session.commit()

            return account

    @override
    def update(self, key: AccountId, account: Account) -> Account | Error:
        with Session(self.__engine) as session:
            account_dao = session.get(AccountDao, key.id)

            if account_dao:
                account_dao.email = account.contact_information.email
                account_dao.cellphones = [
                    CellphoneDao(cellphone=phone)
                    for phone in account.contact_information.cellphones
                ]
                session.commit()
                return account

            else:
                return DomainError(f"Account with id {key.id} not found")

    @override
    def delete(self, key: AccountId) -> Account | Error:
        with Session(self.__engine) as session:
            account_dao = session.get(AccountDao, key.id)

            if account_dao:
                account = AccountMapper.from_account_dao(account_dao)
                session.delete(account_dao)
                session.commit()
                return account
            else:
                return Error(f"Account with id {key.id} does not exist")
