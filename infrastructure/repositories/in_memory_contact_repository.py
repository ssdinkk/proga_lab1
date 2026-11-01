from domain.models.contact import Contact
from application.interfaces.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):

    def __init__(self):
        self.contacts: dict[int, Contact] = {}

    def add(self, contact: Contact) -> None:
        if contact.id in self.contacts:
            raise ValueError(
                f"Контакт с ID {contact.id} уже существует"
            )

        self.contacts[contact.id] = contact

    def get_by_id(self, contact_id: int) -> Contact | None:
        return self.contacts.get(contact_id)

    def get_all(self) -> list[Contact]:
        return list(self.contacts.values())

    def update(self, contact: Contact) -> None:
        if contact.id not in self.contacts:
            raise ValueError(
                f"Контакт с ID {contact.id} не найден"
            )

        self.contacts[contact.id] = contact

    def delete(self, contact_id: int) -> None:
        if contact_id not in self.contacts:
            raise ValueError(
                f"Контакт с ID {contact_id} не найден"
            )

        del self.contacts[contact_id]

    def get_by_owner(self, owner_id: int) -> list[Contact]:
        return [
            contact
            for contact in self.contacts.values()
            if contact.owner_id == owner_id
        ]