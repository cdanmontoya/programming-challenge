from uuid import UUID

from pydantic import BaseModel

from src.infrastructure.acl.dto.requests.account_dto import ContactInformationDto


class AccountIdDto(BaseModel):
    id: UUID


class AccountInsertedDto(BaseModel):
    id: AccountIdDto
    contact_information: ContactInformationDto
