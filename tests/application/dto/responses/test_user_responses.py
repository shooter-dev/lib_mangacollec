"""Tests pour les DTOs de réponse User.

This module contains unit tests for User response DTOs.
"""

import pytest

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.domain.entities import Edition, Serie, UserCollection, Volume


class TestGetUserCollectionByUsernameV2Response:
    """Tests pour GetUserCollectionByUsernameV2Response."""

    def test_create_user_collection_response(self) -> None:
        """Test de création d'une réponse collection utilisateur."""
        editions = [
            Edition(
                id="edition-123",
                title="Edition Collector",
                series_id="series-456",
                publisher_id="publisher-789",
                parent_edition_id=None,
                volumes_count=72,
                last_volume_number=72,
                commercial_stop=False,
                not_finished=False,
                follow_editions_count=1443,
            ),
            Edition(
                id="edition-124",
                title=None,
                series_id="series-457",
                publisher_id="publisher-790",
                parent_edition_id=None,
                volumes_count=50,
                last_volume_number=None,
                commercial_stop=False,
                not_finished=True,
                follow_editions_count=500,
            ),
        ]

        series = [
            Serie(
                id="series-456",
                title="Naruto",
                type_id="type-001",
                adult_content=False,
                editions_count=2,
                tasks_count=2,
            ),
            Serie(
                id="series-457",
                title="One Piece",
                type_id="type-001",
                adult_content=False,
                editions_count=1,
                tasks_count=1,
            ),
        ]

        response = GetUserCollectionByUsernameV2Response(
            editions=editions,
            series=series,
        )

        # Vérifier les éditions
        assert len(response.editions) == 2
        assert response.editions[0].id == "edition-123"
        assert response.editions[0].title == "Edition Collector"
        assert response.editions[1].id == "edition-124"
        assert response.editions[1].title is None

        # Vérifier les séries
        assert len(response.series) == 2
        assert response.series[0].title == "Naruto"
        assert response.series[1].title == "One Piece"

    def test_create_user_collection_response_empty(self) -> None:
        """Test de création d'une réponse collection vide."""
        response = GetUserCollectionByUsernameV2Response(
            editions=[],
            series=[],
        )

        assert response.editions == []
        assert response.series == []

    def test_user_collection_response_is_frozen(self) -> None:
        """Test que la réponse est immuable."""
        editions = [
            Edition(
                id="test-edition",
                title="Test Edition",
                series_id="test-series",
                publisher_id="test-publisher",
                parent_edition_id=None,
                volumes_count=10,
                last_volume_number=10,
                commercial_stop=False,
                not_finished=False,
                follow_editions_count=100,
            )
        ]
        response = GetUserCollectionByUsernameV2Response(
            editions=editions,
            series=[],
        )

        with pytest.raises(AttributeError):
            response.editions = []


class TestGetMeCollectionV2Response:
    """Tests pour GetMeCollectionV2Response."""

    def test_create_me_collection_response(self) -> None:
        """Test de création d'une réponse collection personnelle."""
        user_collection = UserCollection(
            id="collection-123",
            user_id="user-456",
            total_editions=150,
            total_volumes=1250,
            total_series=45,
            last_updated="2025-12-12T10:00:00Z",
        )

        editions = [
            Edition(
                id="edition-789",
                title="Personal Edition",
                series_id="series-101",
                publisher_id="publisher-202",
                parent_edition_id=None,
                volumes_count=25,
                last_volume_number=25,
                commercial_stop=False,
                not_finished=False,
                follow_editions_count=300,
            )
        ]

        series = [
            Serie(
                id="series-101",
                title="My Favorite Series",
                type_id="type-002",
                adult_content=False,
                editions_count=1,
                tasks_count=1,
            )
        ]

        response = GetMeCollectionV2Response(
            user_collection=user_collection,
            editions=editions,
            series=series,
        )

        # Vérifier la collection utilisateur
        assert response.user_collection.id == "collection-123"
        assert response.user_collection.user_id == "user-456"
        assert response.user_collection.total_editions == 150
        assert response.user_collection.total_volumes == 1250
        assert response.user_collection.total_series == 45
        assert response.user_collection.last_updated == "2025-12-12T10:00:00Z"

        # Vérifier les éditions
        assert len(response.editions) == 1
        assert response.editions[0].title == "Personal Edition"

        # Vérifier les séries
        assert len(response.series) == 1
        assert response.series[0].title == "My Favorite Series"

    def test_create_me_collection_response_minimal(self) -> None:
        """Test de création d'une réponse collection personnelle minimale."""
        user_collection = UserCollection(
            id="minimal-collection",
            user_id="minimal-user",
        )

        response = GetMeCollectionV2Response(
            user_collection=user_collection,
            editions=[],
            series=[],
        )

        assert response.user_collection.id == "minimal-collection"
        assert response.user_collection.total_editions == 0
        assert response.editions == []
        assert response.series == []

    def test_me_collection_response_is_frozen(self) -> None:
        """Test que la réponse est immuable."""
        user_collection = UserCollection(
            id="test-collection",
            user_id="test-user",
        )
        response = GetMeCollectionV2Response(
            user_collection=user_collection,
            editions=[],
            series=[],
        )

        with pytest.raises(AttributeError):
            response.user_collection = user_collection

        with pytest.raises(AttributeError):
            response.editions = []


