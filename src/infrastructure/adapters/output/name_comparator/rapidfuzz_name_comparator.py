import logging
from difflib import SequenceMatcher

from rapidfuzz import fuzz, process

from src.app.ports.output.name_comparator.name_comparator import NameComparator
from src.domain.model.name import Name


logger = logging.getLogger("uvicorn")


class RappidFuzzNameComparator(NameComparator):

    def compare(self, name: str, names: list[Name]) -> list[tuple[Name, float]]:
        logger.info(f"Comparing name {name} against all available names")

        choices = [compared_name.full_name for compared_name in names]

        ratios = process.extract(name, choices, scorer=fuzz.WRatio)




        fuzz.ratio()
        return [
            (compared_name, ) for compared_name in names
        ]
