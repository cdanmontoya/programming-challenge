from dataclasses import dataclass

from src.domain.model.account import AccountId


@dataclass(frozen=True)
class GetAccountById:
    account_id: AccountId
