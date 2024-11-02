from uuid import UUID

from pydantic import BaseModel


class UpdateAccountRequestDto(BaseModel):
    id: UUID
    email: str
    cellphones: list[str]
