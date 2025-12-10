"""Tests pour le FollowEditionMapper.

This module contains unit tests for the FollowEditionMapper.
"""

from datetime import datetime, timezone

from mangacollec.application.dto import FollowEditionV1Response
from mangacollec.application.mappers import FollowEditionMapper
from mangacollec.domain.entities import FollowEdition


class TestFollowEditionMapper:
    """Tests pour le mapper FollowEdition."""

    def test_from_dict(self) -> None:
        """Test de conversion d'un dictionnaire en FollowEdition."""
        data = {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "user_id": "user-123",
            "edition_id": "edition-456",
            "following": True,
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-02T12:00:00Z",
        }

        follow_edition = FollowEditionMapper.from_dict(data)

        assert isinstance(follow_edition, FollowEdition)
        assert follow_edition.id == "550e8400-e29b-41d4-a716-446655440000"
        assert follow_edition.user_id == "user-123"
        assert follow_edition.edition_id == "edition-456"
        assert follow_edition.following is True
        assert follow_edition.created_at == datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        assert follow_edition.updated_at == datetime(2024, 1, 2, 12, 0, 0, tzinfo=timezone.utc)

    def test_from_dict_with_following_false(self) -> None:
        """Test de conversion avec following=False."""
        data = {
            "id": "550e8400-e29b-41d4-a716-446655440001",
            "user_id": "user-789",
            "edition_id": "edition-012",
            "following": False,
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-01T12:00:00Z",
        }

        follow_edition = FollowEditionMapper.from_dict(data)

        assert follow_edition.following is False
        assert follow_edition.created_at == follow_edition.updated_at

    def test_to_dict(self) -> None:
        """Test de conversion d'un FollowEdition en dictionnaire."""
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

        result = FollowEditionMapper.to_dict(follow_edition)

        assert result == {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "user_id": "user-123",
            "edition_id": "edition-456",
            "following": True,
            "created_at": created_at.isoformat(),
            "updated_at": updated_at.isoformat(),
        }

    def test_to_dict_preserves_all_fields(self) -> None:
        """Test que to_dict préserve tous les champs."""
        created_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        updated_at = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

        follow_edition = FollowEdition(
            id="test-id",
            user_id="test-user",
            edition_id="test-edition",
            following=False,
            created_at=created_at,
            updated_at=updated_at,
        )

        result = FollowEditionMapper.to_dict(follow_edition)

        assert result["id"] == "test-id"
        assert result["user_id"] == "test-user"
        assert result["edition_id"] == "test-edition"
        assert result["following"] is False
        assert "created_at" in result
        assert "updated_at" in result

    def test_from_api_response(self) -> None:
        """Test de conversion de la réponse API en FollowEditionV1Response."""
        response = {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "user_id": "user-123",
            "edition_id": "edition-456",
            "following": True,
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-02T12:00:00Z",
        }

        result = FollowEditionMapper.from_api_response(response)

        assert isinstance(result, FollowEditionV1Response)
        assert isinstance(result.follow_edition, FollowEdition)
        assert result.follow_edition.id == "550e8400-e29b-41d4-a716-446655440000"
        assert result.follow_edition.user_id == "user-123"
        assert result.follow_edition.edition_id == "edition-456"
        assert result.follow_edition.following is True

    def test_from_api_response_with_following_false(self) -> None:
        """Test de conversion API avec following=False."""
        response = {
            "id": "550e8400-e29b-41d4-a716-446655440001",
            "user_id": "user-789",
            "edition_id": "edition-012",
            "following": False,
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-01T12:00:00Z",
        }

        result = FollowEditionMapper.from_api_response(response)

        assert result.follow_edition.following is False
