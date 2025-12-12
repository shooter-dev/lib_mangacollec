"""Tests pour les use cases User.

This module contains unit tests for User use cases.
"""

import pytest

from mangacollec.application.use_cases import (
    GetMeCollectionV2UseCase, GetMeRecommendationsV1UseCase,
    GetUserCollectionByUsernameV2UseCase)
from mangacollec.domain.exceptions import UserNotFoundException
from mangacollec.infrastructure.repositories import InMemoryUserRepository


@pytest.fixture
def repository() -> InMemoryUserRepository:
    """Fixture pour créer un repository en mémoire."""
    return InMemoryUserRepository()


@pytest.fixture
def sample_editions() -> list[dict]:
    """Fixture pour créer des données d'éditions de test."""
    return [
        {
            "id": "edition-123",
            "title": "Edition Collector",
            "series_id": "series-456",
            "publisher_id": "publisher-789",
            "parent_edition_id": None,
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 1443,
        },
        {
            "id": "edition-456",
            "title": None,
            "series_id": "series-789",
            "publisher_id": "publisher-123",
            "parent_edition_id": None,
            "volumes_count": 50,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 500,
        },
    ]


@pytest.fixture
def sample_series() -> list[dict]:
    """Fixture pour créer des données de séries de test."""
    return [
        {
            "id": "series-456",
            "title": "Naruto",
            "type_id": "type-001",
            "adult_content": False,
            "editions_count": 1,
            "tasks_count": 1,
        },
        {
            "id": "series-789",
            "title": "One Piece",
            "type_id": "type-001",
            "adult_content": False,
            "editions_count": 1,
            "tasks_count": 1,
        },
    ]


@pytest.fixture
def sample_volumes() -> list[dict]:
    """Fixture pour créer des données de volumes de test."""
    return [
        {
            "id": "volume-111",
            "title": "Recommended Volume 1",
            "number": 1,
            "release_date": "2025-12-01",
            "isbn": "9791032724743",
            "asin": "B0FC1DWL9R",
            "edition_id": "edition-111",
            "possessions_count": 59,
            "not_sold": False,
            "image_url": "https://example.com/image1.jpg",
            "nb_pages": 200,
            "content": None,
        },
        {
            "id": "volume-222",
            "title": None,
            "number": 2,
            "release_date": "2025-12-08",
            "isbn": "9791032724744",
            "asin": "B0FC1DWL9S",
            "edition_id": "edition-222",
            "possessions_count": 45,
            "not_sold": False,
            "image_url": "https://example.com/image2.jpg",
            "nb_pages": None,
            "content": None,
        },
    ]


