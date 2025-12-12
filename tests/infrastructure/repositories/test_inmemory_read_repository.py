"""Tests for InMemoryReadRepository."""

from datetime import datetime, timezone

import pytest

from mangacollec.domain.entities import Read, ReadEdition
from mangacollec.infrastructure.repositories import InMemoryReadRepository


class TestInMemoryReadRepository:
    """Tests for InMemoryReadRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryReadRepository:
        """Create a fresh InMemoryReadRepository for each test."""
        return InMemoryReadRepository()

    def test_create_reads_multiple_v1_single(self, repository: InMemoryReadRepository) -> None:
        """Test creating a single read."""
        volume_ids = ["volume_123"]

        response = repository.create_reads_multiple_v1(volume_ids)

        assert len(response.reads) == 1
        assert len(response.read_editions) == 1
        assert response.reads[0].volume_id == "volume_123"
        assert response.reads[0].user_id == "test_user"
        assert response.read_editions[0].reading is True
        assert response.read_editions[0].user_id == "test_user"

    def test_create_reads_multiple_v1_multiple(self, repository: InMemoryReadRepository) -> None:
        """Test creating multiple reads."""
        volume_ids = ["volume_1", "volume_2", "volume_3"]

        response = repository.create_reads_multiple_v1(volume_ids)

        assert len(response.reads) == 3
        assert len(response.read_editions) == 3
        assert response.reads[0].volume_id == "volume_1"
        assert response.reads[1].volume_id == "volume_2"
        assert response.reads[2].volume_id == "volume_3"

    def test_create_reads_multiple_v1_empty(self, repository: InMemoryReadRepository) -> None:
        """Test creating reads with empty list."""
        volume_ids: list[str] = []

        response = repository.create_reads_multiple_v1(volume_ids)

        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_create_reads_increments_ids(self, repository: InMemoryReadRepository) -> None:
        """Test that read IDs are incremented correctly."""
        volume_ids = ["volume_1", "volume_2"]

        response = repository.create_reads_multiple_v1(volume_ids)

        assert response.reads[0].id == "1"
        assert response.reads[1].id == "2"
        assert response.read_editions[0].id == "1"
        assert response.read_editions[1].id == "2"

    def test_delete_reads_multiple_v1_existing(self, repository: InMemoryReadRepository) -> None:
        """Test deleting an existing read."""
        # Create first
        create_response = repository.create_reads_multiple_v1(["volume_1"])
        read_id = create_response.reads[0].id

        # Delete
        response = repository.delete_reads_multiple_v1([read_id])

        assert len(response.reads) == 1
        assert len(response.read_editions) == 1
        assert response.reads[0].id == read_id
        assert response.reads[0].deleted is True
        assert response.read_editions[0].deleted is True

    def test_delete_reads_multiple_v1_nonexistent(self, repository: InMemoryReadRepository) -> None:
        """Test deleting a non-existent read."""
        read_ids = ["nonexistent_id"]

        response = repository.delete_reads_multiple_v1(read_ids)

        assert len(response.reads) == 1
        assert response.reads[0].id == "nonexistent_id"
        assert response.reads[0].deleted is False

    def test_delete_reads_multiple_v1_multiple(self, repository: InMemoryReadRepository) -> None:
        """Test deleting multiple reads."""
        # Create first
        create_response = repository.create_reads_multiple_v1(["volume_1", "volume_2", "volume_3"])
        read_ids = [read.id for read in create_response.reads]

        # Delete
        response = repository.delete_reads_multiple_v1(read_ids)

        assert len(response.reads) == 3
        assert all(read.deleted for read in response.reads)
        assert len(response.read_editions) == 3
        assert all(edition.deleted for edition in response.read_editions)

    def test_add_read(self, repository: InMemoryReadRepository) -> None:
        """Test adding a read directly (helper method for tests)."""
        read = Read(
            id="read_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=datetime.now(timezone.utc),
        )

        result = repository.add_read(read)

        assert result == read
        assert repository._reads["read_123"] == read

    def test_add_read_edition(self, repository: InMemoryReadRepository) -> None:
        """Test adding a read edition directly (helper method for tests)."""
        read_edition = ReadEdition(
            id="read_edition_123",
            edition_id="edition_456",
            user_id="user_789",
            reading=True,
            created_at=datetime.now(timezone.utc),
        )

        result = repository.add_read_edition(read_edition)

        assert result == read_edition
        assert repository._read_editions["read_edition_123"] == read_edition

    def test_clear(self, repository: InMemoryReadRepository) -> None:
        """Test clearing the repository."""
        # Add some data
        repository.create_reads_multiple_v1(["volume_1", "volume_2"])

        # Clear
        repository.clear()

        assert len(repository._reads) == 0
        assert len(repository._read_editions) == 0
        assert repository._next_read_id == 1
        assert repository._next_read_edition_id == 1

    def test_clear_and_recreate(self, repository: InMemoryReadRepository) -> None:
        """Test that IDs restart from 1 after clear."""
        # Create, clear, create again
        repository.create_reads_multiple_v1(["volume_1"])
        repository.clear()
        response = repository.create_reads_multiple_v1(["volume_2"])

        # IDs should start from 1 again
        assert response.reads[0].id == "1"
        assert response.read_editions[0].id == "1"
