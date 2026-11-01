from abc import ABC, abstractmethod

from domain.models.chat import Chat


class ChatRepository(ABC):

    @abstractmethod
    def add(self, chat: Chat) -> None:
        pass

    @abstractmethod
    def get_by_id(self, chat_id: int) -> Chat | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Chat]:
        pass

    @abstractmethod
    def delete(self, chat_id: int) -> None:
        pass