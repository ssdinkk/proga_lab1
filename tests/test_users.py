from domain.models.user import User
from application.services.messenger_service import MessengerService
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository


def test_add_and_get_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    user = User(
        id=1,
        username="test_user",
        display_name="Test User"
    )

    service.add_user(user)

    found_user = service.get_user(1)

    assert found_user == user


def test_delete_user():
    repository = InMemoryUserRepository()
    service = MessengerService(repository)

    user = User(
        id=2,
        username="another_user",
        display_name="Another User"
    )

    service.add_user(user)
    service.delete_user(2)

    assert service.get_all_users() == []