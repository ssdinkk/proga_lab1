from abc import ABC, abstractmethod

from domain.models.attachment import Attachment


class AttachmentRepository(ABC):

    @abstractmethod
    def add(self, attachment: Attachment) -> None:
        pass

    @abstractmethod
    def get_by_id(self, attachment_id: int) -> Attachment | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Attachment]:
        pass

    @abstractmethod
    def update(self, attachment: Attachment) -> None:
        pass

    @abstractmethod
    def delete(self, attachment_id: int) -> None:
        pass

    @abstractmethod
    def get_by_message(self, message_id: int) -> list[Attachment]:
        pass