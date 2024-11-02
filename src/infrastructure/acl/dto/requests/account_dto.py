from uuid import UUID

from pydantic import BaseModel


class ContactInformationDto(BaseModel):
    email: str
    cellphones: list[str]


class AccountDto(BaseModel):
    id: UUID
    contact_information: ContactInformationDto
