import logging

from src.infrastructure.acl.dto.events.integration_event import IntegrationEvent
from src.infrastructure.acl.dto.events.python_template.account_inserted import (
    AccountInsertedDto,
)

logger = logging.getLogger(__name__)


class AccountInsertedProcessor:

    def parse_event(self, event: IntegrationEvent) -> AccountInsertedDto:
        return AccountInsertedDto.model_validate(event.event.data)

    def process_event(self, event: AccountInsertedDto) -> None:
        logger.info("Sending account inserted notification")
        logger.info(
            f"Notification: The account {event.id} has been created successfully."
        )

    async def handle_event(self, event: IntegrationEvent) -> None:
        logger.info(f"Processing event {event.event.id}")
        parsed_event = self.parse_event(event)
        self.process_event(parsed_event)
