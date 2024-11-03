import logging
import os

import pika
from aio_pika.abc import AbstractRobustConnection
from injector import singleton, inject
from pika.adapters.blocking_connection import BlockingConnection

from src.app.ports.output.events.event_publisher import EventPublisher
from src.domain.events.event import Event
from src.infrastructure.acl.translators.event_dto_translator import to_json

logger = logging.getLogger(__name__)


@singleton
class RabbitMqEventPublisher(EventPublisher):
    _connection: AbstractRobustConnection

    @inject
    def __init__(self, connection: BlockingConnection = None) -> None:
        connection = (
            pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=os.getenv("MESSAGE_BROKER_HOST", "localhost"),
                    port=os.getenv("MESSAGE_BROKER_PORT", 5672),
                    heartbeat=0,
                )
            )
            if not connection
            else connection
        )
        self._channel = connection.channel()

    def publish(self, event: Event) -> None:
        self._channel.exchange_declare(
            exchange=f"{event.source}.{event.name}",
            exchange_type="fanout",
        )
        self._channel.basic_publish(exchange=f"{event.source}.{event.name}", routing_key="", body=to_json(event))
        logger.info(f"Published event {event.name} with id {event.id}")
