from domain.models.reaction import Reaction
from application.interfaces.reaction_repository import (
    ReactionRepository
)
from domain.exceptions import (
    ReactionNotFoundException,
    DuplicateEntityException
)


class ReactionService:

    def __init__(self, reaction_repository: ReactionRepository):
        self.reaction_repository = reaction_repository

    def add_reaction(self, reaction: Reaction) -> None:
        if self.reaction_repository.get_by_id(reaction.id) is not None:
            raise DuplicateEntityException(
                f"Реакция с ID {reaction.id} уже существует"
            )

        self.reaction_repository.add(reaction)

    def get_reaction(self, reaction_id: int) -> Reaction:
        reaction = self.reaction_repository.get_by_id(reaction_id)

        if reaction is None:
            raise ReactionNotFoundException(
                f"Реакция с ID {reaction_id} не найдена"
            )

        return reaction

    def get_all_reactions(self) -> list[Reaction]:
        return self.reaction_repository.get_all()

    def update_reaction(self, reaction: Reaction) -> None:
        self.get_reaction(reaction.id)
        self.reaction_repository.update(reaction)

    def delete_reaction(self, reaction_id: int) -> None:
        self.get_reaction(reaction_id)
        self.reaction_repository.delete(reaction_id)

    def get_message_reactions(self, message_id: int) -> list[Reaction]:
        return self.reaction_repository.get_by_message(message_id)