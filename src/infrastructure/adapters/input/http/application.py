from fastapi import FastAPI
from injector import Injector

from src.infrastructure.adapters.input.http.health_status_controller import (
    HealthStatusController,
)
from src.infrastructure.adapters.input.http.name_comparator_controller import NameComparatorController
from src.infrastructure.config.observability.correlation_id.correlation_id import (
    CorrelationIdMiddleware,
)


class Application:
    __health_status_controller: HealthStatusController
    __name_comparator_controller: NameComparatorController

    def __init__(self, injector: Injector) -> None:
        self.__name_comparator_controller = injector.get(NameComparatorController)
        self.__health_status_controller = injector.get(HealthStatusController)

    def create_app(self) -> FastAPI:
        application = FastAPI()
        application.include_router(self.__name_comparator_controller.router)
        application.include_router(self.__health_status_controller.router)
        application.add_middleware(CorrelationIdMiddleware)

        return application
