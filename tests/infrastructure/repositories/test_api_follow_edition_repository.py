"""Tests pour APIFollowEditionRepository.

This module contains unit tests for the API FollowEdition repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.exceptions import (
    FollowEditionNotFoundException,
    FollowEditionOperationException,
)
from mangacollec.infrastructure.repositories import APIFollowEditionRepository


class TestAPIFollowEditionRepository:
    """Tests pour APIFollowEditionRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIFollowEditionRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIFollowEditionRepository(mock_api_client)

    @pytest.fixture
    def sample_follow_edition_data(self) -> dict:
        """Fixture pour créer des données de suivi d'édition de test."""
        return {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "user_id": "user-123",
            "edition_id": "edition-456",
            "following": True,
            "created_at": "2024-01-01T12:00:00Z",
            "updated_at": "2024-01-02T12:00:00Z",
        }

    def test_follow_edition_v1_success(
        self,
        repository: APIFollowEditionRepository,
        mock_api_client: Mock,
        sample_follow_edition_data: dict,
    ) -> None:
        """Test de suivi d'une édition avec succès."""
        mock_api_client.post.return_value = sample_follow_edition_data

        result = repository.follow_edition_v1("edition-456", True)

        assert isinstance(result, FollowEdition)
        assert result.id == "550e8400-e29b-41d4-a716-446655440000"
        assert result.edition_id == "edition-456"
        assert result.following is True

        mock_api_client.post.assert_called_once_with(
            "/v1/follow-editions", data={"edition_id": "edition-456", "following": True}
        )

    def test_follow_edition_v1_unfollow(
        self,
        repository: APIFollowEditionRepository,
        mock_api_client: Mock,
        sample_follow_edition_data: dict,
    ) -> None:
        """Test d'arrêt de suivi d'une édition."""
        unfollow_data = {**sample_follow_edition_data, "following": False}
        mock_api_client.post.return_value = unfollow_data

        result = repository.follow_edition_v1("edition-456", False)

        assert isinstance(result, FollowEdition)
        assert result.following is False

        mock_api_client.post.assert_called_once_with(
            "/v1/follow-editions", data={"edition_id": "edition-456", "following": False}
        )

    def test_follow_edition_v1_api_exception(
        self, repository: APIFollowEditionRepository, mock_api_client: Mock
    ) -> None:
        """Test de gestion d'erreur lors du suivi d'une édition."""
        mock_api_client.post.side_effect = Exception("API Error")

        with pytest.raises(FollowEditionOperationException) as exc_info:
            repository.follow_edition_v1("edition-456", True)

        assert "edition-456" in str(exc_info.value)
        assert "Failed to follow/unfollow" in str(exc_info.value)

    def test_unfollow_edition_v1_success(self, repository: APIFollowEditionRepository, mock_api_client: Mock) -> None:
        """Test de suppression d'un suivi d'édition avec succès."""
        mock_api_client.delete.return_value = {}

        result = repository.unfollow_edition_v1("550e8400-e29b-41d4-a716-446655440000")

        assert result is True
        mock_api_client.delete.assert_called_once_with("/v1/follow-editions/550e8400-e29b-41d4-a716-446655440000")

    def test_unfollow_edition_v1_not_found(self, repository: APIFollowEditionRepository, mock_api_client: Mock) -> None:
        """Test de suppression d'un suivi d'édition inexistant."""
        mock_api_client.delete.side_effect = Exception("404 Not Found")

        with pytest.raises(FollowEditionNotFoundException) as exc_info:
            repository.unfollow_edition_v1("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_unfollow_edition_v1_api_exception(
        self, repository: APIFollowEditionRepository, mock_api_client: Mock
    ) -> None:
        """Test de gestion d'erreur lors de la suppression d'un suivi."""
        mock_api_client.delete.side_effect = Exception("500 Internal Server Error")

        with pytest.raises(FollowEditionOperationException) as exc_info:
            repository.unfollow_edition_v1("550e8400-e29b-41d4-a716-446655440000")

        assert "550e8400-e29b-41d4-a716-446655440000" in str(exc_info.value)
        assert "Failed to delete follow edition" in str(exc_info.value)
