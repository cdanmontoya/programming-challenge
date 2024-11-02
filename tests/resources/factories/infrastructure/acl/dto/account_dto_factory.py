import uuid

import factory
from factory import SubFactory
from faker import Faker

from src.infrastructure.acl.dto.requests.account_dto import (
    ContactInformationDto,
    AccountDto,
)

fake = Faker()


class ContactInformationDtoFactory(factory.Factory):
    class Meta:
        model = ContactInformationDto

    email = fake.email()
    cellphones = [fake.phone_number()]


class AccountDtoFactory(factory.Factory):
    class Meta:
        model = AccountDto

    id = uuid.uuid4()
    contact_information: SubFactory = SubFactory(ContactInformationDtoFactory)
