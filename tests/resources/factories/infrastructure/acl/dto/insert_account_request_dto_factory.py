import factory
from faker import Faker

from src.infrastructure.acl.dto.requests.insert_account_request_dto import (
    InsertAccountRequestDto,
)

fake = Faker()


class InsertAccountRequestDtoFactory(factory.Factory):
    class Meta:
        model = InsertAccountRequestDto

    email = fake.email(domain="email.com")
    cellphones = [fake.phone_number()]
