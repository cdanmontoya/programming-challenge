from pydantic import BaseModel


class ErrorEventDto(BaseModel):
    message: str
