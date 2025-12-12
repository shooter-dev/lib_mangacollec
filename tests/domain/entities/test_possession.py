"""Tests for Possession entities."""

from datetime import datetime, timezone

import pytest

from mangacollec.domain.entities import (
    FollowEditionDeleted,
    LoanDeleted,
    Possession,
    PossessionDeleted,
)


class TestPossessionEntity:
    """Tests for Possession entity."""

    def test_possession_creation(self) -> None:
        """Test creating a Possession entity."""
        created_at = datetime.now(timezone.utc)
        possession = Possession(
            id="possession_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=created_at,
        )

        assert possession.id == "possession_123"
        assert possession.user_id == "user_456"
        assert possession.volume_id == "volume_789"
        assert possession.created_at == created_at

    def test_possession_is_frozen(self) -> None:
        """Test that Possession entity is immutable."""
        possession = Possession(
            id="possession_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=datetime.now(timezone.utc),
        )

        with pytest.raises(AttributeError):
            possession.id = "new_id"  # type: ignore


class TestPossessionDeletedEntity:
    """Tests for PossessionDeleted entity."""

    def test_possession_deleted_creation(self) -> None:
        """Test creating a PossessionDeleted entity."""
        possession_deleted = PossessionDeleted(
            id="possession_123",
            deleted=True,
        )

        assert possession_deleted.id == "possession_123"
        assert possession_deleted.deleted is True

    def test_possession_deleted_is_frozen(self) -> None:
        """Test that PossessionDeleted entity is immutable."""
        possession_deleted = PossessionDeleted(
            id="possession_123",
            deleted=True,
        )

        with pytest.raises(AttributeError):
            possession_deleted.id = "new_id"  # type: ignore


class TestFollowEditionDeletedEntity:
    """Tests for FollowEditionDeleted entity."""

    def test_follow_edition_deleted_creation(self) -> None:
        """Test creating a FollowEditionDeleted entity."""
        follow_edition_deleted = FollowEditionDeleted(
            id="follow_edition_123",
            deleted=True,
        )

        assert follow_edition_deleted.id == "follow_edition_123"
        assert follow_edition_deleted.deleted is True

    def test_follow_edition_deleted_is_frozen(self) -> None:
        """Test that FollowEditionDeleted entity is immutable."""
        follow_edition_deleted = FollowEditionDeleted(
            id="follow_edition_123",
            deleted=True,
        )

        with pytest.raises(AttributeError):
            follow_edition_deleted.id = "new_id"  # type: ignore


class TestLoanDeletedEntity:
    """Tests for LoanDeleted entity."""

    def test_loan_deleted_creation(self) -> None:
        """Test creating a LoanDeleted entity."""
        loan_deleted = LoanDeleted(
            id="loan_123",
            deleted=True,
        )

        assert loan_deleted.id == "loan_123"
        assert loan_deleted.deleted is True

    def test_loan_deleted_is_frozen(self) -> None:
        """Test that LoanDeleted entity is immutable."""
        loan_deleted = LoanDeleted(
            id="loan_123",
            deleted=True,
        )

        with pytest.raises(AttributeError):
            loan_deleted.id = "new_id"  # type: ignore
