from pydantic import BaseModel

from src.infrastructure.acl.dto.requests.account_dto import AccountDto


class GetAllAccountsResponseDto(BaseModel):
    accounts: list[AccountDto]
