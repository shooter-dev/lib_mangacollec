"""Tests pour APIEditionRepository.

This module contains unit tests for the API Edition repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import GetEditionByIdV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume
from mangacollec.domain.exceptions import EditionNotFoundException
from mangacollec.infrastructure.repositories import APIEditionRepository


class TestAPIEditionRepository:
    """Tests pour APIEditionRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIEditionRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIEditionRepository(mock_api_client)

    @pytest.fixture
    def sample_edition_data(self) -> dict:
        """Fixture pour créer des données d'édition de test."""
        return {
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

    @pytest.fixture
    def sample_publisher_data(self) -> dict:
        """Fixture pour créer des données d'éditeur de test."""
        return {
            "id": "publisher-789",
            "title": "Kana",
            "closed": False,
            "editions_count": 150,
            "no_amazon": False,
        }

    @pytest.fixture
    def sample_serie_data(self) -> dict:
        """Fixture pour créer des données de série de test."""
        return {
            "id": "series-456",
            "title": "Naruto",
            "type_id": "type-001",
            "adult_content": False,
            "editions_count": 7,
            "tasks_count": 1,
        }

    @pytest.fixture
    def sample_type_data(self) -> dict:
        """Fixture pour créer des données de type de test."""
        return {
            "id": "type-001",
            "title": "Manga",
            "to_display": True,
        }

    @pytest.fixture
    def sample_volume_data(self) -> dict:
        """Fixture pour créer des données de volume de test."""
        return {
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

    def test_get_edition_by_id_success(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_edition_data: dict,
        sample_publisher_data: dict,
        sample_serie_data: dict,
        sample_type_data: dict,
        sample_volume_data: dict,
    ) -> None:
        """Test de récupération d'une édition par ID avec toutes ses relations."""
        mock_api_client.get.return_value = {
            "editions": [sample_edition_data],
            "publishers": [sample_publisher_data],
            "series": [sample_serie_data],
            "types": [sample_type_data],
            "volumes": [sample_volume_data],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        # Vérifier que le retour est bien un GetEditionByIdV2Response
        assert isinstance(response, GetEditionByIdV2Response)

        # Vérifier les éditions
        assert len(response.editions) == 1
        assert isinstance(response.editions[0], Edition)
        assert response.editions[0].id == "edition-123"
        assert response.editions[0].title == "Edition Collector"
        assert response.editions[0].series_id == "series-456"
        assert response.editions[0].publisher_id == "publisher-789"
        assert response.editions[0].volumes_count == 72

        # Vérifier les publishers
        assert len(response.publishers) == 1
        assert isinstance(response.publishers[0], Publisher)
        assert response.publishers[0].id == "publisher-789"
        assert response.publishers[0].title == "Kana"
        assert response.publishers[0].closed is False

        # Vérifier les séries
        assert len(response.series) == 1
        assert isinstance(response.series[0], Serie)
        assert response.series[0].id == "series-456"
        assert response.series[0].title == "Naruto"

        # Vérifier les types
        assert len(response.types) == 1
        assert isinstance(response.types[0], TypeSerie)
        assert response.types[0].id == "type-001"
        assert response.types[0].title == "Manga"

        # Vérifier les volumes
        assert len(response.volumes) == 1
        assert isinstance(response.volumes[0], Volume)
        assert response.volumes[0].id == "volume-001"
        assert response.volumes[0].number == 1

        mock_api_client.get.assert_called_once_with("/v2/editions/edition-123")

    def test_get_edition_by_id_multiple_editions(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_edition_data: dict,
        sample_publisher_data: dict,
    ) -> None:
        """Test de récupération avec plusieurs éditions (parent et enfants)."""
        parent_edition = sample_edition_data.copy()
        child_edition = sample_edition_data.copy()
        child_edition["id"] = "edition-child"
        child_edition["parent_edition_id"] = "edition-123"
        child_edition["title"] = "Edition Deluxe"

        mock_api_client.get.return_value = {
            "editions": [parent_edition, child_edition],
            "publishers": [sample_publisher_data],
            "series": [],
            "types": [],
            "volumes": [],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.editions) == 2
        assert response.editions[0].id == "edition-123"
        assert response.editions[1].id == "edition-child"
        assert response.editions[1].parent_edition_id == "edition-123"

    def test_get_edition_by_id_not_found_empty_list(
        self, repository: APIEditionRepository, mock_api_client: Mock
    ) -> None:
        """Test de récupération d'une édition inexistante (liste vide)."""
        mock_api_client.get.return_value = {"editions": []}

        with pytest.raises(EditionNotFoundException) as exc_info:
            repository.get_edition_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_edition_by_id_not_found_no_editions_key(
        self, repository: APIEditionRepository, mock_api_client: Mock
    ) -> None:
        """Test de récupération sans clé 'editions' dans la réponse."""
        mock_api_client.get.return_value = {}

        with pytest.raises(EditionNotFoundException):
            repository.get_edition_by_id_v2("test-id")

    def test_get_edition_by_id_api_exception(self, repository: APIEditionRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(EditionNotFoundException):
            repository.get_edition_by_id_v2("test-id")

    def test_get_edition_by_id_empty_lists(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_edition_data: dict,
        sample_publisher_data: dict,
    ) -> None:
        """Test de récupération avec listes vides pour series, types et volumes."""
        mock_api_client.get.return_value = {
            "editions": [sample_edition_data],
            "publishers": [sample_publisher_data],
            "series": [],
            "types": [],
            "volumes": [],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.editions) == 1
        assert len(response.publishers) == 1
        assert isinstance(response.publishers[0], Publisher)
        assert response.series == []
        assert response.types == []
        assert response.volumes == []

    def test_get_edition_by_id_multiple_volumes(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_edition_data: dict,
        sample_publisher_data: dict,
        sample_volume_data: dict,
    ) -> None:
        """Test de récupération avec plusieurs volumes."""
        volume1 = sample_volume_data.copy()
        volume2 = sample_volume_data.copy()
        volume2["id"] = "volume-002"
        volume2["number"] = 2

        mock_api_client.get.return_value = {
            "editions": [sample_edition_data],
            "publishers": [sample_publisher_data],
            "series": [],
            "types": [],
            "volumes": [volume1, volume2],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.volumes) == 2
        assert response.volumes[0].number == 1
        assert response.volumes[1].number == 2

    def test_get_edition_by_id_without_title(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_publisher_data: dict,
    ) -> None:
        """Test de récupération d'une édition sans titre."""
        edition_data = {
            "id": "edition-123",
            "series_id": "series-456",
            "publisher_id": "publisher-789",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        mock_api_client.get.return_value = {
            "editions": [edition_data],
            "publishers": [sample_publisher_data],
            "series": [],
            "types": [],
            "volumes": [],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert response.editions[0].title is None

    def test_get_edition_by_id_commercial_stop(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_publisher_data: dict,
    ) -> None:
        """Test de récupération d'une édition avec arrêt commercial."""
        edition_data = {
            "id": "edition-123",
            "title": "Stopped Edition",
            "series_id": "series-456",
            "publisher_id": "publisher-789",
            "volumes_count": 10,
            "last_volume_number": 10,
            "commercial_stop": True,
            "not_finished": False,
            "follow_editions_count": 50,
        }

        mock_api_client.get.return_value = {
            "editions": [edition_data],
            "publishers": [sample_publisher_data],
            "series": [],
            "types": [],
            "volumes": [],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert response.editions[0].commercial_stop is True
        assert response.editions[0].not_finished is False

    def test_get_edition_by_id_multiple_series_and_types(
        self,
        repository: APIEditionRepository,
        mock_api_client: Mock,
        sample_edition_data: dict,
        sample_publisher_data: dict,
        sample_serie_data: dict,
        sample_type_data: dict,
    ) -> None:
        """Test de récupération avec plusieurs séries et types."""
        serie2 = sample_serie_data.copy()
        serie2["id"] = "series-789"
        serie2["title"] = "One Piece"
        serie2["type_id"] = "type-002"

        type2 = sample_type_data.copy()
        type2["id"] = "type-002"
        type2["title"] = "Manhwa"

        mock_api_client.get.return_value = {
            "editions": [sample_edition_data],
            "publishers": [sample_publisher_data],
            "series": [sample_serie_data, serie2],
            "types": [sample_type_data, type2],
            "volumes": [],
        }

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.series) == 2
        assert response.series[0].title == "Naruto"
        assert response.series[1].title == "One Piece"

        assert len(response.types) == 2
        assert response.types[0].title == "Manga"
        assert response.types[1].title == "Manhwa"
