from domain.models.reaction import Reaction
from application.interfaces.reaction_repository import (
    ReactionRepository
)


class InMemoryReactionRepository(ReactionRepository):

    def __init__(self):
        self.reactions: dict[int, Reaction] = {}

    def add(self, reaction: Reaction) -> None:
        if reaction.id in self.reactions:
            raise ValueError(
                f"Реакция с ID {reaction.id} уже существует"
            )

        self.reactions[reaction.id] = reaction

    def get_by_id(self, reaction_id: int) -> Reaction | None:
        return self.reactions.get(reaction_id)

    def get_all(self) -> list[Reaction]:
        return list(self.reactions.values())

    def update(self, reaction: Reaction) -> None:
        if reaction.id not in self.reactions:
            raise ValueError(
                f"Реакция с ID {reaction.id} не найдена"
            )

        self.reactions[reaction.id] = reaction

    def delete(self, reaction_id: int) -> None:
        if reaction_id not in self.reactions:
            raise ValueError(
                f"Реакция с ID {reaction_id} не найдена"
            )

        del self.reactions[reaction_id]

    def get_by_message(self, message_id: int) -> list[Reaction]:
        return [
            reaction
            for reaction in self.reactions.values()
            if reaction.message_id == message_id
        ]