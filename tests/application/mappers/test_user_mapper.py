"""Tests pour le UserMapper.

This module contains unit tests for the UserMapper.
"""

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.application.mappers import UserMapper
from mangacollec.domain.entities import (Edition, Serie, User, UserCollection,
                                         Volume)


class TestUserMapper:
    """Tests pour le mapper User."""

    def test_from_dict_user_complete(self) -> None:
        """Test de conversion d'un dictionnaire complet en User."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "username": "shooterdev",
            "email": "shooter@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "avatar_url": "https://example.com/avatar.jpg",
        }

        user = UserMapper.from_dict(data)

        assert isinstance(user, User)
        assert user.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert user.username == "shooterdev"
        assert user.email == "shooter@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.avatar_url == "https://example.com/avatar.jpg"

    def test_from_dict_user_minimal(self) -> None:
        """Test de conversion d'un dictionnaire minimal en User."""
        data = {
            "id": "d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            "username": "boichi",
        }

        user = UserMapper.from_dict(data)

        assert user.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
        assert user.username == "boichi"
        assert user.email is None
        assert user.first_name is None
        assert user.last_name is None
        assert user.avatar_url is None

    def test_from_dict_user_without_avatar(self) -> None:
        """Test de conversion sans avatar."""
        data = {
            "id": "test-id",
            "username": "testuser",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
        }

        user = UserMapper.from_dict(data)

        assert user.avatar_url is None

    def test_from_dict_user_collection_complete(self) -> None:
        """Test de conversion d'un dictionnaire complet en UserCollection."""
        data = {
            "id": "collection-123",
            "user_id": "user-456",
            "total_editions": 150,
            "total_volumes": 1250,
            "total_series": 45,
            "last_updated": "2025-12-12T10:00:00Z",
        }

        collection = UserMapper.from_dict_collection(data)

        assert isinstance(collection, UserCollection)
        assert collection.id == "collection-123"
        assert collection.user_id == "user-456"
        assert collection.total_editions == 150
        assert collection.total_volumes == 1250
        assert collection.total_series == 45
        assert collection.last_updated == "2025-12-12T10:00:00Z"

    def test_from_dict_user_collection_minimal(self) -> None:
        """Test de conversion d'un dictionnaire minimal en UserCollection."""
        data = {
            "id": "minimal-collection",
            "user_id": "minimal-user",
        }

        collection = UserMapper.from_dict_collection(data)

        assert collection.id == "minimal-collection"
        assert collection.user_id == "minimal-user"
        assert collection.total_editions == 0
        assert collection.total_volumes == 0
        assert collection.total_series == 0
        assert collection.last_updated is None

    def test_to_dict_user(self) -> None:
        """Test de conversion d'un User en dictionnaire."""
        user = User(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            username="shooterdev",
            email="shooter@example.com",
            first_name="John",
            last_name="Doe",
            avatar_url="https://example.com/avatar.jpg",
        )

        result = UserMapper.to_dict(user)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "username": "shooterdev",
            "email": "shooter@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "avatar_url": "https://example.com/avatar.jpg",
        }

    def test_to_dict_user_with_nulls(self) -> None:
        """Test de conversion avec valeurs nulles."""
        user = User(
            id="test-id",
            username="testuser",
            email=None,
            first_name=None,
            last_name=None,
            avatar_url=None,
        )

        result = UserMapper.to_dict(user)

        assert result == {
            "id": "test-id",
            "username": "testuser",
            "email": None,
            "first_name": None,
            "last_name": None,
            "avatar_url": None,
        }

    def test_to_dict_user_collection(self) -> None:
        """Test de conversion d'une UserCollection en dictionnaire."""
        collection = UserCollection(
            id="collection-123",
            user_id="user-456",
            total_editions=150,
            total_volumes=1250,
            total_series=45,
            last_updated="2025-12-12T10:00:00Z",
        )

        result = UserMapper.to_dict_collection(collection)

        assert result == {
            "id": "collection-123",
            "user_id": "user-456",
            "total_editions": 150,
            "total_volumes": 1250,
            "total_series": 45,
            "last_updated": "2025-12-12T10:00:00Z",
        }

    def test_round_trip_conversion_user(self) -> None:
        """Test de conversion bidirectionnelle User (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "username": "roundtrip_user",
            "email": "roundtrip@example.com",
            "first_name": "Round",
            "last_name": "Trip",
            "avatar_url": "https://example.com/roundtrip.jpg",
        }

        # dict -> entity -> dict
        user = UserMapper.from_dict(original_data)
        result_data = UserMapper.to_dict(user)

        assert result_data == original_data

    def test_round_trip_conversion_user_collection(self) -> None:
        """Test de conversion bidirectionnelle UserCollection."""
        original_data = {
            "id": "roundtrip-collection",
            "user_id": "roundtrip-user",
            "total_editions": 100,
            "total_volumes": 1000,
            "total_series": 25,
            "last_updated": "2025-12-12T15:30:00Z",
        }

        # dict -> entity -> dict
        collection = UserMapper.from_dict_collection(original_data)
        result_data = UserMapper.to_dict_collection(collection)

        assert result_data == original_data

    def test_from_user_collection_username_v2_response(self) -> None:
        """Test de conversion de la réponse GetUserCollectionByUsernameV2."""
        api_response = {
            "editions": [
                {
                    "id": "edition-123",
                    "title": "User Edition",
                    "series_id": "series-456",
                    "publisher_id": "publisher-789",
                    "parent_edition_id": None,
                    "volumes_count": 72,
                    "last_volume_number": 72,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 1443,
                }
            ],
            "series": [
                {
                    "id": "series-456",
                    "title": "User Series",
                    "type_id": "type-001",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 1,
                }
            ],
        }

        result = UserMapper.from_user_collection_username_v2_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetUserCollectionByUsernameV2Response)

        # Vérifier les éditions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].id == "edition-123"
        assert result.editions[0].title == "User Edition"

        # Vérifier les séries
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].id == "series-456"
        assert result.series[0].title == "User Series"

    def test_from_user_collection_username_v2_response_empty(self) -> None:
        """Test de conversion avec réponse vide."""
        api_response = {
            "editions": [],
            "series": [],
        }

        result = UserMapper.from_user_collection_username_v2_response(api_response)

        assert isinstance(result, GetUserCollectionByUsernameV2Response)
        assert result.editions == []
        assert result.series == []

    def test_from_me_collection_v2_response(self) -> None:
        """Test de conversion de la réponse GetMeCollectionV2."""
        api_response = {
            "user_collection": {
                "id": "collection-me",
                "user_id": "user-me",
                "total_editions": 75,
                "total_volumes": 750,
                "total_series": 30,
                "last_updated": "2025-12-12T12:00:00Z",
            },
            "editions": [
                {
                    "id": "edition-me-1",
                    "title": "My Edition",
                    "series_id": "series-me-1",
                    "publisher_id": "publisher-me-1",
                    "parent_edition_id": None,
                    "volumes_count": 25,
                    "last_volume_number": 25,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 500,
                }
            ],
            "series": [
                {
                    "id": "series-me-1",
                    "title": "My Series",
                    "type_id": "type-002",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 1,
                }
            ],
        }

        result = UserMapper.from_me_collection_v2_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetMeCollectionV2Response)

        # Vérifier la collection utilisateur
        assert isinstance(result.user_collection, UserCollection)
        assert result.user_collection.id == "collection-me"
        assert result.user_collection.user_id == "user-me"
        assert result.user_collection.total_editions == 75
        assert result.user_collection.total_volumes == 750
        assert result.user_collection.total_series == 30

        # Vérifier les éditions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].title == "My Edition"

        # Vérifier les séries
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].title == "My Series"

    def test_from_me_recommendations_v1_response(self) -> None:
        """Test de conversion de la réponse GetMeRecommendationsV1."""
        api_response = [
            {
                "id": "volume-rec-1",
                "title": "Recommended Volume 1",
                "number": 1,
                "release_date": "2025-12-01",
                "image_url": "https://example.com/rec1.jpg",
                "isbn": "9791032724743",
                "asin": "B0FC1DWL9R",
                "edition_id": "edition-rec-1",
                "possessions_count": 59,
                "not_sold": False,
                "nb_pages": 200,
                "content": None,
            },
            {
                "id": "volume-rec-2",
                "title": None,
                "number": 2,
                "release_date": "2025-12-08",
                "image_url": "https://example.com/rec2.jpg",
                "isbn": "9791032724744",
                "asin": "B0FC1DWL9S",
                "edition_id": "edition-rec-2",
                "possessions_count": 45,
                "not_sold": False,
                "nb_pages": None,
                "content": None,
            },
        ]

        result = UserMapper.from_me_recommendations_v1_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetMeRecommendationsV1Response)

        # Vérifier les volumes recommandés
        assert len(result.volumes) == 2
        assert all(isinstance(volume, Volume) for volume in result.volumes)

        assert result.volumes[0].id == "volume-rec-1"
        assert result.volumes[0].title == "Recommended Volume 1"
        assert result.volumes[0].number == 1
        assert result.volumes[0].nb_pages == 200

        assert result.volumes[1].id == "volume-rec-2"
        assert result.volumes[1].title is None
        assert result.volumes[1].number == 2
        assert result.volumes[1].nb_pages is None

    def test_from_me_recommendations_v1_response_empty(self) -> None:
        """Test de conversion avec liste de recommandations vide."""
        api_response = []

        result = UserMapper.from_me_recommendations_v1_response(api_response)

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert result.volumes == []

    def test_from_me_recommendations_v1_response_single_item(self) -> None:
        """Test de conversion avec un seul volume recommandé."""
        api_response = [
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

        result = UserMapper.from_me_recommendations_v1_response(api_response)

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].title == "Single Recommendation"
        assert result.volumes[0].nb_pages == 300

    def test_from_me_recommendations_v1_response_missing_optional_fields(self) -> None:
        """Test de conversion avec champs optionnels manquants."""
        api_response = [
            {
                "id": "minimal-rec",
                "number": 1,
                "release_date": "2025-12-01",
                "image_url": "https://example.com/minimal.jpg",
                "isbn": "9791032724750",
                "asin": "B0FC1DWL9F",
                "edition_id": "edition-minimal",
                "possessions_count": 10,
                "not_sold": False,
            }
        ]

        result = UserMapper.from_me_recommendations_v1_response(api_response)

        assert isinstance(result, GetMeRecommendationsV1Response)
        assert len(result.volumes) == 1
        volume = result.volumes[0]
        assert volume.title is None
        assert volume.nb_pages is None
        assert volume.content is None
        assert volume.number == 1
        assert volume.possessions_count == 10
