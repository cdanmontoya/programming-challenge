from uuid import uuid4

import factory
from faker import Faker

from src.infrastructure.acl.dto.requests.update_account_request_dto import (
    UpdateAccountRequestDto,
)

fake = Faker()


class UpdateAccountRequestDtoFactory(factory.Factory):
    class Meta:
        model = UpdateAccountRequestDto

    id = uuid4()
    email = fake.email()
    cellphones = [fake.phone_number()]