class TestGetUserCollectionByUsernameV2UseCase:
    """Tests pour GetUserCollectionByUsernameV2UseCase."""

    def test_get_user_collection_success(
        self,
        repository: InMemoryUserRepository,
        sample_editions: list[dict],
        sample_series: list[dict],
    ) -> None:
        """Test de récupération de collection utilisateur existante."""
        # Simuler la réponse du repository
        repository._user_collections = {
            "shooterdev": {
                "editions": sample_editions,
                "series": sample_series,
            }
        }

        use_case = GetUserCollectionByUsernameV2UseCase(repository)
        result = use_case("shooterdev")

        assert len(result.editions) == 2
        assert len(result.series) == 2
        assert result.editions[0].title == "Edition Collector"
        assert result.series[0].title == "Naruto"

    def test_get_user_collection_empty(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération de collection utilisateur vide."""
        repository._user_collections = {
            "newuser": {
                "editions": [],
                "series": [],
            }
        }

        use_case = GetUserCollectionByUsernameV2UseCase(repository)
        result = use_case("newuser")

        assert result.editions == []
        assert result.series == []

    def test_get_user_collection_not_found(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération de collection utilisateur inexistante."""
        use_case = GetUserCollectionByUsernameV2UseCase(repository)

        with pytest.raises(UserNotFoundException) as exc_info:
            use_case("nonexistent")

        assert "nonexistent" in str(exc_info.value)


class TestGetMeCollectionV2UseCase:
    """Tests pour GetMeCollectionV2UseCase."""

    def test_get_me_collection_success(
        self,
        repository: InMemoryUserRepository,
        sample_editions: list[dict],
        sample_series: list[dict],
    ) -> None:
        """Test de récupération de sa collection personnelle."""
        repository._me_collection = {
            "editions": sample_editions,
            "series": sample_series,
        }

        use_case = GetMeCollectionV2UseCase(repository)
        result = use_case()

        assert result.user_collection is not None
        assert result.user_collection.total_editions == 2
        assert len(result.editions) == 2
        assert len(result.series) == 2
        assert result.editions[0].title == "Edition Collector"

    def test_get_me_collection_minimal(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération de collection personnelle minimale."""
        repository._me_collection = {
            "editions": [],
            "series": [],
        }

        use_case = GetMeCollectionV2UseCase(repository)
        result = use_case()

        assert result.user_collection is not None
        assert result.user_collection.total_editions == 0
        assert result.editions == []
        assert result.series == []

    def test_get_me_collection_no_collection(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération quand l'utilisateur n'a pas de collection."""
        repository._me_collection = None

        use_case = GetMeCollectionV2UseCase(repository)

        with pytest.raises(UserNotFoundException):
            use_case()


class TestGetMeRecommendationsV1UseCase:
    """Tests pour GetMeRecommendationsV1UseCase."""

    def test_get_me_recommendations_success(
        self,
        repository: InMemoryUserRepository,
        sample_volumes: list[dict],
    ) -> None:
        """Test de récupération des recommandations personnelles."""
        repository._me_recommendations = sample_volumes

        use_case = GetMeRecommendationsV1UseCase(repository)
        result = use_case()

        assert len(result.volumes) == 2
        assert result.volumes[0].title == "Recommended Volume 1"
        assert result.volumes[0].number == 1
        assert result.volumes[0].nb_pages == 200

        assert result.volumes[1].title is None
        assert result.volumes[1].number == 2
        assert result.volumes[1].nb_pages is None

    def test_get_me_recommendations_empty(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération de recommandations vides."""
        repository._me_recommendations = []

        use_case = GetMeRecommendationsV1UseCase(repository)
        result = use_case()

        assert result.volumes == []

    def test_get_me_recommendations_single_volume(
        self,
        repository: InMemoryUserRepository,
    ) -> None:
        """Test de récupération d'une seule recommandation."""
        single_volume = [
            {
                "id": "single-rec",
                "title": "Single Recommendation",
                "number": 1,
                "release_date": "2025-12-12",
                "image_url": "https://example.com/single.jpg",
                "isbn": "9782012345678",
                "asin": "2012345678",
                "edition_id": "edition-single",
                "possessions_count": 100,
                "not_sold": False,
                "nb_pages": 300,
                "content": None,
            }
        ]

        repository._me_recommendations = single_volume

        use_case = GetMeRecommendationsV1UseCase(repository)
        result = use_case()

        assert len(result.volumes) == 1
        assert result.volumes[0].title == "Single Recommendation"
        assert result.volumes[0].nb_pages == 300

    def test_get_me_recommendations_no_recommendations(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération quand il n'y a pas de recommandations."""
        repository._me_recommendations = None

        use_case = GetMeRecommendationsV1UseCase(repository)

        with pytest.raises(UserNotFoundException):
            use_case()

    def test_get_me_recommendations_large_list(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération d'une grande liste de recommandations."""
        # Créer 50 volumes recommandés
        recommendations = []
        for i in range(50):
            volume = {
                "id": f"rec-volume-{i}",
                "title": f"Recommendation {i}",
                "number": i + 1,
                "release_date": "2025-12-01",
                "image_url": f"https://example.com/rec{i}.jpg",
                "isbn": f"9791032724{i:03d}",
                "asin": f"B0FC1DWL9{i:02d}",
                "edition_id": f"edition-rec-{i}",
                "possessions_count": i * 10,
                "not_sold": False,
                "nb_pages": 200 + i,
                "content": None,
            }
            recommendations.append(volume)

        repository._me_recommendations = recommendations

        use_case = GetMeRecommendationsV1UseCase(repository)
        result = use_case()

        assert len(result.volumes) == 50
        assert result.volumes[0].title == "Recommendation 0"
        assert result.volumes[49].title == "Recommendation 49"
        assert result.volumes[49].nb_pages == 249

    def test_get_me_recommendations_varied_content(self, repository: InMemoryUserRepository) -> None:
        """Test de récupération de recommandations avec contenu varié."""
        varied_volumes = [
            {
                "id": "vol-1",
                "title": "Manga Chapter",
                "number": 1,
                "release_date": "2025-12-01",
                "image_url": "https://example.com/manga.jpg",
                "isbn": "9791032724751",
                "asin": "B0FC1DWL9M",
                "edition_id": "edition-manga",
                "possessions_count": 150,
                "not_sold": False,
                "nb_pages": 192,
                "content": "manga",
            },
            {
                "id": "vol-2",
                "title": "Artbook",
                "number": None,
                "release_date": "2025-12-08",
                "image_url": "https://example.com/artbook.jpg",
                "isbn": "9791032724752",
                "asin": "B0FC1DWL9A",
                "edition_id": "edition-artbook",
                "possessions_count": 75,
                "not_sold": False,
                "nb_pages": 128,
                "content": "artbook",
            },
        ]

        repository._me_recommendations = varied_volumes

        use_case = GetMeRecommendationsV1UseCase(repository)
        result = use_case()

        assert len(result.volumes) == 2
        assert result.volumes[0].content == "manga"
        assert result.volumes[0].number == 1
        assert result.volumes[1].content == "artbook"
        assert result.volumes[1].number is None
