from abc import ABC, abstractmethod

from domain.models.message import Message


class MessageRepository(ABC):

    @abstractmethod
    def add(self, message: Message) -> None:
        pass

    @abstractmethod
    def get_by_id(self, message_id: int) -> Message | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Message]:
        pass

    @abstractmethod
    def update(self, message: Message) -> None:
        pass

    @abstractmethod
    def delete(self, message_id: int) -> None:
        pass

    @abstractmethod
    def get_by_chat(self, chat_id: int) -> list[Message]:
        pass