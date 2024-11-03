from abc import ABC, abstractmethod

from src.domain.model.name import Name


class NameComparator(ABC):

    @abstractmethod
    def compare(self, name: str, names: list[Name]) -> list[tuple[Name, float]]:
        raise NotImplementedError
