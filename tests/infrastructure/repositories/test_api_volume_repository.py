"""Tests pour APIVolumeRepository.

This module contains unit tests for the API Volume repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.entities import (
    Box,
    BoxEdition,
    BoxVolume,
    Edition,
    Publisher,
    Serie,
    TypeSerie,
    Volume,
)
from mangacollec.domain.exceptions import VolumeNotFoundException
from mangacollec.infrastructure.repositories import APIVolumeRepository


class TestAPIVolumeRepository:
    """Tests pour APIVolumeRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIVolumeRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIVolumeRepository(mock_api_client)

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
            "nb_pages": 192,
            "content": "Chapitre 1...\nChapitre 2...",
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
    def sample_publisher_data(self) -> dict:
        """Fixture pour créer des données d'éditeur de test."""
        return {
            "id": "pub-1",
            "title": "Publisher 1",
            "closed": False,
            "editions_count": 100,
            "no_amazon": False,
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

    @pytest.fixture
    def sample_native_ad_data(self) -> dict:
        """Fixture pour créer des données de publicité native de test."""
        return {
            "id": "ad-1",
            "volume_id": "vol-1",
            "title": "Publicité Native",
            "start_date": "2022-09-01",
            "end_date": "2022-12-31",
        }

    # Tests pour get_by_id_v2

    def test_get_by_id_v2_success(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
        sample_publisher_data: dict,
        sample_serie_data: dict,
        sample_type_data: dict,
    ) -> None:
        """Test de récupération d'un volume par ID avec toutes ses relations."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [sample_edition_data],
            "publishers": [sample_publisher_data],
            "series": [sample_serie_data],
            "types": [sample_type_data],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        response = repository.get_by_id_v2("vol-1")

        # Vérifier que le retour est bien un GetVolumeByIdV2Response
        assert isinstance(response, GetVolumeByIdV2Response)

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

        # Vérifier les publishers
        assert len(response.publishers) == 1
        assert isinstance(response.publishers[0], Publisher)
        assert response.publishers[0].id == "pub-1"

        # Vérifier les séries
        assert len(response.series) == 1
        assert isinstance(response.series[0], Serie)
        assert response.series[0].id == "series-1"

        # Vérifier les types
        assert len(response.types) == 1
        assert isinstance(response.types[0], TypeSerie)
        assert response.types[0].id == "type-1"

        mock_api_client.get.assert_called_once_with("/v2/volumes/vol-1")

    def test_get_by_id_v2_not_found_empty_list(self, repository: APIVolumeRepository, mock_api_client: Mock) -> None:
        """Test de récupération d'un volume inexistant (liste vide)."""
        mock_api_client.get.return_value = {"volumes": []}

        with pytest.raises(VolumeNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        mock_api_client.get.assert_called_once_with("/v2/volumes/nonexistent-id")

    def test_get_by_id_v2_not_found_no_volumes_key(
        self, repository: APIVolumeRepository, mock_api_client: Mock
    ) -> None:
        """Test de récupération sans clé 'volumes' dans la réponse."""
        mock_api_client.get.return_value = {}

        with pytest.raises(VolumeNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        mock_api_client.get.assert_called_once_with("/v2/volumes/nonexistent-id")

    def test_get_by_id_v2_api_exception(self, repository: APIVolumeRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(VolumeNotFoundException) as exc_info:
            repository.get_by_id_v2("vol-1")

        assert "vol-1" in str(exc_info.value)
        mock_api_client.get.assert_called_once_with("/v2/volumes/vol-1")

    def test_get_by_id_v2_with_boxes(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_box_data: dict,
        sample_box_edition_data: dict,
        sample_box_volume_data: dict,
    ) -> None:
        """Test de récupération d'un volume avec des boxes associées."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [],
            "publishers": [],
            "series": [],
            "types": [],
            "box_volumes": [sample_box_volume_data],
            "boxes": [sample_box_data],
            "box_editions": [sample_box_edition_data],
        }

        response = repository.get_by_id_v2("vol-1")

        assert isinstance(response, GetVolumeByIdV2Response)
        assert len(response.volumes) == 1
        assert len(response.box_volumes) == 1
        assert isinstance(response.box_volumes[0], BoxVolume)
        assert len(response.boxes) == 1
        assert isinstance(response.boxes[0], Box)
        assert len(response.box_editions) == 1
        assert isinstance(response.box_editions[0], BoxEdition)

    def test_get_by_id_v2_without_optional_fields(self, repository: APIVolumeRepository, mock_api_client: Mock) -> None:
        """Test de récupération d'un volume avec des champs optionnels manquants."""
        volume_data_minimal = {
            "id": "vol-1",
            "number": 1,
            "edition_id": "ed-1",
            "not_sold": False,
        }
        mock_api_client.get.return_value = {"volumes": [volume_data_minimal]}

        response = repository.get_by_id_v2("vol-1")

        assert isinstance(response, GetVolumeByIdV2Response)
        volume = response.volumes[0]
        assert volume.id == "vol-1"
        assert volume.title is None
        assert volume.release_date is None
        assert volume.isbn is None
        assert volume.asin is None
        assert volume.possessions_count is None
        assert volume.image_url is None
        assert volume.nb_pages is None
        assert volume.content is None

    # Tests pour get_volumes_news_v2

    def test_get_volumes_news_v2_success(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
        sample_serie_data: dict,
        sample_type_data: dict,
        sample_native_ad_data: dict,
    ) -> None:
        """Test de récupération des volumes récents avec publicité native."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [sample_edition_data],
            "series": [sample_serie_data],
            "types": [sample_type_data],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
            "native_ad_volume_home_first": sample_native_ad_data,
        }

        response = repository.get_volumes_news_v2()

        # Vérifier que le retour est bien un GetVolumesNewsV2Response
        assert isinstance(response, GetVolumesNewsV2Response)

        # Vérifier les volumes
        assert len(response.volumes) == 1
        assert isinstance(response.volumes[0], Volume)
        assert response.volumes[0].id == "vol-1"

        # Vérifier les autres entités
        assert len(response.editions) == 1
        assert len(response.series) == 1
        assert len(response.types) == 1

        # Vérifier la publicité native
        assert response.native_ad_volume_home_first is not None
        assert response.native_ad_volume_home_first.id == "ad-1"

        mock_api_client.get.assert_called_once_with("/v2/volumes/news")

    def test_get_volumes_news_v2_without_native_ad(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
    ) -> None:
        """Test de récupération des volumes récents sans publicité native."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
            # Pas de native_ad_volume_home_first
        }

        response = repository.get_volumes_news_v2()

        assert isinstance(response, GetVolumesNewsV2Response)
        assert len(response.volumes) == 1
        assert response.native_ad_volume_home_first is None

        mock_api_client.get.assert_called_once_with("/v2/volumes/news")

    def test_get_volumes_news_v2_empty_response(self, repository: APIVolumeRepository, mock_api_client: Mock) -> None:
        """Test de récupération des volumes récents avec réponse vide."""
        mock_api_client.get.return_value = {
            "volumes": [],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        response = repository.get_volumes_news_v2()

        assert isinstance(response, GetVolumesNewsV2Response)
        assert len(response.volumes) == 0
        assert len(response.editions) == 0
        assert len(response.series) == 0
        assert len(response.types) == 0
        assert len(response.box_volumes) == 0
        assert len(response.boxes) == 0
        assert len(response.box_editions) == 0
        assert response.native_ad_volume_home_first is None

        mock_api_client.get.assert_called_once_with("/v2/volumes/news")

    def test_get_volumes_news_v2_multiple_items(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_edition_data: dict,
    ) -> None:
        """Test de récupération des volumes récents avec plusieurs items."""
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
            "box_volumes": [],
            "boxes": [],
            "box_editions": [],
        }

        response = repository.get_volumes_news_v2()

        assert len(response.volumes) == 2
        assert response.volumes[0].id == "vol-1"
        assert response.volumes[1].id == "vol-2"

        assert len(response.editions) == 2
        assert response.editions[0].id == "ed-1"
        assert response.editions[1].id == "ed-2"

    def test_get_volumes_news_v2_api_exception(self, repository: APIVolumeRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API pour get_volumes_news_v2."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(RuntimeError) as exc_info:
            repository.get_volumes_news_v2()

        assert "Failed to retrieve volumes news" in str(exc_info.value)
        assert "API Error" in str(exc_info.value)

        mock_api_client.get.assert_called_once_with("/v2/volumes/news")

    def test_get_volumes_news_v2_with_boxes(
        self,
        repository: APIVolumeRepository,
        mock_api_client: Mock,
        sample_volume_data: dict,
        sample_box_data: dict,
        sample_box_edition_data: dict,
        sample_box_volume_data: dict,
    ) -> None:
        """Test de récupération des volumes récents avec des boxes."""
        mock_api_client.get.return_value = {
            "volumes": [sample_volume_data],
            "editions": [],
            "series": [],
            "types": [],
            "box_volumes": [sample_box_volume_data],
            "boxes": [sample_box_data],
            "box_editions": [sample_box_edition_data],
        }

        response = repository.get_volumes_news_v2()

        assert isinstance(response, GetVolumesNewsV2Response)
        assert len(response.volumes) == 1
        assert len(response.box_volumes) == 1
        assert len(response.boxes) == 1
        assert len(response.box_editions) == 1

        # Vérifier les types des entités de box
        assert isinstance(response.box_volumes[0], BoxVolume)
        assert isinstance(response.boxes[0], Box)
        assert isinstance(response.box_editions[0], BoxEdition)
