import os

from aio_pika import connect_robust, RobustConnection
from aio_pika.abc import AbstractRobustConnection
from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters
from pytest import fixture
from sqlalchemy import Engine, create_engine
from starlette.testclient import TestClient
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer
from testcontainers.rabbitmq import RabbitMqContainer

from src.app.ports.input.events.event_consumer import EventConsumer
from src.infrastructure.adapters.input.events.rabbit_mq_event_consumer import RabbitMqEventConsumer
from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.config.injector.injector import create_injector


@fixture(scope="session")
def message_broker_conn_params() -> ConnectionParameters:
    rabbit = RabbitMqContainer("rabbitmq:3-management-alpine")

    with rabbit:
        yield rabbit.get_connection_params()


@fixture(scope="session")
def message_broker_blocking_conn(
    message_broker_conn_params: ConnectionParameters,
) -> BlockingConnection:
    return BlockingConnection(
        message_broker_conn_params,
    )


@fixture(scope="session")
async def message_broker_async_conn(
    message_broker_conn_params: ConnectionParameters,
) -> RobustConnection:
    connection = await connect_robust(
        host=message_broker_conn_params.host,
        port=message_broker_conn_params.port,
    )
    yield connection


@fixture(scope="function")
def postgres_container() -> PostgresContainer:
    postgres = PostgresContainer(
        image=os.getenv("DB_IMAGE", "postgres"),
        username=os.getenv("DB_USER", "dbuser"),
        password=os.getenv("DB_PASS", "dbpassword"),
        dbname=os.getenv("DB_DATABASE"),
    )
    with postgres:
        wait_for_logs(
            postgres,
            r"UTC \[1\] LOG:  database system is ready to accept connections",
            10,
        )
        yield postgres


@fixture(scope="function")
def db(postgres_container: PostgresContainer) -> Engine:
    url = postgres_container.get_connection_url()
    engine = create_engine(url, echo=False, future=True)
    yield engine


@fixture(scope="function")
def test_client(
    db: Engine,
    message_broker_blocking_conn: BlockingConnection,
    message_broker_async_conn: RobustConnection,
) -> TestClient:
    inject = create_injector()

    inject.binder.bind(Engine, db)
    inject.binder.bind(BlockingConnection, message_broker_blocking_conn)
    inject.binder.bind(EventConsumer, RabbitMqEventConsumer(message_broker_async_conn))

    return TestClient(Application(inject).create_app())
