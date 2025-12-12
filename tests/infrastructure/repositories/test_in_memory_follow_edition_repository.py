"""Tests for InMemoryFollowEditionRepository."""

from datetime import datetime, timezone

import pytest

from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.exceptions import FollowEditionNotFoundException
from mangacollec.infrastructure.repositories import \
    InMemoryFollowEditionRepository


class TestInMemoryFollowEditionRepository:
    """Tests for InMemoryFollowEditionRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryFollowEditionRepository:
        """Fixture to create an in-memory repository."""
        return InMemoryFollowEditionRepository()

    @pytest.fixture
    def sample_follow_edition(self) -> FollowEdition:
        """Fixture to create a test follow edition."""
        return FollowEdition(
            id="550e8400-e29b-41d4-a716-446655440000",
            user_id="test-user-id",
            edition_id="edition-456",
            following=True,
            created_at=datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
            updated_at=datetime(2024, 1, 2, 12, 0, 0, tzinfo=timezone.utc),
        )

    def test_follow_edition_v1_create_new(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test creating a new follow edition."""
        result = repository.follow_edition_v1("edition-123", True)

        assert isinstance(result, FollowEdition)
        assert result.edition_id == "edition-123"
        assert result.following is True
        assert result.user_id == "test-user-id"
        assert result.id is not None
        assert len(repository.get_all()) == 1

    def test_follow_edition_v1_update_existing(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test updating an existing follow edition."""
        first_result = repository.follow_edition_v1("edition-123", True)
        second_result = repository.follow_edition_v1("edition-123", False)

        assert first_result.id == second_result.id
        assert first_result.following is True
        assert second_result.following is False
        assert second_result.updated_at >= first_result.updated_at
        assert len(repository.get_all()) == 1

    def test_follow_edition_v1_different_editions(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test creating follow editions for different editions."""
        result1 = repository.follow_edition_v1("edition-123", True)
        result2 = repository.follow_edition_v1("edition-456", True)

        assert result1.id != result2.id
        assert result1.edition_id != result2.edition_id
        assert len(repository.get_all()) == 2

    def test_unfollow_edition_v1_success(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test successfully unfollowing an edition."""
        follow_result = repository.follow_edition_v1("edition-123", True)

        result = repository.unfollow_edition_v1(follow_result.id)

        assert result is True
        assert len(repository.get_all()) == 0

    def test_unfollow_edition_v1_not_found(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test unfollowing a non-existent follow edition."""
        with pytest.raises(FollowEditionNotFoundException) as exc_info:
            repository.unfollow_edition_v1("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_by_id_success(
        self, repository: InMemoryFollowEditionRepository, sample_follow_edition: FollowEdition
    ) -> None:
        """Test retrieving a follow edition by ID."""
        repository._data[sample_follow_edition.id] = sample_follow_edition

        result = repository.get_by_id(sample_follow_edition.id)

        assert result is not None
        assert isinstance(result, FollowEdition)
        assert result.id == sample_follow_edition.id
        assert result.edition_id == sample_follow_edition.edition_id

    def test_get_by_id_not_found(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test retrieving a non-existent follow edition."""
        result = repository.get_by_id("nonexistent-id")

        assert result is None

    def test_get_all(self, repository: InMemoryFollowEditionRepository, sample_follow_edition: FollowEdition) -> None:
        """Test retrieving all follow editions."""
        repository._data[sample_follow_edition.id] = sample_follow_edition

        result = repository.get_all()

        assert len(result) == 1
        assert result[0].id == sample_follow_edition.id

    def test_get_all_empty(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test retrieving all follow editions from empty repository."""
        result = repository.get_all()

        assert len(result) == 0
        assert isinstance(result, list)

    def test_clear(self, repository: InMemoryFollowEditionRepository) -> None:
        """Test clearing the repository."""
        repository.follow_edition_v1("edition-123", True)
        repository.follow_edition_v1("edition-456", True)

        assert len(repository.get_all()) == 2

        repository.clear()

        assert len(repository.get_all()) == 0
