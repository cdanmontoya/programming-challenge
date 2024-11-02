from dataclasses import dataclass


@dataclass(frozen=True)
class Error(Exception):
    message: str


class DomainError(Error):
    message: str


class TechnicalError(Error):
    message: str
