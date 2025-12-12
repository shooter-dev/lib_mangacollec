"""Tests pour InMemoryUserRepository.

This module contains unit tests for the InMemory User repository.
"""

import pytest

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.domain.exceptions import UserNotFoundException
from mangacollec.infrastructure.repositories import InMemoryUserRepository


class TestInMemoryUserRepository:
    """Tests pour InMemoryUserRepository."""

    @pytest.fixture
    def repo(self) -> InMemoryUserRepository:
        """Fixture pour le repository."""
        return InMemoryUserRepository()

    # Tests pour get_user_collection_by_username_v2
    def test_get_user_collection_by_username_default_user(self, repo: InMemoryUserRepository) -> None:
        """Test de récupération de collection pour l'utilisateur par défaut."""
        result = repo.get_user_collection_by_username_v2("shooterdev")

        assert isinstance(result, GetUserCollectionByUsernameV2Response)
        assert len(result.editions) > 0
        assert len(result.series) > 0

    def test_get_user_collection_by_username_not_found(self, repo: InMemoryUserRepository) -> None:
        """Test de récupération de collection pour un utilisateur inexistant."""
        with pytest.raises(UserNotFoundException):
            repo.get_user_collection_by_username_v2("nonexistent-user")

    def test_get_user_collection_by_username_added_collection(self, repo: InMemoryUserRepository) -> None:
        """Test de récupération de collection pour un utilisateur ajouté."""
        collection_data = {
            "editions": [
                {
                    "id": "ed-1",
                    "title": "Test Edition",
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
                    "title": "Test Series",
                    "type_id": "t-1",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 0,
                }
            ],
        }

        repo.add_user_collection("testuser", collection_data)
        result = repo.get_user_collection_by_username_v2("testuser")

        assert isinstance(result, GetUserCollectionByUsernameV2Response)
        assert len(result.editions) == 1
        assert len(result.series) == 1
        assert result.editions[0].title == "Test Edition"
        assert result.series[0].title == "Test Series"

    # Tests pour get_me_collection_v2
    def test_get_me_collection_success(self, repo: InMemoryUserRepository) -> None:
        """Test de récupération de la collection de l'utilisateur authentifié."""
        result = repo.get_me_collection_v2()

        assert isinstance(result, GetMeCollectionV2Response)
        assert result.user_collection is not None
        assert len(result.editions) > 0

    def test_get_me_collection_none_raises_exception(self, repo: InMemoryUserRepository) -> None:
        """Test que None pour me_collection lève une exception."""
        repo._me_collection = None

        with pytest.raises(UserNotFoundException):
            repo.get_me_collection_v2()

    def test_set_and_get_me_collection(self, repo: InMemoryUserRepository) -> None:
        """Test de mise à jour et récupération de la collection personnelle."""
        new_collection = {
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

        repo._me_collection = new_collection
        result = repo.get_me_collection_v2()

        assert isinstance(result, GetMeCollectionV2Response)
        assert len(result.editions) == 1
        assert result.editions[0].title == "My Edition"

    # Tests pour get_me_recommendations_v1
    def test_get_me_recommendations_success(self, repo: InMemoryUserRepository) -> None:
        """Test de récupération des recommandations personnelles."""
        result = repo.get_me_recommendations_v1()

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert len(result.volumes) > 0

    def test_get_me_recommendations_none_raises_exception(self, repo: InMemoryUserRepository) -> None:
        """Test que None pour recommendations lève une exception."""
        repo._me_recommendations = None

        with pytest.raises(UserNotFoundException):
            repo.get_me_recommendations_v1()

    def test_set_and_get_me_recommendations(self, repo: InMemoryUserRepository) -> None:
        """Test de mise à jour et récupération des recommandations."""
        new_recommendations = [
            {
                "id": "vol-rec-1",
                "title": "Recommended Volume 1",
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

        repo.set_me_recommendations(new_recommendations)
        result = repo.get_me_recommendations_v1()

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].title == "Recommended Volume 1"

    # Tests pour les méthodes helper
    def test_add_user_collection_and_clear(self, repo: InMemoryUserRepository) -> None:
        """Test l'ajout et le nettoyage de collections utilisateur."""
        collection_data = {
            "editions": [],
            "series": [],
        }

        repo.add_user_collection("temp_user", collection_data)
        result = repo.get_user_collection_by_username_v2("temp_user")

        assert isinstance(result, GetUserCollectionByUsernameV2Response)

        repo.clear_data()

        with pytest.raises(UserNotFoundException):
            repo.get_user_collection_by_username_v2("temp_user")

    def test_set_me_recommendations_empty(self, repo: InMemoryUserRepository) -> None:
        """Test de mise à jour avec une liste vide de recommandations."""
        repo.set_me_recommendations([])
        result = repo.get_me_recommendations_v1()

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert result.volumes == []
