import csv
import logging

from injector import singleton

from src.app.ports.output.repositories.name_repository import NameRepository
from src.domain.model.name import Name


logger = logging.getLogger("uvicorn")


@singleton
class NameRepositoryDict(NameRepository):
    __db: dict[str, Name]

    def __init__(self):
        with open("src/infrastructure/adapters/output/repositories/name/names_dataset.csv", newline="") as csvfile:
            data = csv.DictReader(csvfile)

            self.__db = {row["ID"]: Name(row["ID"], row["Full Name"]) for row in data}

    def get_all(self) -> list[Name]:
        logger.info("Getting all names")
        return list(self.__db.values())
