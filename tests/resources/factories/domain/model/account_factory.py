import uuid

import factory
from factory import SubFactory

from src.domain.model.account import Account, AccountId
from tests.resources.factories.domain.model.contact_information_factory import (
    ContactInformationFactory,
)


class AccountIdFactory(factory.Factory):
    class Meta:
        model = AccountId

    id = uuid.uuid4()


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    id: SubFactory = SubFactory(AccountIdFactory)
    contact_information: SubFactory = SubFactory(ContactInformationFactory)
