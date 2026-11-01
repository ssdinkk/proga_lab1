from domain.models.notification import Notification
from application.interfaces.notification_repository import (
    NotificationRepository
)
from domain.exceptions import (
    NotificationNotFoundException,
    DuplicateEntityException
)


class NotificationService:

    def __init__(
        self,
        notification_repository: NotificationRepository
    ):
        self.notification_repository = notification_repository

    def add_notification(self, notification: Notification) -> None:
        if (
            self.notification_repository.get_by_id(notification.id)
            is not None
        ):
            raise DuplicateEntityException(
                f"Уведомление с ID {notification.id} уже существует"
            )

        self.notification_repository.add(notification)

    def get_notification(self, notification_id: int) -> Notification:
        notification = self.notification_repository.get_by_id(
            notification_id
        )

        if notification is None:
            raise NotificationNotFoundException(
                f"Уведомление с ID {notification_id} не найдено"
            )

        return notification

    def get_all_notifications(self) -> list[Notification]:
        return self.notification_repository.get_all()

    def update_notification(self, notification: Notification) -> None:
        self.get_notification(notification.id)
        self.notification_repository.update(notification)

    def delete_notification(self, notification_id: int) -> None:
        self.get_notification(notification_id)
        self.notification_repository.delete(notification_id)

    def get_user_notifications(
        self,
        user_id: int
    ) -> list[Notification]:
        return self.notification_repository.get_by_user(user_id)