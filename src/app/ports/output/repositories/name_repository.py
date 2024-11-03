from abc import ABC, abstractmethod

from src.domain.model.name import Name


class NameRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Name]:
        raise NotImplementedError
