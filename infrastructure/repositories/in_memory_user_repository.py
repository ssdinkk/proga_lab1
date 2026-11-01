
from domain.models.user import User
from application.interfaces.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users: dict[int, User] = {}

    def add(self, user: User) -> None:
        if user.id in self.users:
            raise ValueError(f"Пользователь с ID {user.id} уже существует")

        self.users[user.id] = user

    def get_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def get_all(self) -> list[User]:
        return list(self.users.values())

    def delete(self, user_id: int) -> None:
        self.users.pop(user_id, None)
