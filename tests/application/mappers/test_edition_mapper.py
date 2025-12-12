"""Tests pour le EditionMapper.

This module contains unit tests for the EditionMapper.
"""

from mangacollec.application.dto import GetEditionByIdV2Response
from mangacollec.application.mappers import EditionMapper
from mangacollec.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume


class TestEditionMapper:
    """Tests pour le mapper Edition."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Edition."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Edition Collector",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 1443,
        }

        edition = EditionMapper.from_dict(data)

        assert isinstance(edition, Edition)
        assert edition.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert edition.title == "Edition Collector"
        assert edition.series_id == "series-123"
        assert edition.publisher_id == "publisher-456"
        assert edition.parent_edition_id == "parent-789"
        assert edition.volumes_count == 72
        assert edition.last_volume_number == 72
        assert edition.commercial_stop is False
        assert edition.not_finished is False
        assert edition.follow_editions_count == 1443

    def test_from_dict_without_title(self) -> None:
        """Test de conversion sans titre."""
        data = {
            "id": "test-id",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.id == "test-id"
        assert edition.title is None
        assert edition.series_id == "series-123"
        assert edition.publisher_id == "publisher-456"

    def test_from_dict_without_parent_edition(self) -> None:
        """Test de conversion sans édition parente."""
        data = {
            "id": "test-id",
            "title": "Main Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.parent_edition_id is None

    def test_from_dict_without_last_volume_number(self) -> None:
        """Test de conversion sans numéro de dernier volume."""
        data = {
            "id": "test-id",
            "title": "Ongoing Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.last_volume_number is None

    def test_from_dict_commercial_stop(self) -> None:
        """Test de conversion avec arrêt commercial."""
        data = {
            "id": "test-id",
            "title": "Stopped Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 10,
            "last_volume_number": 10,
            "commercial_stop": True,
            "not_finished": False,
            "follow_editions_count": 50,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.commercial_stop is True
        assert edition.not_finished is False

    def test_from_dict_not_finished(self) -> None:
        """Test de conversion avec série non terminée."""
        data = {
            "id": "test-id",
            "title": "Ongoing Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 500,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.not_finished is True
        assert edition.commercial_stop is False

    def test_to_dict(self) -> None:
        """Test de conversion d'une Edition en dictionnaire."""
        edition = Edition(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Edition Collector",
            series_id="series-123",
            publisher_id="publisher-456",
            parent_edition_id="parent-789",
            volumes_count=72,
            last_volume_number=72,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=1443,
        )

        result = EditionMapper.to_dict(edition)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Edition Collector",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 1443,
        }

    def test_to_dict_with_nulls(self) -> None:
        """Test de conversion avec valeurs nulles."""
        edition = Edition(
            id="test-id",
            title=None,
            series_id="series-123",
            publisher_id="publisher-456",
            parent_edition_id=None,
            volumes_count=50,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=100,
        )

        result = EditionMapper.to_dict(edition)

        assert result == {
            "id": "test-id",
            "title": None,
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": None,
            "volumes_count": 50,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 100,
            "last_volume_number": 100,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 200,
        }

        # dict -> entity -> dict
        edition = EditionMapper.from_dict(original_data)
        result_data = EditionMapper.to_dict(edition)

        assert result_data == original_data

    def test_round_trip_conversion_with_nulls(self) -> None:
        """Test de conversion bidirectionnelle avec valeurs nulles."""
        original_data = {
            "id": "test-id",
            "title": None,
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": None,
            "volumes_count": 50,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        # dict -> entity -> dict
        edition = EditionMapper.from_dict(original_data)
        result_data = EditionMapper.to_dict(edition)

        assert result_data == original_data

    def test_from_api_response_with_all_entities(self) -> None:
        """Test de conversion de la réponse complète de l'API V2."""
        api_response = {
            "editions": [
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
                }
            ],
            "publishers": [
                {
                    "id": "publisher-789",
                    "title": "Kana",
                    "closed": False,
                    "editions_count": 150,
                    "no_amazon": False,
                }
            ],
            "series": [
                {
                    "id": "series-456",
                    "title": "Naruto",
                    "type_id": "type-001",
                    "adult_content": False,
                    "editions_count": 7,
                    "tasks_count": 1,
                }
            ],
            "types": [
                {
                    "id": "type-001",
                    "title": "Manga",
                    "to_display": True,
                }
            ],
            "volumes": [
                {
                    "id": "volume-001",
                    "title": None,
                    "number": 1,
                    "release_date": "2002-03-01",
                    "isbn": "9782012345678",
                    "asin": "2012345678",
                    "edition_id": "edition-123",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "https://example.com/image.jpg",
                }
            ],
        }

        result = EditionMapper.from_api_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetEditionByIdV2Response)

        # Vérifier les éditions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].id == "edition-123"
        assert result.editions[0].title == "Edition Collector"

        # Vérifier les publishers
        assert len(result.publishers) == 1
        assert isinstance(result.publishers[0], Publisher)
        assert result.publishers[0].id == "publisher-789"
        assert result.publishers[0].title == "Kana"

        # Vérifier les series
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].id == "series-456"
        assert result.series[0].title == "Naruto"

        # Vérifier les types
        assert len(result.types) == 1
        assert isinstance(result.types[0], TypeSerie)
        assert result.types[0].id == "type-001"
        assert result.types[0].title == "Manga"

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert isinstance(result.volumes[0], Volume)
        assert result.volumes[0].id == "volume-001"
        assert result.volumes[0].number == 1

    def test_from_api_response_with_empty_lists(self) -> None:
        """Test de conversion avec listes vides."""
        api_response = {
            "editions": [
                {
                    "id": "edition-123",
                    "title": "Edition Test",
                    "series_id": "series-456",
                    "publisher_id": "publisher-789",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            "publishers": [
                {
                    "id": "publisher-789",
                    "title": "Test Publisher",
                    "closed": False,
                    "editions_count": 10,
                    "no_amazon": False,
                }
            ],
            "series": [],
            "types": [],
            "volumes": [],
        }

        result = EditionMapper.from_api_response(api_response)

        assert isinstance(result, GetEditionByIdV2Response)
        assert len(result.editions) == 1
        assert len(result.publishers) == 1
        assert result.series == []
        assert result.types == []
        assert result.volumes == []

    def test_from_api_response_with_missing_keys(self) -> None:
        """Test de conversion avec clés manquantes (utilise .get())."""
        api_response = {
            "editions": [
                {
                    "id": "edition-123",
                    "title": "Edition Test",
                    "series_id": "series-456",
                    "publisher_id": "publisher-789",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            "publishers": [],
        }

        result = EditionMapper.from_api_response(api_response)

        assert isinstance(result, GetEditionByIdV2Response)
        assert len(result.editions) == 1
        assert result.publishers == []
        assert result.series == []
        assert result.types == []
        assert result.volumes == []

    def test_from_api_response_with_multiple_editions(self) -> None:
        """Test de conversion avec plusieurs éditions (parent et enfants)."""
        api_response = {
            "editions": [
                {
                    "id": "edition-parent",
                    "title": "Edition Standard",
                    "series_id": "series-456",
                    "publisher_id": "publisher-789",
                    "volumes_count": 72,
                    "last_volume_number": 72,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 1000,
                },
                {
                    "id": "edition-child",
                    "title": "Edition Deluxe",
                    "series_id": "series-456",
                    "publisher_id": "publisher-789",
                    "parent_edition_id": "edition-parent",
                    "volumes_count": 72,
                    "last_volume_number": 72,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 500,
                },
            ],
            "publishers": [],
            "series": [],
            "types": [],
            "volumes": [],
        }

        result = EditionMapper.from_api_response(api_response)

        assert isinstance(result, GetEditionByIdV2Response)
        assert len(result.editions) == 2
        assert result.editions[0].id == "edition-parent"
        assert result.editions[1].id == "edition-child"
        assert result.editions[1].parent_edition_id == "edition-parent"
