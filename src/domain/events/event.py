import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import uuid4, UUID


@dataclass
class Event:
    id: UUID
    occurred_on: datetime
    source: str
    name: str
    version: str
    data: Any

    def __init__(self, version: str, data: Any) -> None:
        self.id = uuid4()
        self.occurred_on = datetime.now()
        self.name = self.__class__.__name__
        self.source = os.getenv("APP_NAME", "undefined")
        self.version = version
        self.data = data
