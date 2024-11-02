from uuid import UUID

from pydantic import BaseModel

from src.infrastructure.acl.dto.events.error_event import ErrorEventDto
from src.infrastructure.acl.dto.requests.account_dto import ContactInformationDto


class AccountDeletedDto(BaseModel):
    id: UUID
    contact_information: ContactInformationDto


class AccountNotDeletedDto(ErrorEventDto):
    pass
