from domain.models.chat_member import ChatMember
from application.interfaces.chat_member_repository import (
    ChatMemberRepository
)
from domain.exceptions import (
    ChatMemberNotFoundException,
    DuplicateEntityException
)


class ChatMemberService:

    def __init__(self, member_repository: ChatMemberRepository):
        self.member_repository = member_repository

    def add_member(self, member: ChatMember) -> None:
        if self.member_repository.get_by_id(member.id) is not None:
            raise DuplicateEntityException(
                f"Участник с ID {member.id} уже существует"
            )

        self.member_repository.add(member)

    def get_member(self, member_id: int) -> ChatMember:
        member = self.member_repository.get_by_id(member_id)

        if member is None:
            raise ChatMemberNotFoundException(
                f"Участник с ID {member_id} не найден"
            )

        return member

    def get_all_members(self) -> list[ChatMember]:
        return self.member_repository.get_all()

    def update_member(self, member: ChatMember) -> None:
        self.get_member(member.id)
        self.member_repository.update(member)

    def delete_member(self, member_id: int) -> None:
        self.get_member(member_id)
        self.member_repository.delete(member_id)

    def get_chat_members(self, chat_id: int) -> list[ChatMember]:
        return self.member_repository.get_by_chat(chat_id)