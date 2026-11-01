from domain.models.contact import Contact
from application.interfaces.contact_repository import ContactRepository
from domain.exceptions import (
    ContactNotFoundException,
    DuplicateEntityException
)


class ContactService:

    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def create_contact(self, contact: Contact) -> None:
        if self.contact_repository.get_by_id(contact.id) is not None:
            raise DuplicateEntityException(
                f"Контакт с ID {contact.id} уже существует"
            )

        self.contact_repository.add(contact)

    def get_contact(self, contact_id: int) -> Contact:
        contact = self.contact_repository.get_by_id(contact_id)

        if contact is None:
            raise ContactNotFoundException(
                f"Контакт с ID {contact_id} не найден"
            )

        return contact

    def get_all_contacts(self) -> list[Contact]:
        return self.contact_repository.get_all()

    def update_contact(self, contact: Contact) -> None:
        self.get_contact(contact.id)
        self.contact_repository.update(contact)

    def delete_contact(self, contact_id: int) -> None:
        self.get_contact(contact_id)
        self.contact_repository.delete(contact_id)

    def get_user_contacts(self, owner_id: int) -> list[Contact]:
        return self.contact_repository.get_by_owner(owner_id)