"""Tests pour APISerieRepository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.application.dto import (GetAllSeriesV2Response,
                                         GetSerieByIdV2Response)
from mangacollec.domain.exceptions import SerieNotFoundException
from mangacollec.infrastructure.repositories import APISerieRepository


class TestAPISerieRepository:
    """Tests pour APISerieRepository."""

    @pytest.fixture
    def mock_client_api(self):
        """Fixture pour créer un mock du client API."""
        return MagicMock()

    @pytest.fixture
    def repository(self, mock_client_api):
        """Fixture pour créer le repository avec un mock."""
        return APISerieRepository(mock_client_api)

    def test_get_serie_by_id_v2_success(self, repository, mock_client_api):
        """Test de récupération d'une série via l'API."""
        mock_response = {
            "series": [
                {
                    "id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 12,
                    "tasks_count": 5,
                    "kinds_ids": ["kind-1"],
                }
            ],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
            "kinds": [{"id": "kind-1", "name": "Shonen", "name_en": "Shonen"}],
            "tasks": [],
            "jobs": [],
            "authors": [],
            "editions": [],
            "publishers": [],
            "volumes": [],
            "box_editions": [],
            "boxes": [],
            "box_volumes": [],
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_serie_by_id_v2("39c0f48b-c9f3-488d-9f01-bb9f21f30b0e")

        mock_client_api.get.assert_called_once_with("/v2/series/39c0f48b-c9f3-488d-9f01-bb9f21f30b0e")
        assert isinstance(response, GetSerieByIdV2Response)
        assert len(response.series) == 1
        assert response.series[0].id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert response.series[0].title == "Naruto"
        assert response.series[0].kinds_ids == ["kind-1"]
        assert len(response.types) == 1
        assert len(response.kinds) == 1

    def test_get_serie_by_id_v2_not_found_empty_list(self, repository, mock_client_api):
        """Test de récupération d'une série inexistante (liste vide)."""
        mock_response = {
            "series": [],
            "types": [],
            "kinds": [],
            "tasks": [],
            "jobs": [],
            "authors": [],
            "editions": [],
            "publishers": [],
            "volumes": [],
            "box_editions": [],
            "boxes": [],
            "box_volumes": [],
        }
        mock_client_api.get.return_value = mock_response

        with pytest.raises(SerieNotFoundException) as exc_info:
            repository.get_serie_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_serie_by_id_v2_not_found_no_key(self, repository, mock_client_api):
        """Test de récupération d'une série inexistante (pas de clé 'series')."""
        mock_response = {}
        mock_client_api.get.return_value = mock_response

        with pytest.raises(SerieNotFoundException) as exc_info:
            repository.get_serie_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_serie_by_id_v2_api_error(self, repository, mock_client_api):
        """Test de récupération d'une série avec erreur API."""
        mock_client_api.get.side_effect = Exception("API Error")

        with pytest.raises(SerieNotFoundException) as exc_info:
            repository.get_serie_by_id_v2("serie-id")

        assert "serie-id" in str(exc_info.value)

    def test_get_all_series_v2_success(self, repository, mock_client_api):
        """Test de récupération de toutes les séries via l'API."""
        mock_response = {
            "series": [
                {
                    "id": "1",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 12,
                    "tasks_count": 5,
                    "kinds_ids": ["kind-1"],
                },
                {
                    "id": "2",
                    "title": "One Piece",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 25,
                    "tasks_count": 3,
                },
            ],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_all_series_v2()

        mock_client_api.get.assert_called_once_with("/v2/series/")
        assert isinstance(response, GetAllSeriesV2Response)
        assert len(response.series) == 2
        assert response.series[0].title == "Naruto"
        assert response.series[0].kinds_ids == ["kind-1"]
        assert response.series[1].title == "One Piece"
        assert response.series[1].kinds_ids is None
        assert len(response.types) == 1

    def test_get_all_series_v2_empty(self, repository, mock_client_api):
        """Test de récupération avec liste vide."""
        mock_response = {"series": [], "types": []}
        mock_client_api.get.return_value = mock_response

        response = repository.get_all_series_v2()

        assert isinstance(response, GetAllSeriesV2Response)
        assert len(response.series) == 0
        assert len(response.types) == 0

    def test_get_all_series_v2_api_error(self, repository, mock_client_api):
        """Test de récupération avec erreur API."""
        mock_client_api.get.side_effect = Exception("API Error")

        with pytest.raises(RuntimeError) as exc_info:
            repository.get_all_series_v2()

        assert "Failed to retrieve series" in str(exc_info.value)
