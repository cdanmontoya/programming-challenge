import logging
import re

from src.domain.model.account import Account
from src.domain.model.contact_information import ContactInformation

logger = logging.getLogger(__name__)


class ValidationService:

    def is_valid(self, account: Account, email_domain: str) -> bool:
        logger.info(
            f"Validating if account {account.id} with email {account.contact_information.email} belongs to "
            f"domain {email_domain}"
        )
        return self.__has_valid_email_pattern(
            account.contact_information
        ) and self.__belongs_to_allowed_domain(
            account.contact_information, email_domain
        )

    @staticmethod
    def __has_valid_email_pattern(contact_information: ContactInformation) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if re.match(pattern, contact_information.email):
            return True
        else:
            return False

    @staticmethod
    def __belongs_to_allowed_domain(
        contact_information: ContactInformation, email_domain: str
    ) -> bool:
        return contact_information.email.endswith(email_domain)
