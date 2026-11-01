from datetime import datetime

import pytest

from domain.models.message import Message
from domain.exceptions import (
    MessageNotFoundException,
    DuplicateEntityException
)

from application.services.message_service import MessageService
from infrastructure.repositories.in_memory_message_repository import (
    InMemoryMessageRepository
)


def create_test_message(message_id=1):
    return Message(
        id=message_id,
        chat_id=1,
        sender_id=1,
        text="Привет!",
        created_at=datetime(2026, 11, 1, 12, 0)
    )


def test_create_and_get_message():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    message = create_test_message()
    service.create_message(message)

    assert service.get_message(1) == message


def test_create_duplicate_message():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    message = create_test_message()
    service.create_message(message)

    with pytest.raises(DuplicateEntityException):
        service.create_message(message)


def test_get_all_messages():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    service.create_message(create_test_message(1))
    service.create_message(create_test_message(2))

    assert len(service.get_all_messages()) == 2


def test_update_message():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    message = create_test_message()
    service.create_message(message)

    updated_message = Message(
        id=1,
        chat_id=1,
        sender_id=1,
        text="Новое сообщение",
        created_at=message.created_at
    )

    service.update_message(updated_message)

    assert service.get_message(1).text == "Новое сообщение"


def test_delete_message():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    service.create_message(create_test_message())
    service.delete_message(1)

    assert service.get_all_messages() == []


def test_get_missing_message():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    with pytest.raises(MessageNotFoundException):
        service.get_message(999)


def test_get_chat_messages():
    repository = InMemoryMessageRepository()
    service = MessageService(repository)

    service.create_message(create_test_message(1))
    service.create_message(create_test_message(2))

    assert len(service.get_chat_messages(1)) == 2