import pytest
from datetime import datetime

from domain.models.chat_member import ChatMember
from domain.exceptions import (
    ChatMemberNotFoundException,
    DuplicateEntityException
)
from application.services.chat_member_service import ChatMemberService
from infrastructure.repositories.in_memory_chat_member_repository import (
    InMemoryChatMemberRepository
)


@pytest.fixture
def service():
    repository = InMemoryChatMemberRepository()
    return ChatMemberService(repository)


def create_test_member(member_id=1, role="member"):
    return ChatMember(
        id=member_id,
        chat_id=10,
        user_id=5,
        joined_at=datetime(2026, 11, 1, 12, 0),
        role=role
    )


def test_add_and_get_member(service):
    member = create_test_member()

    service.add_member(member)

    assert service.get_member(1) == member


def test_add_duplicate_member(service):
    member = create_test_member()

    service.add_member(member)

    with pytest.raises(DuplicateEntityException):
        service.add_member(member)


def test_get_all_members(service):
    first = create_test_member(1)
    second = create_test_member(2)

    service.add_member(first)
    service.add_member(second)

    assert service.get_all_members() == [first, second]


def test_update_member(service):
    member = create_test_member()
    service.add_member(member)

    updated_member = create_test_member(role="admin")
    service.update_member(updated_member)

    assert service.get_member(1).role == "admin"


def test_delete_member(service):
    service.add_member(create_test_member())

    service.delete_member(1)

    assert service.get_all_members() == []


def test_get_missing_member(service):
    with pytest.raises(ChatMemberNotFoundException):
        service.get_member(999)


def test_get_chat_members(service):
    first = create_test_member(1)
    second = create_test_member(2)
    third = create_test_member(3)

    third.chat_id = 20

    service.add_member(first)
    service.add_member(second)
    service.add_member(third)

    assert service.get_chat_members(10) == [first, second]