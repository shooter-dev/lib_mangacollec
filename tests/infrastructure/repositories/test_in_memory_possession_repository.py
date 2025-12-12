"""Tests for InMemoryPossessionRepository."""

import pytest

from mangacollec.infrastructure.repositories import InMemoryPossessionRepository


class TestInMemoryPossessionRepository:
    """Tests for InMemoryPossessionRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryPossessionRepository:
        """Create a fresh InMemoryPossessionRepository for each test."""
        return InMemoryPossessionRepository()

    def test_add_possessions_multiple_v1_single(self, repository: InMemoryPossessionRepository) -> None:
        """Test adding a single possession."""
        volume_ids = ["volume_123"]

        response = repository.add_possessions_multiple_v1(volume_ids)

        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        assert response.possessions[0].volume_id == "volume_123"
        assert response.possessions[0].user_id == "user-test"
        assert response.follow_editions[0].following is True
        assert response.follow_editions[0].user_id == "user-test"

    def test_add_possessions_multiple_v1_multiple(self, repository: InMemoryPossessionRepository) -> None:
        """Test adding multiple possessions."""
        volume_ids = ["volume_1", "volume_2", "volume_3"]

        response = repository.add_possessions_multiple_v1(volume_ids)

        assert len(response.possessions) == 3
        assert len(response.follow_editions) == 3
        assert response.possessions[0].volume_id == "volume_1"
        assert response.possessions[1].volume_id == "volume_2"
        assert response.possessions[2].volume_id == "volume_3"

    def test_add_possessions_multiple_v1_empty(self, repository: InMemoryPossessionRepository) -> None:
        """Test adding possessions with empty list."""
        volume_ids: list[str] = []

        response = repository.add_possessions_multiple_v1(volume_ids)

        assert len(response.possessions) == 0
        assert len(response.follow_editions) == 0

    def test_delete_possessions_multiple_v1_existing(self, repository: InMemoryPossessionRepository) -> None:
        """Test deleting an existing possession."""
        # Add first
        add_response = repository.add_possessions_multiple_v1(["volume_1"])
        possession_id = add_response.possessions[0].id

        # Delete
        response = repository.delete_possessions_multiple_v1([possession_id])

        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        assert response.possessions[0].id == possession_id
        assert response.possessions[0].deleted is True
        assert response.follow_editions[0].deleted is True

    def test_delete_possessions_multiple_v1_nonexistent(self, repository: InMemoryPossessionRepository) -> None:
        """Test deleting a non-existent possession."""
        response = repository.delete_possessions_multiple_v1(["nonexistent_id"])

        assert len(response.possessions) == 0
        assert len(response.follow_editions) == 0
        assert len(response.loans) == 0

    def test_delete_possessions_multiple_v1_multiple(self, repository: InMemoryPossessionRepository) -> None:
        """Test deleting multiple possessions."""
        # Add first
        add_response = repository.add_possessions_multiple_v1(["volume_1", "volume_2"])
        possession_id_1 = add_response.possessions[0].id
        possession_id_2 = add_response.possessions[1].id

        # Delete
        response = repository.delete_possessions_multiple_v1([possession_id_1, possession_id_2])

        assert len(response.possessions) == 2
        assert len(response.follow_editions) == 2
        assert response.possessions[0].deleted is True
        assert response.possessions[1].deleted is True

    def test_delete_possessions_multiple_v1_with_loans(self, repository: InMemoryPossessionRepository) -> None:
        """Test deleting possessions with associated loans."""
        # Add possession and simulate loan
        add_response = repository.add_possessions_multiple_v1(["volume_1"])
        possession_id = add_response.possessions[0].id

        # Simulate a loan (add to internal loans dict)
        repository._loans[possession_id] = {"loan_data": "test"}

        # Delete
        response = repository.delete_possessions_multiple_v1([possession_id])

        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        assert len(response.loans) == 1
        assert response.loans[0].deleted is True
