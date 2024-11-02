import logging
import os
from collections.abc import Callable, Coroutine
from typing import Any

from aio_pika import connect_robust, RobustConnection
from aio_pika.abc import (
    AbstractIncomingMessage,
    AbstractRobustConnection,
    AbstractRobustChannel,
    AbstractRobustQueue,
    ExchangeType,
)

from src.app.ports.input.events.event_consumer import EventConsumer
from src.infrastructure.acl.dto.events.integration_event import IntegrationEvent
from src.infrastructure.adapters.input.events.python_template.account_inserted import (
    AccountInsertedProcessor,
)
from src.infrastructure.adapters.input.events.python_template.account_not_deleted import (
    AccountNotDeletedProcessor,
)

logger = logging.getLogger(__name__)


class RabbitMqEventConsumer(EventConsumer):
    _connection: AbstractRobustConnection
    _chanel: AbstractRobustChannel
    _queue: AbstractRobustQueue

    def __init__(self, connection: RobustConnection = None) -> None:
        self._connection: RobustConnection = connection
        self._channel: AbstractRobustChannel = None
        self._queue: AbstractRobustQueue = None
        self._event_handlers: dict[str, Callable[IntegrationEvent, None]] = {
            "python_template.AccountNotDeleted": AccountNotDeletedProcessor().handle_event,
            "python_template.AccountInserted": AccountInsertedProcessor().handle_event,
        }

    async def connect(self) -> None:
        if not self._connection:
            self._connection = await connect_robust(
                host=os.getenv("MESSAGE_BROKER_HOST", "localhost"),
                port=int(os.getenv("MESSAGE_BROKER_PORT", 5672)),
                login=os.getenv("MESSAGE_BROKER_USER", "guest"),
                password=os.getenv("MESSAGE_BROKER_PASS", "guest"),
            )
        self._channel = await self._connection.channel()
        self._queue = await self._channel.declare_queue(
            os.getenv("APP_NAME", "undefined")
        )

    async def consume(self) -> None:
        for handler_name in self._event_handlers.keys():
            await self._channel.declare_exchange(handler_name, type=ExchangeType.FANOUT)
            await self._queue.bind(handler_name)

        await self._queue.consume(self.on_message)

    def process_event(self, event: IntegrationEvent) -> Coroutine[Any, Any, None]:
        handler = self._event_handlers.get(f"{event.event.source}.{event.event.name}")
        return handler(event)

    async def on_message(self, message: AbstractIncomingMessage) -> None:
        async with message.process():
            integration_event = IntegrationEvent.model_validate_json(
                message.body.decode("utf-8")
            )
            logger.info(f"Processing event: {integration_event}")
            await self.process_event(integration_event)

    async def run(self) -> None:
        await self.connect()
        await self.consume()
