from abc import ABC, abstractmethod

from domain.models.reaction import Reaction


class ReactionRepository(ABC):

    @abstractmethod
    def add(self, reaction: Reaction) -> None:
        pass

    @abstractmethod
    def get_by_id(self, reaction_id: int) -> Reaction | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Reaction]:
        pass

    @abstractmethod
    def update(self, reaction: Reaction) -> None:
        pass

    @abstractmethod
    def delete(self, reaction_id: int) -> None:
        pass

    @abstractmethod
    def get_by_message(self, message_id: int) -> list[Reaction]:
        pass