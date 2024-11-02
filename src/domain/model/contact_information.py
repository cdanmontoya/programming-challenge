from dataclasses import dataclass


@dataclass()
class ContactInformation:
    email: str
    cellphones: list[str]
