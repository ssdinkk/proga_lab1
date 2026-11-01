import pytest
from datetime import datetime

from domain.models.reaction import Reaction
from domain.exceptions import (
    ReactionNotFoundException,
    DuplicateEntityException
)
from application.services.reaction_service import ReactionService
from infrastructure.repositories.in_memory_reaction_repository import (
    InMemoryReactionRepository
)


@pytest.fixture
def service():
    repository = InMemoryReactionRepository()
    return ReactionService(repository)


def create_test_reaction(reaction_id=1, emoji="👍"):
    return Reaction(
        id=reaction_id,
        message_id=10,
        user_id=5,
        emoji=emoji,
        created_at=datetime(2026, 11, 1, 12, 0)
    )


def test_add_and_get_reaction(service):
    reaction = create_test_reaction()

    service.add_reaction(reaction)

    assert service.get_reaction(1) == reaction


def test_add_duplicate_reaction(service):
    reaction = create_test_reaction()
    service.add_reaction(reaction)

    with pytest.raises(DuplicateEntityException):
        service.add_reaction(reaction)


def test_get_all_reactions(service):
    first = create_test_reaction(1)
    second = create_test_reaction(2, "❤️")

    service.add_reaction(first)
    service.add_reaction(second)

    assert service.get_all_reactions() == [first, second]


def test_update_reaction(service):
    reaction = create_test_reaction()
    service.add_reaction(reaction)

    updated = create_test_reaction(1, "🔥")
    service.update_reaction(updated)

    assert service.get_reaction(1).emoji == "🔥"


def test_delete_reaction(service):
    service.add_reaction(create_test_reaction())

    service.delete_reaction(1)

    assert service.get_all_reactions() == []


def test_get_missing_reaction(service):
    with pytest.raises(ReactionNotFoundException):
        service.get_reaction(999)


def test_get_message_reactions(service):
    first = create_test_reaction(1)
    second = create_test_reaction(2, "❤️")

    third = create_test_reaction(3, "🔥")
    third.message_id = 20

    service.add_reaction(first)
    service.add_reaction(second)
    service.add_reaction(third)

    assert service.get_message_reactions(10) == [first, second]