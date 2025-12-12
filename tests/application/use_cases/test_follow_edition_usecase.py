"""Tests pour les use cases FollowEdition.

This module contains unit tests for FollowEdition use cases.
"""

import pytest

from mangacollec.application.use_cases import (
    FollowEditionV1UseCase,
    UnfollowEditionV1UseCase,
)
from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.exceptions import FollowEditionNotFoundException
from mangacollec.infrastructure.repositories import InMemoryFollowEditionRepository


@pytest.fixture
def repository() -> InMemoryFollowEditionRepository:
    """Fixture pour créer un repository en mémoire."""
    return InMemoryFollowEditionRepository()


@pytest.fixture
def sample_edition_id() -> str:
    """Fixture pour l'ID d'une édition de test."""
    return "edition-456"


class TestFollowEditionV1UseCase:
    """Tests pour FollowEditionV1UseCase."""

    def test_follow_edition_success(self, repository: InMemoryFollowEditionRepository, sample_edition_id: str) -> None:
        """Test de suivi d'une édition avec following=True."""
        usecase = FollowEditionV1UseCase(repository)

        result = usecase(sample_edition_id, True)

        assert isinstance(result, FollowEdition)
        assert result.edition_id == sample_edition_id
        assert result.following is True
        assert result.user_id == "test-user-id"
        assert result.id is not None

    def test_unfollow_edition_success(
        self, repository: InMemoryFollowEditionRepository, sample_edition_id: str
    ) -> None:
        """Test d'arrêt de suivi d'une édition avec following=False."""
        usecase = FollowEditionV1UseCase(repository)

        result = usecase(sample_edition_id, False)

        assert isinstance(result, FollowEdition)
        assert result.edition_id == sample_edition_id
        assert result.following is False

    def test_follow_edition_creates_new_follow(
        self, repository: InMemoryFollowEditionRepository, sample_edition_id: str
    ) -> None:
        """Test que suivre une nouvelle édition crée un nouveau suivi."""
        usecase = FollowEditionV1UseCase(repository)

        result = usecase(sample_edition_id, True)

        all_follows = repository.get_all()
        assert len(all_follows) == 1
        assert all_follows[0].id == result.id

    def test_follow_edition_returns_follow_edition(
        self, repository: InMemoryFollowEditionRepository, sample_edition_id: str
    ) -> None:
        """Test que le use case retourne bien un FollowEdition."""
        usecase = FollowEditionV1UseCase(repository)

        result = usecase(sample_edition_id, True)

        assert isinstance(result, FollowEdition)
        assert hasattr(result, "id")
        assert hasattr(result, "user_id")
        assert hasattr(result, "edition_id")
        assert hasattr(result, "following")
        assert hasattr(result, "created_at")
        assert hasattr(result, "updated_at")

    def test_follow_edition_update_existing(
        self, repository: InMemoryFollowEditionRepository, sample_edition_id: str
    ) -> None:
        """Test de mise à jour d'un suivi existant."""
        usecase = FollowEditionV1UseCase(repository)

        first_result = usecase(sample_edition_id, True)
        second_result = usecase(sample_edition_id, False)

        assert first_result.id == second_result.id
        assert first_result.following is True
        assert second_result.following is False
        assert second_result.updated_at >= first_result.updated_at


class TestUnfollowEditionV1UseCase:
    """Tests pour UnfollowEditionV1UseCase."""

    def test_unfollow_edition_success(
        self, repository: InMemoryFollowEditionRepository, sample_edition_id: str
    ) -> None:
        """Test de suppression d'un suivi d'édition."""
        follow_usecase = FollowEditionV1UseCase(repository)
        follow_result = follow_usecase(sample_edition_id, True)

        unfollow_usecase = UnfollowEditionV1UseCase(repository)
        result = unfollow_usecase(follow_result.id)

        assert result is True
        all_follows = repository.get_all()
        assert len(all_follows) == 0

    def test_unfollow_nonexistent_edition(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test de suppression d'un suivi inexistant."""
        usecase = UnfollowEditionV1UseCase(repository)

        with pytest.raises(FollowEditionNotFoundException) as exc_info:
            usecase("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
