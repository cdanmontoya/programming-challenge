import logging
from uuid import UUID

from fastapi import APIRouter, Response
from injector import inject

from src.app.services.delete_account_service import DeleteAccountService
from src.app.services.get_accounts_service import GetAccountsService
from src.app.services.insert_account_service import InsertAccountService
from src.app.services.update_account_service import UpdateAccountService
from src.domain.error import Error, DomainError
from src.infrastructure.acl.dto.requests.account_dto import AccountDto
from src.infrastructure.acl.dto.requests.get_all_accounts_dto import (
    GetAllAccountsResponseDto,
)
from src.infrastructure.acl.dto.requests.insert_account_request_dto import (
    InsertAccountRequestDto,
)
from src.infrastructure.acl.dto.requests.update_account_request_dto import (
    UpdateAccountRequestDto,
)
from src.infrastructure.acl.translators.account_dto_translator import (
    AccountDtoTranslator,
)
from src.infrastructure.acl.translators.delete_account_request_dto_translator import (
    DeleteAccountRequestDtoTranslator,
)
from src.infrastructure.acl.translators.get_accounts_request_dto_translator import (
    GetAccountByIdRequestDtoTranslator,
)
from src.infrastructure.acl.translators.get_all_accounts_response_dto_translator import (
    GetAllAccountsDtoTranslator,
)
from src.infrastructure.acl.translators.insert_account_request_dto_translator import (
    InsertAccountRequestDtoTranslator,
)
from src.infrastructure.acl.translators.update_account_request_dto_translator import (
    UpdateAccountRequestDtoTranslator,
)
from src.infrastructure.adapters.input.http.utils.utils import get_status_code

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ACCOUNT_PATH = "/{account_id}"


class AccountController:
    router: APIRouter
    __insert_account_service: InsertAccountService
    __get_accounts_service: GetAccountsService
    __delete_account_service: DeleteAccountService
    __update_account_service: UpdateAccountService

    @inject
    def __init__(
        self,
        insert_account_service: InsertAccountService,
        get_accounts_service: GetAccountsService,
        delete_account_service: DeleteAccountService,
        update_account_service: UpdateAccountService,
    ) -> None:
        self.router = APIRouter(
            prefix="/accounts",
            tags=["accounts"],
        )
        self.__insert_account_service = insert_account_service
        self.__get_accounts_service = get_accounts_service
        self.__delete_account_service = delete_account_service
        self.__update_account_service = update_account_service

        self.router.add_api_route("/", self.insert, methods=["POST"])
        self.router.add_api_route("/", self.get_all, methods=["GET"])
        self.router.add_api_route(ACCOUNT_PATH, self.get, methods=["GET"])
        self.router.add_api_route(ACCOUNT_PATH, self.delete, methods=["DELETE"])
        self.router.add_api_route(ACCOUNT_PATH, self.update, methods=["PUT"])

    async def insert(self, request: InsertAccountRequestDto, response: Response) -> AccountDto | Error:
        logger.info("Insert account request received")
        insert_account = InsertAccountRequestDtoTranslator.of(request)
        account_result = self.__insert_account_service.insert(insert_account)

        if isinstance(account_result, Error):
            response.status_code = get_status_code(account_result)
            return account_result
        else:
            return AccountDtoTranslator.of(account_result)

    async def get_all(self) -> GetAllAccountsResponseDto:
        logger.info("Get all accounts request received")
        accounts = self.__get_accounts_service.get_all()
        return GetAllAccountsDtoTranslator.of(accounts)

    async def get(self, account_id: UUID, response: Response) -> AccountDto | Error:
        logger.info("Get account request received")
        get_by_id = GetAccountByIdRequestDtoTranslator.of(account_id)
        account_result = self.__get_accounts_service.get(get_by_id)

        if not account_result:
            error = DomainError("Account not found")
            response.status_code = get_status_code(error)
            return error
        else:
            return AccountDtoTranslator.of(account_result)

    async def delete(self, account_id: UUID, response: Response) -> AccountDto | Error:
        logger.info("Delete account request received")
        delete_account = DeleteAccountRequestDtoTranslator.of(account_id)
        account = self.__delete_account_service.delete(delete_account)

        if isinstance(account, Error):
            return account
        else:
            return AccountDtoTranslator.of(account)

    async def update(self, request: UpdateAccountRequestDto, response: Response) -> AccountDto | Error:
        logger.info("Updated account request received")
        update_account = UpdateAccountRequestDtoTranslator.of(request)
        account_result = self.__update_account_service.update(update_account)

        if isinstance(account_result, Error):
            response.status_code = get_status_code(account_result)
            return account_result
        else:
            return AccountDtoTranslator.of(account_result)
