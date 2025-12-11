"""Tests unitaires pour APIKindRepository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.application.dto import (GetAllKindsV1Response,
                                         GetAllKindsV2Response)
from mangacollec.domain.entities import Kind
from mangacollec.infrastructure.repositories.api.api_kind_repository import \
    APIKindRepository


class TestAPIKindRepository:
    """Tests pour APIKindRepository."""

    @pytest.fixture
    def mock_api_client(self):
        """Fixture pour créer un mock du client API."""
        return MagicMock()

    @pytest.fixture
    def repository(self, mock_api_client):
        """Fixture pour créer un repository avec un client mock."""
        return APIKindRepository(client_api=mock_api_client)

    @pytest.fixture
    def sample_kinds_data(self):
        """Fixture pour des données de kinds."""
        return [
            {"id": "1", "name": "Manga", "name_en": "Manga"},
            {"id": "2", "name": "Comics", "name_en": "Comics"},
        ]

    # Tests pour get_all_kinds_v1

    def test_get_all_kinds_v1_success(self, repository, mock_api_client, sample_kinds_data):
        """Test get_all_kinds_v1 avec succès."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": sample_kinds_data}

        # Act
        result = repository.get_all_kinds_v1()

        # Assert
        mock_api_client.get.assert_called_once_with("/v1/kinds")
        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 2
        assert isinstance(result.kinds[0], Kind)
        assert result.kinds[0].id == "1"
        assert result.kinds[0].name == "Manga"

    def test_get_all_kinds_v1_empty_response(self, repository, mock_api_client):
        """Test get_all_kinds_v1 avec une réponse vide."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": []}

        # Act
        result = repository.get_all_kinds_v1()

        # Assert
        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 0

    def test_get_all_kinds_v1_raises_error_on_api_failure(self, repository, mock_api_client):
        """Test get_all_kinds_v1 lève une erreur si l'API échoue."""
        # Arrange
        mock_api_client.get.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(RuntimeError, match="Failed to retrieve kinds from V1 API"):
            repository.get_all_kinds_v1()

    def test_get_all_kinds_v1_uses_correct_endpoint(self, repository, mock_api_client):
        """Test que get_all_kinds_v1 utilise le bon endpoint."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": []}

        # Act
        repository.get_all_kinds_v1()

        # Assert
        mock_api_client.get.assert_called_once_with("/v1/kinds")

    # Tests pour get_all_kinds_v2

    def test_get_all_kinds_v2_success(self, repository, mock_api_client, sample_kinds_data):
        """Test get_all_kinds_v2 avec succès."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": sample_kinds_data}

        # Act
        result = repository.get_all_kinds_v2()

        # Assert
        mock_api_client.get.assert_called_once_with("/v2/kinds/")
        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 2
        assert isinstance(result.kinds[0], Kind)
        assert result.kinds[0].id == "1"
        assert result.kinds[0].name == "Manga"

    def test_get_all_kinds_v2_empty_response(self, repository, mock_api_client):
        """Test get_all_kinds_v2 avec une réponse vide."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": []}

        # Act
        result = repository.get_all_kinds_v2()

        # Assert
        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 0

    def test_get_all_kinds_v2_raises_error_on_api_failure(self, repository, mock_api_client):
        """Test get_all_kinds_v2 lève une erreur si l'API échoue."""
        # Arrange
        mock_api_client.get.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(RuntimeError, match="Failed to retrieve kinds from V2 API"):
            repository.get_all_kinds_v2()

    def test_get_all_kinds_v2_uses_correct_endpoint(self, repository, mock_api_client):
        """Test que get_all_kinds_v2 utilise le bon endpoint."""
        # Arrange
        mock_api_client.get.return_value = {"kinds": []}

        # Act
        repository.get_all_kinds_v2()

        # Assert
        mock_api_client.get.assert_called_once_with("/v2/kinds/")
