import logging

from src.infrastructure.acl.dto.events.integration_event import IntegrationEvent
from src.infrastructure.acl.dto.events.python_template.account_deleted import (
    AccountNotDeletedDto,
)

logger = logging.getLogger(__name__)


class AccountNotDeletedProcessor:

    def parse_event(self, event: IntegrationEvent) -> AccountNotDeletedDto:
        return AccountNotDeletedDto.model_validate(event.event.data)

    def process_event(self, event: AccountNotDeletedDto) -> None:
        logger.info("Sending notification")
        logger.info(
            f"Notification: The account has not been deleted. Reason: {event.message}"
        )

    async def handle_event(self, event: IntegrationEvent) -> None:
        logger.info(f"Processing event {event.event.id}")
        parsed_event = self.parse_event(event)
        self.process_event(parsed_event)
