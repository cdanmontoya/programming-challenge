import logging

from injector import inject

from src.app.ports.output.name_comparator.name_comparator import NameComparator
from src.app.ports.output.repositories.name_repository import NameRepository
from src.app.queries.compare_name import CompareName

logger = logging.getLogger("uvicorn")


class CompareNameUseCase:
    _name_repository: NameRepository
    _name_comparator: NameComparator

    @inject
    def __init__(self, name_repository: NameRepository, name_comparator: NameComparator):
        self._name_repository = name_repository
        self._name_comparator = name_comparator

    def compare_name(self, compare_name_query: CompareName):
        names = self._name_repository.get_all()

        similarities = self._name_comparator.compare(compare_name_query.name, names)
        filtered_similarities = list(filter(lambda x: x[1] >= compare_name_query.threshold, similarities))
        sorted_similarities = sorted(filtered_similarities, key=lambda tup: tup[1], reverse=True)

        return sorted_similarities
