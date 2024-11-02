import logging

from injector import inject

from src.app.commands.delete_account import DeleteAccount
from src.app.ports.output.events.event_publisher import publishes, EventPublisher
from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.error import Error
from src.domain.events.account_deleted import AccountDeleted, AccountNotDeleted
from src.domain.model.account import Account

logger = logging.getLogger(__name__)


class DeleteAccountService:
    _event_publisher: EventPublisher
    __account_repository: AccountRepository

    @inject
    def __init__(
        self, event_publisher: EventPublisher, account_repository: AccountRepository
    ) -> None:
        self._event_publisher = event_publisher
        self.__account_repository = account_repository

    @publishes(AccountDeleted, AccountNotDeleted)
    def delete(self, delete_account: DeleteAccount) -> Account | Error:
        logger.info(f"Deleting account {delete_account.id}")
        return self.__account_repository.delete(delete_account.id)
