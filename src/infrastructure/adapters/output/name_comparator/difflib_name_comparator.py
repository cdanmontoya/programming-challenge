import logging
from difflib import SequenceMatcher

from src.app.ports.output.name_comparator.name_comparator import NameComparator
from src.domain.model.name import Name


logger = logging.getLogger("uvicorn")


class DiffLibNameComparator(NameComparator):

    def compare(self, name: str, names: list[Name]) -> list[tuple[Name, float]]:
        logger.info(f"Comparing name {name} against all available names")
        return [
            (compared_name, SequenceMatcher(None, name, compared_name.full_name).ratio()) for compared_name in names
        ]
