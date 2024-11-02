from pydantic import BaseModel


class InsertAccountRequestDto(BaseModel):
    email: str
    cellphones: list[str]
