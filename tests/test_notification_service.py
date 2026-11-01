import pytest
from datetime import datetime

from domain.models.notification import Notification
from domain.exceptions import (
    NotificationNotFoundException,
    DuplicateEntityException
)
from application.services.notification_service import NotificationService
from infrastructure.repositories.in_memory_notification_repository import (
    InMemoryNotificationRepository
)


@pytest.fixture
def service():
    repository = InMemoryNotificationRepository()
    return NotificationService(repository)


def create_test_notification(notification_id=1, is_read=False):
    return Notification(
        id=notification_id,
        user_id=5,
        message="Новое сообщение",
        created_at=datetime(2026, 11, 1, 12, 0),
        is_read=is_read
    )


def test_add_and_get_notification(service):
    notification = create_test_notification()

    service.add_notification(notification)

    assert service.get_notification(1) == notification


def test_add_duplicate_notification(service):
    notification = create_test_notification()
    service.add_notification(notification)

    with pytest.raises(DuplicateEntityException):
        service.add_notification(notification)


def test_get_all_notifications(service):
    first = create_test_notification(1)
    second = create_test_notification(2)

    service.add_notification(first)
    service.add_notification(second)

    assert service.get_all_notifications() == [first, second]


def test_update_notification(service):
    notification = create_test_notification()
    service.add_notification(notification)

    updated = create_test_notification(1, is_read=True)
    service.update_notification(updated)

    assert service.get_notification(1).is_read is True


def test_delete_notification(service):
    service.add_notification(create_test_notification())

    service.delete_notification(1)

    assert service.get_all_notifications() == []


def test_get_missing_notification(service):
    with pytest.raises(NotificationNotFoundException):
        service.get_notification(999)


def test_get_user_notifications(service):
    first = create_test_notification(1)
    second = create_test_notification(2)

    third = create_test_notification(3)
    third.user_id = 10

    service.add_notification(first)
    service.add_notification(second)
    service.add_notification(third)

    assert service.get_user_notifications(5) == [first, second]