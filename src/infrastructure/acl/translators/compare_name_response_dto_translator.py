from src.domain.model.name import Name
from src.infrastructure.acl.dto.requests.compare_name_response_dto import CompareNameResponseDto


class CompareNameResponseDtoTranslator:

    @staticmethod
    def of(names: list[tuple[Name, float]]) -> CompareNameResponseDto:
        mapped_names = {
            name_similarity[0].id: {"name": name_similarity[0].full_name, "similarity": name_similarity[1]}
            for name_similarity in names
        }

        return CompareNameResponseDto.model_validate(mapped_names)
