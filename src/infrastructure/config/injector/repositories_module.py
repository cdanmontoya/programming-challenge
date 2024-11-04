from injector import Module, Binder

from src.app.ports.output.repositories.name_repository import NameRepository
from src.infrastructure.adapters.output.repositories.name.name_repository_dict import NameRepositoryDict


class RepositoriesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=NameRepository, to=NameRepositoryDict)  # type: ignore
