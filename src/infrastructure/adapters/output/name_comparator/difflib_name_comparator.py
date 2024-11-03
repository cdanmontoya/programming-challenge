import difflib

from src.app.ports.output.name_comparator.name_comparator import NameComparator
from src.domain.model.name import Name


class DifflibNameComparator(NameComparator):

    def compare(self, name: str, names: list[Name]) -> list[tuple[Name, float]]:
        return [
            (compared_name, difflib.SequenceMatcher(None, name, compared_name.full_name).ratio())
            for compared_name in names
        ]
