from starlette import status

from src.domain.error import Error, DomainError, TechnicalError


def get_status_code(error: Error) -> int:
    if isinstance(error, DomainError):
        return status.HTTP_400_BAD_REQUEST

    if isinstance(error, TechnicalError):
        return status.HTTP_500_INTERNAL_SERVER_ERROR

    return status.HTTP_200_OK
