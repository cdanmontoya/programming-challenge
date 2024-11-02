import os

import pika
from injector import Module, Binder, provider
from pika.adapters.blocking_connection import BlockingConnection

from src.app.ports.input.events.event_consumer import EventConsumer
from src.app.ports.output.events.event_publisher import EventPublisher
from src.infrastructure.adapters.input.events.rabbit_mq_event_consumer import (
    RabbitMqEventConsumer,
)
from src.infrastructure.adapters.output.events.rabbit_mq_event_publisher import (
    RabbitMqEventPublisher,
)


class PublishersModule(Module):
    @provider
    def message_broker_blocking_connection(self) -> BlockingConnection:
        return pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("MESSAGE_BROKER_HOST", "localhost"),
                port=os.getenv("MESSAGE_BROKER_PORT", 5672),
                heartbeat=0,
            )
        )

    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventPublisher, to=RabbitMqEventPublisher)


class ConsumersModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventConsumer, to=RabbitMqEventConsumer)