class TestGetMeRecommendationsV1Response:
    """Tests pour GetMeRecommendationsV1Response."""

    def test_create_recommendations_response(self) -> None:
        """Test de création d'une réponse recommandations."""
        volumes = [
            Volume(
                id="volume-111",
                title="Recommended Volume 1",
                number=1,
                release_date="2025-12-01",
                isbn="9791032724743",
                asin="B0FC1DWL9R",
                edition_id="edition-111",
                possessions_count=59,
                not_sold=False,
                image_url="https://example.com/image1.jpg",
                nb_pages=None,
                content=None,
            ),
            Volume(
                id="volume-112",
                title=None,
                number=2,
                release_date="2025-12-08",
                isbn="9791032724744",
                asin="B0FC1DWL9S",
                edition_id="edition-112",
                possessions_count=45,
                not_sold=False,
                image_url="https://example.com/image2.jpg",
                nb_pages=200,
                content=None,
            ),
        ]

        response = GetMeRecommendationsV1Response(volumes=volumes)

        # Vérifier les volumes recommandés
        assert len(response.volumes) == 2
        assert response.volumes[0].id == "volume-111"
        assert response.volumes[0].title == "Recommended Volume 1"
        assert response.volumes[0].number == 1
        assert response.volumes[0].isbn == "9791032724743"

        assert response.volumes[1].id == "volume-112"
        assert response.volumes[1].title is None
        assert response.volumes[1].number == 2
        assert response.volumes[1].nb_pages == 200

    def test_create_recommendations_response_empty(self) -> None:
        """Test de création d'une réponse recommandations vide."""
        response = GetMeRecommendationsV1Response(volumes=[])

        assert response.volumes == []

    def test_create_recommendations_response_single_volume(self) -> None:
        """Test de création d'une réponse avec un seul volume recommandé."""
        volume = Volume(
            id="single-volume",
            title="Single Recommendation",
            number=1,
            release_date="2025-12-12",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-single",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/single.jpg",
            nb_pages=300,
            content=None,
        )

        response = GetMeRecommendationsV1Response(volumes=[volume])

        assert len(response.volumes) == 1
        assert response.volumes[0].title == "Single Recommendation"
        assert response.volumes[0].nb_pages == 300

    def test_recommendations_response_is_frozen(self) -> None:
        """Test que la réponse est immuable."""
        volumes = [
            Volume(
                id="frozen-volume",
                title="Frozen Volume",
                number=1,
                release_date="2025-12-01",
                isbn="9791032724750",
                asin="B0FC1DWL9F",
                edition_id="edition-frozen",
                possessions_count=10,
                not_sold=False,
                image_url="https://example.com/frozen.jpg",
                nb_pages=150,
                content=None,
            )
        ]
        response = GetMeRecommendationsV1Response(volumes=volumes)

        with pytest.raises(AttributeError):
            response.volumes = []

    def test_recommendations_response_large_volume_list(self) -> None:
        """Test de création d'une réponse avec une grande liste de volumes."""
        volumes = []
        for i in range(100):
            volume = Volume(
                id=f"volume-{i}",
                title=f"Recommendation {i}",
                number=i + 1,
                release_date="2025-12-01",
                isbn=f"9791032724{i:03d}",
                asin=f"B0FC1DWL9{i:02d}",
                edition_id=f"edition-{i}",
                possessions_count=i * 10,
                not_sold=False,
                image_url=f"https://example.com/image{i}.jpg",
                nb_pages=200 + i,
                content=None,
            )
            volumes.append(volume)

        response = GetMeRecommendationsV1Response(volumes=volumes)

        assert len(response.volumes) == 100
        assert response.volumes[0].title == "Recommendation 0"
        assert response.volumes[99].title == "Recommendation 99"
        assert response.volumes[99].nb_pages == 299
