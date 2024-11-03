from typing import Any

from fastapi import APIRouter
from injector import inject

from src.app.use_cases.compare_name_use_case import CompareNameUseCase
from src.domain.model.name import Name
from src.infrastructure.acl.dto.requests.compare_name_request_dto import CompareNameRequestDto
from src.infrastructure.acl.dto.requests.compare_name_response_dto import CompareNameResponseDto
from src.infrastructure.acl.translators.compare_name_request_dto_translator import CompareNameRequestDtoTranslator
from src.infrastructure.acl.translators.compare_name_response_dto_translator import CompareNameResponseDtoTranslator


class NameComparatorController:
    router: APIRouter
    compare_name_use_case: CompareNameUseCase

    @inject
    def __init__(self, compare_name_use_case: CompareNameUseCase):
        self.compare_name_use_case = compare_name_use_case

        self.router = APIRouter(
            prefix="/names",
            tags=["Name Comparator"],
        )

        self.router.add_api_route("/", self.compare_name, methods=["POST"])

    async def compare_name(self, body: CompareNameRequestDto) -> CompareNameResponseDto:
        query = CompareNameRequestDtoTranslator.of(body)
        result = self.compare_name_use_case.compare_name(query)
        return CompareNameResponseDtoTranslator.of(result)
