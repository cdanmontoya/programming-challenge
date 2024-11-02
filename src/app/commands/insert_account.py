from dataclasses import dataclass


@dataclass(frozen=True)
class InsertAccount:
    email: str
    cellphones: list[str]
