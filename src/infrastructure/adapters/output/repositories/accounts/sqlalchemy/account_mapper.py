from src.domain.model.account import Account, AccountId
from src.domain.model.contact_information import ContactInformation
from src.infrastructure.adapters.output.repositories.accounts.sqlalchemy.account_model import (
    AccountDao,
    CellphoneDao,
)


class AccountMapper:

    @staticmethod
    def from_account(account: Account) -> AccountDao:
        return AccountDao(
            id=account.id.id,
            email=account.contact_information.email,
            cellphones=[
                CellphoneDao(cellphone=cellphone)
                for cellphone in account.contact_information.cellphones
            ],
        )

    @staticmethod
    def from_account_dao(account_dao: AccountDao) -> Account:
        contact_information = ContactInformation(
            email=account_dao.email,
            cellphones=[cellphone.cellphone for cellphone in account_dao.cellphones],
        )

        return Account(
            id=AccountId(account_dao.id), contact_information=contact_information
        )
