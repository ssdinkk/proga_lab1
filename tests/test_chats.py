from datetime import datetime

from domain.models.chat import Chat
from infrastructure.repositories.in_memory_chat_repository import InMemoryChatRepository


def test_add_and_get_chat():
    repository = InMemoryChatRepository()
    chat = Chat(
        id=1,
        title="Test chat",
        created_at=datetime.now()
    )

    repository.add(chat)

    assert repository.get_by_id(1) == chat


def test_delete_chat():
    repository = InMemoryChatRepository()
    chat = Chat(
        id=2,
        title="Another chat",
        created_at=datetime.now()
    )

    repository.add(chat)
    repository.delete(2)

    assert repository.get_all() == []