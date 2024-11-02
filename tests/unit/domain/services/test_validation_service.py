import pytest

from src.domain.services.validation_service import ValidationService
from tests.resources.factories.domain.model.account_factory import AccountFactory
from tests.resources.factories.domain.model.contact_information_factory import (
    ContactInformationFactory,
)


@pytest.fixture
def service() -> ValidationService:
    return ValidationService()


def test_given_a_valid_account_should_return_true(service: ValidationService) -> None:
    account = AccountFactory.create()

    result = service.is_valid(account, "email.com")

    assert result is True


def test_given_an_invalid_email_pattern_should_return_false(
    service: ValidationService,
) -> None:
    contact_information = ContactInformationFactory(email="acco@unt@email.com")
    account = AccountFactory.create(contact_information=contact_information)

    result = service.is_valid(account, "email.com")

    assert result is False


def test_given_a_valid_pattern_and_invalid_domain_should_return_false(
    service: ValidationService,
) -> None:
    contact_information = ContactInformationFactory(email="account@email.com")
    account = AccountFactory.create(contact_information=contact_information)

    result = service.is_valid(account, "fakemail.com")

    assert result is False
