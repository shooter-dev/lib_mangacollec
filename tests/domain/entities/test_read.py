"""Tests for Read entities."""

from datetime import datetime, timezone

import pytest

from mangacollec.domain.entities import (Read, ReadDeleted, ReadEdition,
                                         ReadEditionDeleted)


class TestReadEntity:
    """Tests for Read entity."""

    def test_read_creation(self) -> None:
        """Test creating a Read entity."""
        created_at = datetime.now(timezone.utc)
        read = Read(
            id="read_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=created_at,
        )

        assert read.id == "read_123"
        assert read.user_id == "user_456"
        assert read.volume_id == "volume_789"
        assert read.created_at == created_at

    def test_read_is_frozen(self) -> None:
        """Test that Read entity is immutable."""
        read = Read(
            id="read_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=datetime.now(timezone.utc),
        )

        with pytest.raises(AttributeError):
            read.id = "new_id"  # type: ignore


class TestReadEditionEntity:
    """Tests for ReadEdition entity."""

    def test_read_edition_creation(self) -> None:
        """Test creating a ReadEdition entity."""
        created_at = datetime.now(timezone.utc)
        read_edition = ReadEdition(
            id="read_edition_123",
            edition_id="edition_456",
            user_id="user_789",
            reading=True,
            created_at=created_at,
        )

        assert read_edition.id == "read_edition_123"
        assert read_edition.edition_id == "edition_456"
        assert read_edition.user_id == "user_789"
        assert read_edition.reading is True
        assert read_edition.created_at == created_at

    def test_read_edition_not_reading(self) -> None:
        """Test ReadEdition with reading=False."""
        read_edition = ReadEdition(
            id="read_edition_123",
            edition_id="edition_456",
            user_id="user_789",
            reading=False,
            created_at=datetime.now(timezone.utc),
        )

        assert read_edition.reading is False

    def test_read_edition_is_frozen(self) -> None:
        """Test that ReadEdition entity is immutable."""
        read_edition = ReadEdition(
            id="read_edition_123",
            edition_id="edition_456",
            user_id="user_789",
            reading=True,
            created_at=datetime.now(timezone.utc),
        )

        with pytest.raises(AttributeError):
            read_edition.id = "new_id"  # type: ignore


class TestReadDeletedEntity:
    """Tests for ReadDeleted entity."""

    def test_read_deleted_creation_success(self) -> None:
        """Test creating a ReadDeleted entity with deleted=True."""
        read_deleted = ReadDeleted(id="read_123", deleted=True)

        assert read_deleted.id == "read_123"
        assert read_deleted.deleted is True

    def test_read_deleted_creation_failure(self) -> None:
        """Test creating a ReadDeleted entity with deleted=False."""
        read_deleted = ReadDeleted(id="read_123", deleted=False)

        assert read_deleted.id == "read_123"
        assert read_deleted.deleted is False

    def test_read_deleted_is_frozen(self) -> None:
        """Test that ReadDeleted entity is immutable."""
        read_deleted = ReadDeleted(id="read_123", deleted=True)

        with pytest.raises(AttributeError):
            read_deleted.id = "new_id"  # type: ignore


class TestReadEditionDeletedEntity:
    """Tests for ReadEditionDeleted entity."""

    def test_read_edition_deleted_creation_success(self) -> None:
        """Test creating a ReadEditionDeleted entity with deleted=True."""
        read_edition_deleted = ReadEditionDeleted(id="read_edition_123", deleted=True)

        assert read_edition_deleted.id == "read_edition_123"
        assert read_edition_deleted.deleted is True

    def test_read_edition_deleted_creation_failure(self) -> None:
        """Test creating a ReadEditionDeleted entity with deleted=False."""
        read_edition_deleted = ReadEditionDeleted(id="read_edition_123", deleted=False)

        assert read_edition_deleted.id == "read_edition_123"
        assert read_edition_deleted.deleted is False

    def test_read_edition_deleted_is_frozen(self) -> None:
        """Test that ReadEditionDeleted entity is immutable."""
        read_edition_deleted = ReadEditionDeleted(id="read_edition_123", deleted=True)

        with pytest.raises(AttributeError):
            read_edition_deleted.id = "new_id"  # type: ignore
