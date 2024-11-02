from injector import Module, Binder

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.infrastructure.adapters.output.repositories.accounts.sqlalchemy.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)


class RepositoriesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=AccountRepository, to=AccountRepositorySQLAlchemy)
