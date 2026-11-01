from domain.models.attachment import Attachment
from application.interfaces.attachment_repository import (
    AttachmentRepository
)
from domain.exceptions import (
    AttachmentNotFoundException,
    DuplicateEntityException
)


class AttachmentService:

    def __init__(self, attachment_repository: AttachmentRepository):
        self.attachment_repository = attachment_repository

    def add_attachment(self, attachment: Attachment) -> None:
        if self.attachment_repository.get_by_id(attachment.id) is not None:
            raise DuplicateEntityException(
                f"Вложение с ID {attachment.id} уже существует"
            )

        self.attachment_repository.add(attachment)

    def get_attachment(self, attachment_id: int) -> Attachment:
        attachment = self.attachment_repository.get_by_id(attachment_id)

        if attachment is None:
            raise AttachmentNotFoundException(
                f"Вложение с ID {attachment_id} не найдено"
            )

        return attachment

    def get_all_attachments(self) -> list[Attachment]:
        return self.attachment_repository.get_all()

    def update_attachment(self, attachment: Attachment) -> None:
        self.get_attachment(attachment.id)
        self.attachment_repository.update(attachment)

    def delete_attachment(self, attachment_id: int) -> None:
        self.get_attachment(attachment_id)
        self.attachment_repository.delete(attachment_id)

    def get_message_attachments(
        self,
        message_id: int
    ) -> list[Attachment]:
        return self.attachment_repository.get_by_message(message_id)