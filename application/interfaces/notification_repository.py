from abc import ABC, abstractmethod

from domain.models.notification import Notification


class NotificationRepository(ABC):

    @abstractmethod
    def add(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def get_by_id(self, notification_id: int) -> Notification | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Notification]:
        pass

    @abstractmethod
    def update(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def delete(self, notification_id: int) -> None:
        pass

    @abstractmethod
    def get_by_user(self, user_id: int) -> list[Notification]:
        pass