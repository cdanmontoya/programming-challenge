from uuid import UUID

from src.app.commands.delete_account import DeleteAccount
from src.domain.model.account import AccountId


class DeleteAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UUID) -> DeleteAccount:
        return DeleteAccount(AccountId(request_dto))
