from datetime import datetime

import pytest

from domain.models.chat import Chat
from application.services.chat_service import ChatService
from infrastructure.repositories.in_memory_chat_repository import InMemoryChatRepository


def test_create_and_get_chat():
    repository = InMemoryChatRepository()
    service = ChatService(repository)

    chat = Chat(id=1, title="Test chat", created_at=datetime.now())
    service.create_chat(chat)

    assert service.get_chat(1) == chat


def test_create_duplicate_chat():
    repository = InMemoryChatRepository()
    service = ChatService(repository)

    chat = Chat(id=1, title="Test chat", created_at=datetime.now())
    service.create_chat(chat)

    with pytest.raises(ValueError):
        service.create_chat(chat)


def test_delete_chat():
    repository = InMemoryChatRepository()
    service = ChatService(repository)

    chat = Chat(id=2, title="Another chat", created_at=datetime.now())
    service.create_chat(chat)
    service.delete_chat(2)

    assert service.get_all_chats() == []


def test_get_missing_chat():
    repository = InMemoryChatRepository()
    service = ChatService(repository)

    with pytest.raises(ValueError):
        service.get_chat(999)