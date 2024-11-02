from dataclasses import dataclass

from src.domain.model.account import AccountId


@dataclass(frozen=True)
class UpdateAccount:
    id: AccountId
    email: str
    cellphones: list[str]
