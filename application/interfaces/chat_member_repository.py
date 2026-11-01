from abc import ABC, abstractmethod

from domain.models.chat_member import ChatMember


class ChatMemberRepository(ABC):

    @abstractmethod
    def add(self, member: ChatMember) -> None:
        pass

    @abstractmethod
    def get_by_id(self, member_id: int) -> ChatMember | None:
        pass

    @abstractmethod
    def get_all(self) -> list[ChatMember]:
        pass

    @abstractmethod
    def update(self, member: ChatMember) -> None:
        pass

    @abstractmethod
    def delete(self, member_id: int) -> None:
        pass

    @abstractmethod
    def get_by_chat(self, chat_id: int) -> list[ChatMember]:
        pass