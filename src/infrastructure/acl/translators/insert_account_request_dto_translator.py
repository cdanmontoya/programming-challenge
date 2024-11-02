from src.app.commands.insert_account import InsertAccount
from src.infrastructure.acl.dto.requests.insert_account_request_dto import (
    InsertAccountRequestDto,
)


class InsertAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: InsertAccountRequestDto) -> InsertAccount:
        return InsertAccount(request_dto.email, request_dto.cellphones)
