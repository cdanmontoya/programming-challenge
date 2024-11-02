from typing import override

from injector import singleton

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.error import Error, DomainError
from src.domain.model.account import Account, AccountId


@singleton
class AccountRepositoryDict(AccountRepository):
    __db: dict[AccountId, Account]

    def __init__(self) -> None:
        self.__db = {}

    @override
    def get(self, key: AccountId) -> Account | None:
        return self.__db.get(key)

    @override
    def get_all(self) -> list[Account]:
        return list(self.__db.values())

    @override
    def insert(self, account: Account) -> Account:
        self.__db[account.id] = account
        return account

    @override
    def update(self, key: AccountId, account: Account) -> Account:
        self.__db.update({key: account})
        return account

    @override
    def delete(self, key: AccountId) -> Account | Error:
        try:
            return self.__db.pop(key)
        except KeyError:
            return DomainError(f"The account with id {key.id} does not exist.")
