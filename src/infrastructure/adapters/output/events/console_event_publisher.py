import logging

from src.app.ports.output.events.event_publisher import EventPublisher
from src.domain.events.event import Event
from src.infrastructure.acl.translators.event_dto_translator import to_json

logger = logging.getLogger(__name__)


class ConsoleEventPublisher(EventPublisher):
    def publish(self, event: Event) -> None:
        logger.info(to_json(event))
