from dataclasses import dataclass


@dataclass(frozen=True)
class CompareName:
    name: str
    threshold: float
