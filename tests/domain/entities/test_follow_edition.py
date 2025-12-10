"""Tests pour l'entité FollowEdition.

This module contains unit tests for FollowEdition entity.
"""

from datetime import datetime, timezone

import pytest

from mangacollec.domain.entities import FollowEdition


class TestFollowEdition:
    """Tests pour l'entité FollowEdition."""

    def test_create_follow_edition_with_all_fields(self) -> None:
        """Test de création d'un suivi d'édition avec tous les champs."""
        created_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        updated_at = datetime(2024, 1, 2, 12, 0, 0, tzinfo=timezone.utc)

        follow_edition = FollowEdition(
            id="550e8400-e29b-41d4-a716-446655440000",
            user_id="user-123",
            edition_id="edition-456",
            following=True,
            created_at=created_at,
            updated_at=updated_at,
        )

        assert follow_edition.id == "550e8400-e29b-41d4-a716-446655440000"
        assert follow_edition.user_id == "user-123"
        assert follow_edition.edition_id == "edition-456"
        assert follow_edition.following is True
        assert follow_edition.created_at == created_at
        assert follow_edition.updated_at == updated_at

    def test_create_follow_edition_following_false(self) -> None:
        """Test de création d'un suivi d'édition avec following=False."""
        created_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        updated_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

        follow_edition = FollowEdition(
            id="550e8400-e29b-41d4-a716-446655440001",
            user_id="user-789",
            edition_id="edition-012",
            following=False,
            created_at=created_at,
            updated_at=updated_at,
        )

        assert follow_edition.id == "550e8400-e29b-41d4-a716-446655440001"
        assert follow_edition.following is False

    def test_follow_edition_is_frozen(self) -> None:
        """Test que l'entité FollowEdition est immuable."""
        follow_edition = FollowEdition(
            id="test-id",
            user_id="test-user",
            edition_id="test-edition",
            following=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        with pytest.raises(AttributeError):
            follow_edition.following = False
