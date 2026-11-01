import pytest

from domain.models.user import User
from application.services.messenger_service import MessengerService
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from domain.exceptions import UserNotFoundException, DuplicateEntityException


def test_add_and_get_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    user = User(id=1, username="test_user", display_name="Test User")
    service.add_user(user)

    found_user = service.get_user(1)

    assert found_user == user


def test_delete_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    user = User(id=2, username="another_user", display_name="Another User")
    service.add_user(user)
    service.delete_user(2)

    assert service.get_all_users() == []


def test_add_duplicate_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    user = User(id=3, username="test_user", display_name="Test User")
    service.add_user(user)

    with pytest.raises(DuplicateEntityException):
        service.add_user(user)


def test_get_missing_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    with pytest.raises(UserNotFoundException):
        service.get_user(999)