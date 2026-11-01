
from domain.models.chat import Chat
from application.interfaces.chat_repository import ChatRepository


class InMemoryChatRepository(ChatRepository):

    def __init__(self):
        self.chats: dict[int, Chat] = {}

    def add(self, chat: Chat) -> None:
        if chat.id in self.chats:
            raise ValueError(f"Чат с ID {chat.id} уже существует")

        self.chats[chat.id] = chat

    def get_by_id(self, chat_id: int) -> Chat | None:
        return self.chats.get(chat_id)

    def get_all(self) -> list[Chat]:
        return list(self.chats.values())

    def delete(self, chat_id: int) -> None:
        self.chats.pop(chat_id, None)
