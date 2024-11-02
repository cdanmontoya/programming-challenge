from dataclasses import dataclass
from uuid import UUID

from src.domain.model.contact_information import ContactInformation


@dataclass(frozen=True)
class AccountId:
    id: UUID


@dataclass()
class Account:
    id: AccountId
    contact_information: ContactInformation
