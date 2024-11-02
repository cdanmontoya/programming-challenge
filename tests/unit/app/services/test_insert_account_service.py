from pytest import fixture

from src.app.commands.insert_account import InsertAccount
from src.app.services.insert_account_service import InsertAccountService
from src.domain.error import DomainError
from src.domain.services.validation_service import ValidationService
from src.infrastructure.adapters.output.events.console_event_publisher import (
    ConsoleEventPublisher,
)


@fixture
def service() -> InsertAccountService:
    validation_service = ValidationService()
    event_publisher = ConsoleEventPublisher()
    return InsertAccountService(None, validation_service, event_publisher)


def test_given_an_invalid_account_should_return_true(
    service: InsertAccountService,
) -> None:
    insert_account = InsertAccount(email="old@invalid", cellphones=[])

    result = service.insert(insert_account)

    assert isinstance(result, DomainError)
