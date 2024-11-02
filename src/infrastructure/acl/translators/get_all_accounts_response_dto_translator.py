from src.domain.model.account import Account
from src.infrastructure.acl.dto.requests.get_all_accounts_dto import (
    GetAllAccountsResponseDto,
)
from src.infrastructure.acl.translators.account_dto_translator import (
    AccountDtoTranslator,
)


class GetAllAccountsDtoTranslator:

    @staticmethod
    def of(accounts: list[Account]) -> GetAllAccountsResponseDto:
        dtos = [AccountDtoTranslator.of(account) for account in accounts]
        filtered_dtos = [dto for dto in dtos if dto is not None]
        return GetAllAccountsResponseDto(accounts=filtered_dtos)
