
from domain.models.user import User
from application.interfaces.user_repository import UserRepository


class MessengerService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add_user(self, user: User) -> None:
        if self.user_repository.get_by_id(user.id) is not None:
            raise ValueError(f"Пользователь с ID {user.id} уже существует")

        self.user_repository.add(user)

    def get_user(self, user_id: int) -> User:
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise ValueError(f"Пользователь с ID {user_id} не найден")

        return user

    def get_all_users(self) -> list[User]:
        return self.user_repository.get_all()

    def delete_user(self, user_id: int) -> None:
        self.get_user(user_id)
        self.user_repository.delete(user_id)
