import factory
from faker import Faker

from src.domain.model.contact_information import ContactInformation

fake = Faker()


class ContactInformationFactory(factory.Factory):
    class Meta:
        model = ContactInformation

    email = fake.email(domain="email.com")
    cellphones = [fake.phone_number()]
