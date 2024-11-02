from dataclasses import dataclass

from src.domain.model.account import AccountId


@dataclass(frozen=True)
class DeleteAccount:
    id: AccountId
