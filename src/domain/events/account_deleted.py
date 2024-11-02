from src.domain.events.event import Event
from src.domain.model.account import Account


class AccountDeleted(Event):
    def __init__(self, data: Account, version: str = "1.0.0") -> None:
        super().__init__(version, data)


class AccountNotDeleted(Event):
    def __init__(self, data: str, version: str = "1.0.0") -> None:
        super().__init__(version, data)
