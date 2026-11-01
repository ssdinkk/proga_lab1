from domain.models.chat import Chat
from application.interfaces.chat_repository import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def create_chat(self, chat: Chat) -> None:
        if self.chat_repository.get_by_id(chat.id) is not None:
            raise ValueError(f"Чат с ID {chat.id} уже существует")

        self.chat_repository.add(chat)

    def get_chat(self, chat_id: int) -> Chat:
        chat = self.chat_repository.get_by_id(chat_id)

        if chat is None:
            raise ValueError(f"Чат с ID {chat_id} не найден")

        return chat

    def get_all_chats(self) -> list[Chat]:
        return self.chat_repository.get_all()

    def delete_chat(self, chat_id: int) -> None:
        self.get_chat(chat_id)
        self.chat_repository.delete(chat_id)