import logging
from uuid import uuid4

from injector import inject

from src.app.commands.insert_account import InsertAccount
from src.app.ports.output.events.event_publisher import EventPublisher, publishes
from src.app.ports.output.repositories.account_repository import AccountRepository
from src.domain.error import Error, DomainError
from src.domain.events.account_inserted import AccountInserted, AccountNotInserted
from src.domain.model.account import Account, AccountId
from src.domain.model.contact_information import ContactInformation
from src.domain.services.validation_service import ValidationService

logger = logging.getLogger(__name__)


class InsertAccountService:
    _event_publisher: EventPublisher
    __account_repository: AccountRepository
    __validation_service: ValidationService
    __EMAIL_DOMAIN: str

    @inject
    def __init__(
        self,
        account_repository: AccountRepository,
        validation_service: ValidationService,
        event_publisher: EventPublisher,
    ) -> None:
        self._event_publisher = event_publisher
        self.__account_repository = account_repository
        self.__validation_service = validation_service
        self.__EMAIL_DOMAIN = "email.com"

    @publishes(AccountInserted, AccountNotInserted)
    def insert(self, insert_account: InsertAccount) -> Account | Error:
        account = Account(
            AccountId(uuid4()),
            ContactInformation(insert_account.email, insert_account.cellphones),
        )

        is_valid = self.__validation_service.is_valid(account, self.__EMAIL_DOMAIN)

        if is_valid:
            logger.info(f"Inserting account {account.id}")
            return self.__account_repository.insert(account)
        else:
            logger.info(f"Account {account} is not valid")
            return DomainError(f"Account {account} is not valid")
