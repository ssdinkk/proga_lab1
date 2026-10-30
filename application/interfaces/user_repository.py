
from abc import ABC, abstractmethod

from domain.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass
