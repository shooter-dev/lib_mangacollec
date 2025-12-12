"""Tests pour APIPlanningRepository.

This module contains unit tests for the API Planning repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         Serie, TypeSerie, Volume)
from mangacollec.infrastructure.repositories import APIPlanningRepository


class TestAPIPlanningRepository:
    """Tests pour APIPlanningRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIPlanningRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIPlanningRepository(mock_api_client)

    @pytest.fixture
    def sample_volume_data(self) -> dict:
        """Fixture pour créer des données de volume de test."""
        return {
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

    @pytest.fixture
    def sample_edition_data(self) -> dict:
        """Fixture pour créer des données d'édition de test."""
        return {
            "id": "ed-1",
            "title": "Edition 1",
            "series_id": "series-1",
            "publisher_id": "pub-1",
            "parent_edition_id": None,
            "volumes_count": 10,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 50,
        }

    @pytest.fixture
    def sample_serie_data(self) -> dict:
        """Fixture pour créer des données de série de test."""
        return {
            "id": "series-1",
            "title": "Serie 1",
            "type_id": "type-1",
            "adult_content": False,
            "editions_count": 5,
            "tasks_count": 2,
        }

    @pytest.fixture
    def sample_type_data(self) -> dict:
        """Fixture pour créer des données de type de test."""
        return {"id": "type-1", "title": "Manga", "to_display": True}

    @pytest.fixture
    def sample_box_data(self) -> dict:
        """Fixture pour créer des données de box de test."""
        return {
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

    @pytest.fixture
    def sample_box_edition_data(self) -> dict:
        """Fixture pour créer des données de box_edition de test."""
        return {
            "id": "be-1",
            "title": "Box Edition 1",
            "publisher_id": "pub-1",
            "boxes_count": 2,
            "adult_content": False,
            "box_follow_editions_count": 10,
        }

    @pytest.fixture
    def sample_box_volume_data(self) -> dict:
        """Fixture pour créer des données de box_volume de test."""
        return {
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

    def test_get_planning_v2_success(
        self,
        repository: APIPlanningRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
        sample_serie_data: dict,
        sample_type_data: dict,
        sample_box_data: dict,
        sample_box_edition_data: dict,
        sample_box_volume_data: dict,
    ) -> None:
        """Test de récupération du planning avec toutes les entités."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [sample_edition_data],
            "series": [sample_serie_data],
            "types": [sample_type_data],
            "boxes": [sample_box_data],
            "box_editions": [sample_box_edition_data],
            "box_volumes": [sample_box_volume_data],
        }

        response = repository.get_planning_v2("2022-09-30")

        # Vérifier que le retour est bien un GetPlanningV2Response
        assert isinstance(response, GetPlanningV2Response)

        # Vérifier les volumes
        assert len(response.volumes) == 1
        assert isinstance(response.volumes[0], Volume)
        assert response.volumes[0].id == "vol-1"
        assert response.volumes[0].title == "Volume 1"
        assert response.volumes[0].number == 1

        # Vérifier les éditions
        assert len(response.editions) == 1
        assert isinstance(response.editions[0], Edition)
        assert response.editions[0].id == "ed-1"
        assert response.editions[0].title == "Edition 1"

        # Vérifier les séries
        assert len(response.series) == 1
        assert isinstance(response.series[0], Serie)
        assert response.series[0].id == "series-1"
        assert response.series[0].title == "Serie 1"

        # Vérifier les types
        assert len(response.types) == 1
        assert isinstance(response.types[0], TypeSerie)
        assert response.types[0].id == "type-1"
        assert response.types[0].title == "Manga"

        # Vérifier les boxes
        assert len(response.boxes) == 1
        assert isinstance(response.boxes[0], Box)
        assert response.boxes[0].id == "box-1"
        assert response.boxes[0].title == "Box 1"

        # Vérifier les box_editions
        assert len(response.box_editions) == 1
        assert isinstance(response.box_editions[0], BoxEdition)
        assert response.box_editions[0].id == "be-1"

        # Vérifier les box_volumes
        assert len(response.box_volumes) == 1
        assert isinstance(response.box_volumes[0], BoxVolume)
        assert response.box_volumes[0].id == "bv-1"

        mock_api_client.get.assert_called_once_with("/v2/planning/?month=2022-09-30")

    def test_get_planning_v2_empty_response(self, repository: APIPlanningRepository, mock_api_client: Mock) -> None:
        """Test de récupération avec réponse vide."""
        mock_api_client.get.return_value = {}

        response = repository.get_planning_v2("2022-09-30")

        assert isinstance(response, GetPlanningV2Response)
        assert len(response.volumes) == 0
        assert len(response.editions) == 0
        assert len(response.series) == 0
        assert len(response.types) == 0
        assert len(response.boxes) == 0
        assert len(response.box_editions) == 0
        assert len(response.box_volumes) == 0

        mock_api_client.get.assert_called_once_with("/v2/planning/?month=2022-09-30")

    def test_get_planning_v2_empty_lists(self, repository: APIPlanningRepository, mock_api_client: Mock) -> None:
        """Test de récupération avec listes vides."""
        mock_api_client.get.return_value = {
            "volumes": [],
            "editions": [],
            "series": [],
            "types": [],
            "boxes": [],
            "box_editions": [],
            "box_volumes": [],
        }

        response = repository.get_planning_v2("2022-09-30")

        assert isinstance(response, GetPlanningV2Response)
        assert len(response.volumes) == 0
        assert len(response.editions) == 0
        assert len(response.series) == 0
        assert len(response.types) == 0
        assert len(response.boxes) == 0
        assert len(response.box_editions) == 0
        assert len(response.box_volumes) == 0

    def test_get_planning_v2_multiple_items(
        self,
        repository: APIPlanningRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
    ) -> None:
        """Test de récupération avec plusieurs items."""
        volume2 = sample_volume_data.copy()
        volume2["id"] = "vol-2"
        volume2["title"] = "Volume 2"
        volume2["number"] = 2

        edition2 = sample_edition_data.copy()
        edition2["id"] = "ed-2"
        edition2["title"] = "Edition 2"

        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data, volume2],
            "editions": [sample_edition_data, edition2],
            "series": [],
            "types": [],
            "boxes": [],
            "box_editions": [],
            "box_volumes": [],
        }

        response = repository.get_planning_v2("2022-09-30")

        assert len(response.volumes) == 2
        assert response.volumes[0].id == "vol-1"
        assert response.volumes[1].id == "vol-2"

        assert len(response.editions) == 2
        assert response.editions[0].id == "ed-1"
        assert response.editions[1].id == "ed-2"

    def test_get_planning_v2_different_months(
        self,
        repository: APIPlanningRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
    ) -> None:
        """Test de récupération pour différents mois."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [],
            "series": [],
            "types": [],
            "boxes": [],
            "box_editions": [],
            "box_volumes": [],
        }

        # Tester avec plusieurs dates
        response1 = repository.get_planning_v2("2022-09-30")
        response2 = repository.get_planning_v2("2022-10-31")

        assert isinstance(response1, GetPlanningV2Response)
        assert isinstance(response2, GetPlanningV2Response)

        # Vérifier que l'API a été appelée avec les bons paramètres
        calls = mock_api_client.get.call_args_list
        assert len(calls) == 2
        assert calls[0][0][0] == "/v2/planning/?month=2022-09-30"
        assert calls[1][0][0] == "/v2/planning/?month=2022-10-31"

    def test_get_planning_v2_api_exception(self, repository: APIPlanningRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(RuntimeError) as exc_info:
            repository.get_planning_v2("2022-09-30")

        assert "Failed to retrieve planning for month 2022-09-30" in str(exc_info.value)

    def test_get_planning_v2_partial_data(
        self,
        repository: APIPlanningRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
    ) -> None:
        """Test de récupération avec seulement certaines entités."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [sample_edition_data],
            # Pas de series, types, boxes, box_editions, box_volumes
        }

        response = repository.get_planning_v2("2022-09-30")

        assert isinstance(response, GetPlanningV2Response)
        assert len(response.volumes) == 1
        assert len(response.editions) == 1
        assert len(response.series) == 0
        assert len(response.types) == 0
        assert len(response.boxes) == 0
        assert len(response.box_editions) == 0
        assert len(response.box_volumes) == 0

    def test_get_planning_v2_only_boxes(
        self,
        repository: APIPlanningRepository,
        mock_api_client: Mock,
        sample_box_data: dict,
        sample_box_edition_data: dict,
        sample_box_volume_data: dict,
    ) -> None:
        """Test de récupération avec uniquement des boxes."""
        mock_api_client.get.return_value = {
            "volumes": [],
            "editions": [],
            "series": [],
            "types": [],
            "boxes": [sample_box_data],
            "box_editions": [sample_box_edition_data],
            "box_volumes": [sample_box_volume_data],
        }

        response = repository.get_planning_v2("2022-09-30")

        assert isinstance(response, GetPlanningV2Response)
        assert len(response.volumes) == 0
        assert len(response.editions) == 0
        assert len(response.boxes) == 1
        assert len(response.box_editions) == 1
        assert len(response.box_volumes) == 1
        assert response.boxes[0].id == "box-1"
