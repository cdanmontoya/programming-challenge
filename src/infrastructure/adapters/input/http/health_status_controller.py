import os

from fastapi import APIRouter
from injector import inject


class HealthStatusController:
    router: APIRouter

    @inject
    def __init__(self) -> None:
        self.router = APIRouter(
            prefix="/status",
            tags=["status"],
        )

        self.router.add_api_route("/", self.get_status, methods=["GET"])

    @staticmethod
    async def get_status() -> dict[str, str]:
        return {"application_name": os.getenv("APP_NAME", "undefined"), "status": "ok"}
