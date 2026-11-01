from domain.models.chat_member import ChatMember
from application.interfaces.chat_member_repository import (
    ChatMemberRepository
)


class InMemoryChatMemberRepository(ChatMemberRepository):

    def __init__(self):
        self.members: dict[int, ChatMember] = {}

    def add(self, member: ChatMember) -> None:
        if member.id in self.members:
            raise ValueError(
                f"Участник с ID {member.id} уже существует"
            )

        self.members[member.id] = member

    def get_by_id(self, member_id: int) -> ChatMember | None:
        return self.members.get(member_id)

    def get_all(self) -> list[ChatMember]:
        return list(self.members.values())

    def update(self, member: ChatMember) -> None:
        if member.id not in self.members:
            raise ValueError(
                f"Участник с ID {member.id} не найден"
            )

        self.members[member.id] = member

    def delete(self, member_id: int) -> None:
        if member_id not in self.members:
            raise ValueError(
                f"Участник с ID {member_id} не найден"
            )

        del self.members[member_id]

    def get_by_chat(self, chat_id: int) -> list[ChatMember]:
        return [
            member
            for member in self.members.values()
            if member.chat_id == chat_id
        ]