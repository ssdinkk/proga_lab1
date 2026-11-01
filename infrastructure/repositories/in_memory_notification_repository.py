from domain.models.notification import Notification
from application.interfaces.notification_repository import (
    NotificationRepository
)


class InMemoryNotificationRepository(NotificationRepository):

    def __init__(self):
        self.notifications: dict[int, Notification] = {}

    def add(self, notification: Notification) -> None:
        if notification.id in self.notifications:
            raise ValueError(
                f"Уведомление с ID {notification.id} уже существует"
            )

        self.notifications[notification.id] = notification

    def get_by_id(self, notification_id: int) -> Notification | None:
        return self.notifications.get(notification_id)

    def get_all(self) -> list[Notification]:
        return list(self.notifications.values())

    def update(self, notification: Notification) -> None:
        if notification.id not in self.notifications:
            raise ValueError(
                f"Уведомление с ID {notification.id} не найдено"
            )

        self.notifications[notification.id] = notification

    def delete(self, notification_id: int) -> None:
        if notification_id not in self.notifications:
            raise ValueError(
                f"Уведомление с ID {notification_id} не найдено"
            )

        del self.notifications[notification_id]

    def get_by_user(self, user_id: int) -> list[Notification]:
        return [
            notification
            for notification in self.notifications.values()
            if notification.user_id == user_id
        ]