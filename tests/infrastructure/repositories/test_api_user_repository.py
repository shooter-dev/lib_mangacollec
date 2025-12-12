"""Tests pour APIUserRepository.

This module contains unit tests for the API User repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.exceptions import UserNotFoundException
from mangacollec.infrastructure.repositories import APIUserRepository


class TestAPIUserRepository:
    """Tests pour APIUserRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIUserRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIUserRepository(mock_api_client)

    # Tests pour get_user_collection_by_username_v2
    def test_get_user_collection_by_username_success(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test de récupération réussie de collection utilisateur."""
        mock_api_client.get.return_value = {
            "editions": [
                {
                    "id": "ed-1",
                    "title": "Edition 1",
                    "series_id": "s-1",
                    "publisher_id": "p-1",
                    "parent_edition_id": None,
                    "volumes_count": 10,
                    "last_volume_number": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 100,
                }
            ],
            "series": [
                {
                    "id": "s-1",
                    "title": "Series 1",
                    "type_id": "t-1",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 0,
                }
            ],
        }

        result = repository.get_user_collection_by_username_v2("testuser")

        assert isinstance(result, GetUserCollectionByUsernameV2Response)
        assert len(result.editions) == 1
        assert len(result.series) == 1
        assert result.editions[0].title == "Edition 1"
        mock_api_client.get.assert_called_once_with("/v2/user/testuser/collection")

    def test_get_user_collection_by_username_not_found(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test quand la collection utilisateur n'existe pas."""
        mock_api_client.get.return_value = {
            "editions": [],
            "series": [],
        }

        with pytest.raises(UserNotFoundException):
            repository.get_user_collection_by_username_v2("nonexistent")

    def test_get_user_collection_by_username_api_error(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test en cas d'erreur API."""
        mock_api_client.get.side_effect = RuntimeError("API Error")

        with pytest.raises(UserNotFoundException):
            repository.get_user_collection_by_username_v2("testuser")

    # Tests pour get_me_collection_v2
    def test_get_me_collection_success(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test de récupération réussie de la collection personnelle."""
        mock_api_client.get.return_value = {
            "editions": [
                {
                    "id": "ed-me-1",
                    "title": "My Edition",
                    "series_id": "s-me-1",
                    "publisher_id": "p-me-1",
                    "parent_edition_id": None,
                    "volumes_count": 5,
                    "last_volume_number": 5,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            "series": [
                {
                    "id": "s-me-1",
                    "title": "My Series",
                    "type_id": "t-me-1",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 0,
                }
            ],
        }

        result = repository.get_me_collection_v2()

        assert isinstance(result, GetMeCollectionV2Response)
        assert result.user_collection is not None
        assert len(result.editions) == 1
        mock_api_client.get.assert_called_once_with("/v2/users/me/collection")

    def test_get_me_collection_api_error(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test en cas d'erreur API pour me_collection."""
        mock_api_client.get.side_effect = RuntimeError("API Error")

        with pytest.raises(RuntimeError):
            repository.get_me_collection_v2()

    # Tests pour get_me_recommendations_v1
    def test_get_me_recommendations_success(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test de récupération réussie des recommandations."""
        mock_api_client.get.return_value = [
            {
                "id": "vol-rec-1",
                "title": "Recommended Volume",
                "number": 1,
                "release_date": "2025-12-01",
                "isbn": "9791032724743",
                "asin": "B0FC1DWL9R",
                "edition_id": "ed-rec-1",
                "possessions_count": 100,
                "not_sold": False,
                "image_url": "https://example.com/rec1.jpg",
                "nb_pages": 192,
                "content": None,
            }
        ]

        result = repository.get_me_recommendations_v1()

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert len(result.volumes) == 1
        mock_api_client.get.assert_called_once_with("/v1/users/me/recommendation")

    def test_get_me_recommendations_empty(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test récupération d'une liste vide de recommandations."""
        mock_api_client.get.return_value = []

        result = repository.get_me_recommendations_v1()

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert result.volumes == []

    def test_get_me_recommendations_api_error(
        self,
        repository: APIUserRepository,
        mock_api_client: Mock,
    ) -> None:
        """Test en cas d'erreur API pour les recommandations."""
        mock_api_client.get.side_effect = RuntimeError("API Error")

        with pytest.raises(RuntimeError):
            repository.get_me_recommendations_v1()
