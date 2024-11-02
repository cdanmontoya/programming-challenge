from src.domain.model.account import Account
from src.infrastructure.acl.dto.requests.account_dto import (
    AccountDto,
    ContactInformationDto,
)


class AccountDtoTranslator:

    @staticmethod
    def of(account: Account) -> AccountDto:
        return AccountDto(
            id=account.id.id,
            contact_information=ContactInformationDto(
                email=account.contact_information.email,
                cellphones=account.contact_information.cellphones,
            ),
        )
