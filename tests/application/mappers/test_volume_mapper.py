"""Tests pour le VolumeMapper.

This module contains unit tests for the VolumeMapper.
"""

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.application.mappers import VolumeMapper
from mangacollec.domain.entities import (
    Box,
    BoxEdition,
    BoxVolume,
    Edition,
    NativeAdVolumeHomeFirst,
    Publisher,
    Serie,
    TypeSerie,
    Volume,
)


class TestVolumeMapper:
    """Tests pour le mapper Volume."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Volume."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Tome 1 : Le Début",
            "number": 1,
            "release_date": "2023-01-15",
            "isbn": "9782012345678",
            "asin": "2012345678",
            "edition_id": "edition-456",
            "possessions_count": 150,
            "not_sold": False,
            "image_url": "https://example.com/image.jpg",
            "nb_pages": 192,
            "content": "Chapitres 1-3",
        }

        volume = VolumeMapper.from_dict(data)

        assert isinstance(volume, Volume)
        assert volume.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert volume.title == "Tome 1 : Le Début"
        assert volume.number == 1
        assert volume.release_date == "2023-01-15"
        assert volume.isbn == "9782012345678"
        assert volume.asin == "2012345678"
        assert volume.edition_id == "edition-456"
        assert volume.possessions_count == 150
        assert volume.not_sold is False
        assert volume.image_url == "https://example.com/image.jpg"
        assert volume.nb_pages == 192
        assert volume.content == "Chapitres 1-3"

    def test_from_dict_with_minimum_fields(self) -> None:
        """Test de conversion avec les champs minimum."""
        data = {
            "id": "volume-123",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": False,
        }

        volume = VolumeMapper.from_dict(data)

        assert volume.id == "volume-123"
        assert volume.title is None
        assert volume.number == 1
        assert volume.release_date is None
        assert volume.isbn is None
        assert volume.asin is None
        assert volume.edition_id == "edition-456"
        assert volume.possessions_count is None
        assert volume.not_sold is False
        assert volume.image_url is None
        assert volume.nb_pages is None
        assert volume.content is None

    def test_from_dict_without_title(self) -> None:
        """Test de conversion sans titre."""
        data = {
            "id": "test-id",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": False,
            "possessions_count": 50,
        }

        volume = VolumeMapper.from_dict(data)

        assert volume.id == "test-id"
        assert volume.title is None
        assert volume.number == 1

    def test_from_dict_without_isbn_asin(self) -> None:
        """Test de conversion sans ISBN ni ASIN."""
        data = {
            "id": "test-id",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": False,
            "isbn": None,
            "asin": None,
        }

        volume = VolumeMapper.from_dict(data)

        assert volume.isbn is None
        assert volume.asin is None

    def test_from_dict_not_sold(self) -> None:
        """Test de conversion d'un volume non vendu."""
        data = {
            "id": "test-id",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": True,
            "possessions_count": 0,
        }

        volume = VolumeMapper.from_dict(data)

        assert volume.not_sold is True
        assert volume.possessions_count == 0

    def test_from_dict_with_zero_possessions(self) -> None:
        """Test de conversion avec zéro possession."""
        data = {
            "id": "test-id",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": False,
            "possessions_count": 0,
        }

        volume = VolumeMapper.from_dict(data)

        assert volume.possessions_count == 0

    def test_to_dict(self) -> None:
        """Test de conversion d'un Volume en dictionnaire."""
        volume = Volume(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Tome 1 : Le Début",
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=150,
            not_sold=False,
            image_url="https://example.com/image.jpg",
            nb_pages=192,
            content="Chapitres 1-3",
        )

        result = VolumeMapper.to_dict(volume)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Tome 1 : Le Début",
            "number": 1,
            "release_date": "2023-01-15",
            "isbn": "9782012345678",
            "asin": "2012345678",
            "edition_id": "edition-456",
            "possessions_count": 150,
            "not_sold": False,
            "image_url": "https://example.com/image.jpg",
            "nb_pages": 192,
            "content": "Chapitres 1-3",
        }

    def test_to_dict_with_nulls(self) -> None:
        """Test de conversion avec valeurs nulles."""
        volume = Volume(
            id="test-id",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=None,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        result = VolumeMapper.to_dict(volume)

        assert result == {
            "id": "test-id",
            "title": None,
            "number": 1,
            "release_date": None,
            "isbn": None,
            "asin": None,
            "edition_id": "edition-456",
            "possessions_count": None,
            "not_sold": False,
            "image_url": None,
            "nb_pages": None,
            "content": None,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test Volume",
            "number": 1,
            "release_date": "2023-01-15",
            "isbn": "9782012345678",
            "asin": "2012345678",
            "edition_id": "edition-456",
            "possessions_count": 50,
            "not_sold": False,
            "image_url": "https://example.com/image.jpg",
            "nb_pages": 192,
            "content": "Test content",
        }

        # dict -> entity -> dict
        volume = VolumeMapper.from_dict(original_data)
        result_data = VolumeMapper.to_dict(volume)

        assert result_data == original_data

    def test_round_trip_conversion_with_nulls(self) -> None:
        """Test de conversion bidirectionnelle avec valeurs nulles."""
        original_data = {
            "id": "test-id",
            "title": None,
            "number": 1,
            "release_date": None,
            "isbn": None,
            "asin": None,
            "edition_id": "edition-456",
            "possessions_count": None,
            "not_sold": True,
            "image_url": None,
            "nb_pages": None,
            "content": None,
        }

        # dict -> entity -> dict
        volume = VolumeMapper.from_dict(original_data)
        result_data = VolumeMapper.to_dict(volume)

        assert result_data == original_data

    def test_from_api_response_with_all_entities(self) -> None:
        """Test de conversion de la réponse complète de l'API V2."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Tome 1",
                    "number": 1,
                    "release_date": "2023-01-15",
                    "isbn": "9782012345678",
                    "asin": "2012345678",
                    "edition_id": "edition-456",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "https://example.com/image.jpg",
                    "nb_pages": 192,
                    "content": "Chapitres 1-3",
                }
            ],
            "editions": [
                {
                    "id": "edition-456",
                    "title": "Edition Collector",
                    "series_id": "series-789",
                    "publisher_id": "publisher-001",
                    "parent_edition_id": None,
                    "volumes_count": 12,
                    "last_volume_number": 12,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 300,
                }
            ],
            "publishers": [
                {
                    "id": "publisher-001",
                    "title": "Kana",
                    "closed": False,
                    "editions_count": 150,
                    "no_amazon": False,
                }
            ],
            "series": [
                {
                    "id": "series-789",
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
            "box_volumes": [
                {
                    "id": "box-volume-123",
                    "title": None,
                    "number": 1,
                    "release_date": None,
                    "isbn": None,
                    "asin": None,
                    "edition_id": "edition-456",
                    "possessions_count": None,
                    "not_sold": False,
                    "image_url": None,
                }
            ],
            "boxes": [
                {
                    "id": "box-456",
                    "title": "Intégrale Saison 1",
                    "number": 1,
                    "release_date": None,
                    "isbn": None,
                    "asin": None,
                    "commercial_stop": False,
                    "box_edition_id": "box-edition-123",
                    "box_possessions_count": None,
                    "image_url": None,
                }
            ],
            "box_editions": [
                {
                    "id": "box-edition-123",
                    "title": None,
                    "publisher_id": "publisher-001",
                    "boxes_count": 1,
                    "adult_content": False,
                    "box_follow_editions_count": 10,
                }
            ],
        }

        result = VolumeMapper.from_api_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetVolumeByIdV2Response)

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert isinstance(result.volumes[0], Volume)
        assert result.volumes[0].id == "volume-123"
        assert result.volumes[0].title == "Tome 1"

        # Vérifier les editions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].id == "edition-456"
        assert result.editions[0].title == "Edition Collector"

        # Vérifier les publishers
        assert len(result.publishers) == 1
        assert isinstance(result.publishers[0], Publisher)
        assert result.publishers[0].id == "publisher-001"
        assert result.publishers[0].title == "Kana"

        # Vérifier les series
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].id == "series-789"
        assert result.series[0].title == "Naruto"

        # Vérifier les types
        assert len(result.types) == 1
        assert isinstance(result.types[0], TypeSerie)
        assert result.types[0].id == "type-001"
        assert result.types[0].title == "Manga"

        # Vérifier les box_volumes
        assert len(result.box_volumes) == 1
        assert isinstance(result.box_volumes[0], BoxVolume)
        assert result.box_volumes[0].id == "box-volume-123"
        assert result.box_volumes[0].edition_id == "edition-456"

        # Vérifier les boxes
        assert len(result.boxes) == 1
        assert isinstance(result.boxes[0], Box)
        assert result.boxes[0].id == "box-456"
        assert result.boxes[0].title == "Intégrale Saison 1"
        assert result.boxes[0].box_edition_id == "box-edition-123"

        # Vérifier les box_editions
        assert len(result.box_editions) == 1
        assert isinstance(result.box_editions[0], BoxEdition)
        assert result.box_editions[0].id == "box-edition-123"
        assert result.box_editions[0].publisher_id == "publisher-001"

    def test_from_api_response_with_empty_lists(self) -> None:
        """Test de conversion avec listes vides."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Volume Test",
                    "number": 1,
                    "edition_id": "edition-456",
                    "not_sold": False,
                }
            ],
            "editions": [
                {
                    "id": "edition-456",
                    "title": "Edition Test",
                    "series_id": "series-789",
                    "publisher_id": "publisher-001",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            "publishers": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        result = VolumeMapper.from_api_response(api_response)

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert len(result.editions) == 1
        assert result.publishers == []
        assert result.series == []
        assert result.types == []
        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []

    def test_from_api_response_with_missing_keys(self) -> None:
        """Test de conversion avec clés manquantes (utilise .get())."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Volume Test",
                    "number": 1,
                    "edition_id": "edition-456",
                    "not_sold": False,
                }
            ],
            "editions": [],
        }

        result = VolumeMapper.from_api_response(api_response)

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.editions == []
        assert result.publishers == []
        assert result.series == []
        assert result.types == []
        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []

    def test_from_api_response_with_multiple_volumes(self) -> None:
        """Test de conversion avec plusieurs volumes."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Tome 1",
                    "number": 1,
                    "edition_id": "edition-456",
                    "not_sold": False,
                },
                {
                    "id": "volume-124",
                    "title": "Tome 2",
                    "number": 2,
                    "edition_id": "edition-456",
                    "not_sold": False,
                },
            ],
            "editions": [],
            "publishers": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        result = VolumeMapper.from_api_response(api_response)

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 2
        assert result.volumes[0].number == 1
        assert result.volumes[1].number == 2

    def test_from_volumes_news_response_with_all_entities(self) -> None:
        """Test de conversion de la réponse news de l'API V2."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Nouveauté Tome 1",
                    "number": 1,
                    "release_date": "2023-12-01",
                    "isbn": None,
                    "asin": None,
                    "edition_id": "edition-456",
                    "possessions_count": 50,
                    "not_sold": False,
                    "image_url": "https://example.com/new.jpg",
                    "nb_pages": None,
                    "content": None,
                }
            ],
            "editions": [
                {
                    "id": "edition-456",
                    "title": "Nouvelle Édition",
                    "series_id": "series-789",
                    "publisher_id": None,
                    "parent_edition_id": None,
                    "volumes_count": 5,
                    "last_volume_number": None,
                    "commercial_stop": False,
                    "not_finished": True,
                    "follow_editions_count": 100,
                }
            ],
            "series": [
                {
                    "id": "series-789",
                    "title": "Nouvelle Série",
                    "type_id": "type-001",
                    "adult_content": False,
                    "editions_count": 2,
                    "tasks_count": 3,
                }
            ],
            "types": [
                {
                    "id": "type-001",
                    "title": "Manga",
                    "to_display": True,
                }
            ],
            "box_volumes": [
                {
                    "id": "box-volume-123",
                    "title": None,
                    "number": 1,
                    "release_date": None,
                    "isbn": None,
                    "asin": None,
                    "edition_id": "edition-456",
                    "possessions_count": None,
                    "not_sold": False,
                    "image_url": None,
                }
            ],
            "boxes": [
                {
                    "id": "box-456",
                    "title": "Box Set Nouveauté",
                    "number": 1,
                    "release_date": None,
                    "isbn": None,
                    "asin": None,
                    "commercial_stop": False,
                    "box_edition_id": "box-edition-123",
                    "box_possessions_count": None,
                    "image_url": None,
                }
            ],
            "box_editions": [
                {
                    "id": "box-edition-123",
                    "title": None,
                    "publisher_id": "publisher-001",
                    "boxes_count": 1,
                    "adult_content": False,
                    "box_follow_editions_count": 10,
                }
            ],
            "native_ad_volume_home_first": {
                "id": "ad-123",
                "volume_id": "volume-123",
                "title": "Publicité Spéciale",
                "start_date": "2023-12-01",
                "end_date": "2023-12-31",
            },
        }

        result = VolumeMapper.from_volumes_news_response(api_response)

        # Vérifier le type de retour
        assert isinstance(result, GetVolumesNewsV2Response)

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert isinstance(result.volumes[0], Volume)
        assert result.volumes[0].id == "volume-123"
        assert result.volumes[0].title == "Nouveauté Tome 1"

        # Vérifier les editions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].id == "edition-456"

        # Vérifier les series
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].id == "series-789"

        # Vérifier les types
        assert len(result.types) == 1
        assert isinstance(result.types[0], TypeSerie)
        assert result.types[0].id == "type-001"

        # Vérifier les box_volumes
        assert len(result.box_volumes) == 1
        assert isinstance(result.box_volumes[0], BoxVolume)
        assert result.box_volumes[0].edition_id == "edition-456"

        # Vérifier les boxes
        assert len(result.boxes) == 1
        assert isinstance(result.boxes[0], Box)
        assert result.boxes[0].title == "Box Set Nouveauté"
        assert result.boxes[0].box_edition_id == "box-edition-123"

        # Vérifier les box_editions
        assert len(result.box_editions) == 1
        assert isinstance(result.box_editions[0], BoxEdition)
        assert result.box_editions[0].publisher_id == "publisher-001"

        # Vérifier la publicité native
        assert result.native_ad_volume_home_first is not None
        assert isinstance(result.native_ad_volume_home_first, NativeAdVolumeHomeFirst)
        assert result.native_ad_volume_home_first.id == "ad-123"
        assert result.native_ad_volume_home_first.volume_id == "volume-123"
        assert result.native_ad_volume_home_first.title == "Publicité Spéciale"

    def test_from_volumes_news_response_without_native_ad(self) -> None:
        """Test de conversion sans publicité native."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Nouveauté",
                    "number": 1,
                    "edition_id": "edition-456",
                    "not_sold": False,
                }
            ],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        result = VolumeMapper.from_volumes_news_response(api_response)

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert result.native_ad_volume_home_first is None

    def test_from_volumes_news_response_with_empty_lists(self) -> None:
        """Test de conversion de réponse news avec listes vides."""
        api_response = {
            "volumes": [],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        result = VolumeMapper.from_volumes_news_response(api_response)

        assert isinstance(result, GetVolumesNewsV2Response)
        assert result.volumes == []
        assert result.editions == []
        assert result.series == []
        assert result.types == []
        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []
        assert result.native_ad_volume_home_first is None

    def test_from_volumes_news_response_with_multiple_volumes(self) -> None:
        """Test de conversion news avec plusieurs volumes."""
        api_response = {
            "volumes": [
                {
                    "id": "volume-123",
                    "title": "Nouveauté 1",
                    "number": 1,
                    "edition_id": "edition-456",
                    "not_sold": False,
                },
                {
                    "id": "volume-124",
                    "title": "Nouveauté 2",
                    "number": 2,
                    "edition_id": "edition-456",
                    "not_sold": False,
                },
            ],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        result = VolumeMapper.from_volumes_news_response(api_response)

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 2
        assert result.volumes[0].title == "Nouveauté 1"
        assert result.volumes[1].title == "Nouveauté 2"
