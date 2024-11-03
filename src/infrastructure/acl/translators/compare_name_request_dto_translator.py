from src.app.queries.compare_name import CompareName
from src.infrastructure.acl.dto.requests.compare_name_request_dto import CompareNameRequestDto


class CompareNameRequestDtoTranslator:

    @staticmethod
    def of(request_dto: CompareNameRequestDto) -> CompareName:
        return CompareName(name=request_dto.name, threshold=request_dto.threshold)
