from uuid import UUID

from src.app.queries.get_account_by_id import GetAccountById
from src.domain.model.account import AccountId


class GetAccountByIdRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UUID) -> GetAccountById:
        return GetAccountById(AccountId(request_dto))
