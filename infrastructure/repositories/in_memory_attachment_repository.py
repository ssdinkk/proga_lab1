from domain.models.attachment import Attachment
from application.interfaces.attachment_repository import (
    AttachmentRepository
)


class InMemoryAttachmentRepository(AttachmentRepository):

    def __init__(self):
        self.attachments: dict[int, Attachment] = {}

    def add(self, attachment: Attachment) -> None:
        if attachment.id in self.attachments:
            raise ValueError(
                f"Вложение с ID {attachment.id} уже существует"
            )

        self.attachments[attachment.id] = attachment

    def get_by_id(self, attachment_id: int) -> Attachment | None:
        return self.attachments.get(attachment_id)

    def get_all(self) -> list[Attachment]:
        return list(self.attachments.values())

    def update(self, attachment: Attachment) -> None:
        if attachment.id not in self.attachments:
            raise ValueError(
                f"Вложение с ID {attachment.id} не найдено"
            )

        self.attachments[attachment.id] = attachment

    def delete(self, attachment_id: int) -> None:
        if attachment_id not in self.attachments:
            raise ValueError(
                f"Вложение с ID {attachment_id} не найдено"
            )

        del self.attachments[attachment_id]

    def get_by_message(self, message_id: int) -> list[Attachment]:
        return [
            attachment
            for attachment in self.attachments.values()
            if attachment.message_id == message_id
        ]