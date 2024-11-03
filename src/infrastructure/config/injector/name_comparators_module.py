from injector import Module, Binder

from src.app.ports.output.name_comparator.name_comparator import NameComparator
from src.infrastructure.adapters.output.name_comparator.difflib_name_comparator import DiffLibNameComparator


class NameComparatorsModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=NameComparator, to=DiffLibNameComparator)
