import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from injector import Injector

from src.app.ports.input.events.event_consumer import EventConsumer
from src.infrastructure.adapters.input.http.account_controller import AccountController
from src.infrastructure.config.observability.correlation_id.correlation_id import (
    CorrelationIdMiddleware,
)
from src.infrastructure.adapters.input.http.health_status_controller import (
    HealthStatusController,
)


class Application:
    __health_status_controller: HealthStatusController
    __account_controller: AccountController
    _event_consumer: EventConsumer

    def __init__(self, injector: Injector) -> None:
        self.__account_controller = injector.get(AccountController)
        self.__health_status_controller = injector.get(HealthStatusController)
        self.__event_consumer = injector.get(EventConsumer)

    @asynccontextmanager
    async def lifespan(self, app: FastAPI) -> AsyncGenerator[None]:
        loop = asyncio.get_running_loop()
        task = loop.create_task(self.__event_consumer.run())
        await task
        yield

    def create_app(self) -> FastAPI:
        application = FastAPI(lifespan=self.lifespan)
        application.include_router(self.__account_controller.router)
        application.include_router(self.__health_status_controller.router)
        application.add_middleware(CorrelationIdMiddleware)

        return application
