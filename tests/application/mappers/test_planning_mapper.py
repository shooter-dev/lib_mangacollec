"""Tests unitaires pour PlanningMapper.

This module contains unit tests for the PlanningMapper.
"""

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.application.mappers import PlanningMapper
from mangacollec.domain.entities import Box, BoxEdition, BoxVolume, Edition, Serie, TypeSerie, Volume


class TestPlanningMapperFromPlanningV2Response:
    """Tests pour la méthode from_planning_v2_response."""

    def test_from_planning_v2_response_with_complete_data(self) -> None:
        """Test la conversion d'une réponse API complète en GetPlanningV2Response."""
        # Arrange
        response = {
            "volumes": [
                {
                    "id": "vol-1",
                    "title": "Volume 1",
                    "number": 1,
                    "release_date": "2022-09-01",
                    "isbn": "9781234567890",
                    "asin": "B001",
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/vol1.jpg",
                }
            ],
            "editions": [
                {
                    "id": "ed-1",
                    "title": "Edition 1",
                    "series_id": "series-1",
                    "publisher_id": "pub-1",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            "series": [
                {
                    "id": "series-1",
                    "title": "Serie 1",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 5,
                    "tasks_count": 2,
                }
            ],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
            "boxes": [
                {
                    "id": "box-1",
                    "title": "Box 1",
                    "number": 1,
                    "release_date": "2022-10-01",
                    "isbn": "9780987654321",
                    "asin": "B002",
                    "commercial_stop": False,
                    "box_edition_id": "be-1",
                    "box_possessions_count": 50,
                    "image_url": "http://example.com/box1.jpg",
                }
            ],
            "box_editions": [
                {
                    "id": "be-1",
                    "title": "Box Edition 1",
                    "publisher_id": "pub-1",
                    "boxes_count": 2,
                    "adult_content": False,
                    "box_follow_editions_count": 10,
                }
            ],
            "box_volumes": [
                {
                    "id": "bv-1",
                    "title": None,
                    "number": 1,
                    "release_date": "2022-10-01",
                    "isbn": "9781234567890",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/boxvol1.jpg",
                }
            ],
        }

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert isinstance(result, GetPlanningV2Response)

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert isinstance(result.volumes[0], Volume)
        assert result.volumes[0].id == "vol-1"
        assert result.volumes[0].title == "Volume 1"
        assert result.volumes[0].number == 1

        # Vérifier les éditions
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert result.editions[0].id == "ed-1"
        assert result.editions[0].title == "Edition 1"

        # Vérifier les séries
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert result.series[0].id == "series-1"
        assert result.series[0].title == "Serie 1"

        # Vérifier les types
        assert len(result.types) == 1
        assert isinstance(result.types[0], TypeSerie)
        assert result.types[0].id == "type-1"
        assert result.types[0].title == "Manga"

        # Vérifier les boxes
        assert len(result.boxes) == 1
        assert isinstance(result.boxes[0], Box)
        assert result.boxes[0].id == "box-1"
        assert result.boxes[0].title == "Box 1"

        # Vérifier les box_editions
        assert len(result.box_editions) == 1
        assert isinstance(result.box_editions[0], BoxEdition)
        assert result.box_editions[0].id == "be-1"

        # Vérifier les box_volumes
        assert len(result.box_volumes) == 1
        assert isinstance(result.box_volumes[0], BoxVolume)
        assert result.box_volumes[0].id == "bv-1"

    def test_from_planning_v2_response_with_empty_response(self) -> None:
        """Test la conversion d'une réponse vide."""
        # Arrange
        response = {}

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

    def test_from_planning_v2_response_with_empty_lists(self) -> None:
        """Test la conversion avec des listes vides."""
        # Arrange
        response = {
            "volumes": [],
            "editions": [],
            "series": [],
            "types": [],
            "boxes": [],
            "box_editions": [],
            "box_volumes": [],
        }

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

    def test_from_planning_v2_response_with_multiple_items(self) -> None:
        """Test la conversion avec plusieurs items de chaque type."""
        # Arrange
        response = {
            "volumes": [
                {
                    "id": "vol-1",
                    "title": "Volume 1",
                    "number": 1,
                    "release_date": "2022-09-01",
                    "isbn": "9781234567890",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/vol1.jpg",
                },
                {
                    "id": "vol-2",
                    "title": "Volume 2",
                    "number": 2,
                    "release_date": "2022-10-01",
                    "isbn": "9781234567891",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 95,
                    "not_sold": False,
                    "image_url": "http://example.com/vol2.jpg",
                },
            ],
            "editions": [
                {
                    "id": "ed-1",
                    "title": "Edition 1",
                    "series_id": "series-1",
                    "publisher_id": "pub-1",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                },
                {
                    "id": "ed-2",
                    "title": "Edition 2",
                    "series_id": "series-2",
                    "publisher_id": "pub-2",
                    "volumes_count": 5,
                    "commercial_stop": False,
                    "not_finished": True,
                    "follow_editions_count": 25,
                },
            ],
            "series": [
                {
                    "id": "series-1",
                    "title": "Serie 1",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 5,
                    "tasks_count": 2,
                }
            ],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
            "boxes": [
                {
                    "id": "box-1",
                    "title": "Box 1",
                    "number": 1,
                    "release_date": "2022-10-01",
                    "isbn": "9780987654321",
                    "asin": None,
                    "commercial_stop": False,
                    "box_edition_id": "be-1",
                    "box_possessions_count": 50,
                    "image_url": "http://example.com/box1.jpg",
                }
            ],
            "box_editions": [
                {
                    "id": "be-1",
                    "title": "Box Edition 1",
                    "publisher_id": "pub-1",
                    "boxes_count": 2,
                    "adult_content": False,
                    "box_follow_editions_count": 10,
                }
            ],
            "box_volumes": [
                {
                    "id": "bv-1",
                    "title": None,
                    "number": 1,
                    "release_date": "2022-10-01",
                    "isbn": "9781234567890",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/boxvol1.jpg",
                }
            ],
        }

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert len(result.volumes) == 2
        assert result.volumes[0].id == "vol-1"
        assert result.volumes[1].id == "vol-2"

        assert len(result.editions) == 2
        assert result.editions[0].id == "ed-1"
        assert result.editions[1].id == "ed-2"

        assert len(result.series) == 1
        assert len(result.types) == 1
        assert len(result.boxes) == 1
        assert len(result.box_editions) == 1
        assert len(result.box_volumes) == 1

    def test_from_planning_v2_response_preserves_order(self) -> None:
        """Test que l'ordre des éléments est préservé."""
        # Arrange
        response = {
            "volumes": [
                {
                    "id": "vol-3",
                    "title": "Volume 3",
                    "number": 3,
                    "release_date": "2022-11-01",
                    "isbn": "9781234567892",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 90,
                    "not_sold": False,
                    "image_url": "http://example.com/vol3.jpg",
                },
                {
                    "id": "vol-1",
                    "title": "Volume 1",
                    "number": 1,
                    "release_date": "2022-09-01",
                    "isbn": "9781234567890",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/vol1.jpg",
                },
                {
                    "id": "vol-2",
                    "title": "Volume 2",
                    "number": 2,
                    "release_date": "2022-10-01",
                    "isbn": "9781234567891",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 95,
                    "not_sold": False,
                    "image_url": "http://example.com/vol2.jpg",
                },
            ],
            "editions": [],
            "series": [],
            "types": [],
            "boxes": [],
            "box_editions": [],
            "box_volumes": [],
        }

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert result.volumes[0].id == "vol-3"
        assert result.volumes[1].id == "vol-1"
        assert result.volumes[2].id == "vol-2"

    def test_from_planning_v2_response_with_partial_data(self) -> None:
        """Test la conversion avec seulement certains types de données."""
        # Arrange
        response = {
            "volumes": [
                {
                    "id": "vol-1",
                    "title": "Volume 1",
                    "number": 1,
                    "release_date": "2022-09-01",
                    "isbn": "9781234567890",
                    "asin": None,
                    "edition_id": "ed-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "http://example.com/vol1.jpg",
                }
            ],
            "editions": [
                {
                    "id": "ed-1",
                    "title": "Edition 1",
                    "series_id": "series-1",
                    "publisher_id": "pub-1",
                    "volumes_count": 10,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 50,
                }
            ],
            # Pas de series, types, boxes, box_editions, box_volumes
        }

        # Act
        result = PlanningMapper.from_planning_v2_response(response)

        # Assert
        assert len(result.volumes) == 1
        assert len(result.editions) == 1
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0
