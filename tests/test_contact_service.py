import pytest

from domain.models.contact import Contact
from domain.exceptions import (
    ContactNotFoundException,
    DuplicateEntityException
)

from application.services.contact_service import ContactService
from infrastructure.repositories.in_memory_contact_repository import (
    InMemoryContactRepository
)


def create_test_contact(contact_id=1):
    return Contact(
        id=contact_id,
        owner_id=1,
        contact_user_id=2,
        nickname="Друг"
    )


def test_create_and_get_contact():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    contact = create_test_contact()
    service.create_contact(contact)

    assert service.get_contact(1) == contact


def test_create_duplicate_contact():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    contact = create_test_contact()
    service.create_contact(contact)

    with pytest.raises(DuplicateEntityException):
        service.create_contact(contact)


def test_get_all_contacts():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    service.create_contact(create_test_contact(1))
    service.create_contact(create_test_contact(2))

    assert len(service.get_all_contacts()) == 2


def test_update_contact():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    contact = create_test_contact()
    service.create_contact(contact)

    updated_contact = Contact(
        id=1,
        owner_id=1,
        contact_user_id=2,
        nickname="Лучший друг"
    )

    service.update_contact(updated_contact)

    assert service.get_contact(1).nickname == "Лучший друг"


def test_delete_contact():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    service.create_contact(create_test_contact())
    service.delete_contact(1)

    assert service.get_all_contacts() == []


def test_get_missing_contact():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    with pytest.raises(ContactNotFoundException):
        service.get_contact(999)


def test_get_user_contacts():
    repository = InMemoryContactRepository()
    service = ContactService(repository)

    service.create_contact(create_test_contact(1))
    service.create_contact(create_test_contact(2))

    contacts = service.get_user_contacts(1)

    assert len(contacts) == 2
    assert all(contact.owner_id == 1 for contact in contacts)