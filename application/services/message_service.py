from domain.models.message import Message
from application.interfaces.message_repository import MessageRepository
from domain.exceptions import (
    MessageNotFoundException,
    DuplicateEntityException
)


class MessageService:

    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def create_message(self, message: Message) -> None:
        if self.message_repository.get_by_id(message.id) is not None:
            raise DuplicateEntityException(
                f"Сообщение с ID {message.id} уже существует"
            )

        self.message_repository.add(message)

    def get_message(self, message_id: int) -> Message:
        message = self.message_repository.get_by_id(message_id)

        if message is None:
            raise MessageNotFoundException(
                f"Сообщение с ID {message_id} не найдено"
            )

        return message

    def get_all_messages(self) -> list[Message]:
        return self.message_repository.get_all()

    def update_message(self, message: Message) -> None:
        self.get_message(message.id)
        self.message_repository.update(message)

    def delete_message(self, message_id: int) -> None:
        self.get_message(message_id)
        self.message_repository.delete(message_id)

    def get_chat_messages(self, chat_id: int) -> list[Message]:
        return self.message_repository.get_by_chat(chat_id)