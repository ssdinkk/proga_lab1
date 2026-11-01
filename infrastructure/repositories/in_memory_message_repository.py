from domain.models.message import Message
from application.interfaces.message_repository import MessageRepository


class InMemoryMessageRepository(MessageRepository):

    def __init__(self):
        self.messages: dict[int, Message] = {}

    def add(self, message: Message) -> None:
        if message.id in self.messages:
            raise ValueError(
                f"Сообщение с ID {message.id} уже существует"
            )

        self.messages[message.id] = message

    def get_by_id(self, message_id: int) -> Message | None:
        return self.messages.get(message_id)

    def get_all(self) -> list[Message]:
        return list(self.messages.values())

    def update(self, message: Message) -> None:
        if message.id not in self.messages:
            raise ValueError(
                f"Сообщение с ID {message.id} не найдено"
            )

        self.messages[message.id] = message

    def delete(self, message_id: int) -> None:
        if message_id not in self.messages:
            raise ValueError(
                f"Сообщение с ID {message_id} не найдено"
            )

        del self.messages[message_id]

    def get_by_chat(self, chat_id: int) -> list[Message]:
        return [
            message
            for message in self.messages.values()
            if message.chat_id == chat_id
        ]