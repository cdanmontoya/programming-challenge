from injector import Injector

from src.infrastructure.config.injector.name_comparators_module import NameComparatorsModule
from src.infrastructure.config.injector.repositories_module import RepositoriesModule


def create_injector() -> Injector:
    return Injector([RepositoriesModule, NameComparatorsModule])
