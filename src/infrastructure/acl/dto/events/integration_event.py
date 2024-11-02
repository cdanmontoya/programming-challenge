from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class EventDto(BaseModel):
    id: UUID
    occurred_on: datetime
    source: str
    name: str
    version: str
    data: Any


class IntegrationEvent(BaseModel):
    event: EventDto
    correlation_id: str | None

