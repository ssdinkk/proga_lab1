import pytest

from domain.models.attachment import Attachment
from domain.exceptions import (
    AttachmentNotFoundException,
    DuplicateEntityException
)
from application.services.attachment_service import AttachmentService
from infrastructure.repositories.in_memory_attachment_repository import (
    InMemoryAttachmentRepository
)


@pytest.fixture
def service():
    repository = InMemoryAttachmentRepository()
    return AttachmentService(repository)


def create_test_attachment(attachment_id=1):
    return Attachment(
        id=attachment_id,
        message_id=10,
        file_name="document.pdf",
        file_path="files/document.pdf",
        file_type="application/pdf"
    )


def test_add_and_get_attachment(service):
    attachment = create_test_attachment()

    service.add_attachment(attachment)

    assert service.get_attachment(1) == attachment


def test_add_duplicate_attachment(service):
    attachment = create_test_attachment()
    service.add_attachment(attachment)

    with pytest.raises(DuplicateEntityException):
        service.add_attachment(attachment)


def test_get_all_attachments(service):
    first = create_test_attachment(1)
    second = create_test_attachment(2)

    service.add_attachment(first)
    service.add_attachment(second)

    assert service.get_all_attachments() == [first, second]


def test_update_attachment(service):
    attachment = create_test_attachment()
    service.add_attachment(attachment)

    updated = Attachment(
        id=1,
        message_id=10,
        file_name="new_document.pdf",
        file_path="files/new_document.pdf",
        file_type="application/pdf"
    )

    service.update_attachment(updated)

    assert service.get_attachment(1).file_name == "new_document.pdf"


def test_delete_attachment(service):
    service.add_attachment(create_test_attachment())

    service.delete_attachment(1)

    assert service.get_all_attachments() == []


def test_get_missing_attachment(service):
    with pytest.raises(AttachmentNotFoundException):
        service.get_attachment(999)


def test_get_message_attachments(service):
    first = create_test_attachment(1)
    second = create_test_attachment(2)

    third = create_test_attachment(3)
    third.message_id = 20

    service.add_attachment(first)
    service.add_attachment(second)
    service.add_attachment(third)

    assert service.get_message_attachments(10) == [first, second]