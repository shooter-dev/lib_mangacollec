"""Tests unitaires pour APIJobRepository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.application.dto.responses.job_responses import GetAllJobsV1Response
from mangacollec.domain.entities import Job
from mangacollec.infrastructure.repositories.api.api_job_repository import \
    APIJobRepository


class TestAPIJobRepository:
    """Tests pour APIJobRepository."""

    @pytest.fixture
    def mock_api_client(self):
        """Fixture pour créer un mock du client API."""
        return MagicMock()

    @pytest.fixture
    def repository(self, mock_api_client):
        """Fixture pour créer un repository avec un client mock."""
        return APIJobRepository(client_api=mock_api_client)

    def test_get_all_success(self, repository, mock_api_client):
        """Test get_all avec succès."""
        # Arrange
        mock_api_client.get.return_value = [
            {"id": "dc7b6062-6aae-49ee-87a2-95d47ab52600", "title": "Auteur"},
            {"id": "88bb716c-1bcc-4b78-8c98-10a738e2fbbc", "title": "Auteur original"},
        ]

        # Act
        result = repository.get_all()

        # Assert
        mock_api_client.get.assert_called_once_with("/v1/jobs/")
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 2
        assert isinstance(result.jobs[0], Job)
        assert result.jobs[0].id == "dc7b6062-6aae-49ee-87a2-95d47ab52600"
        assert result.jobs[0].title == "Auteur"

    def test_get_all_empty_response(self, repository, mock_api_client):
        """Test get_all avec une réponse vide."""
        # Arrange
        mock_api_client.get.return_value = []

        # Act
        result = repository.get_all()

        # Assert
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 0

    def test_get_all_raises_error_on_api_failure(self, repository, mock_api_client):
        """Test get_all lève une erreur si l'API échoue."""
        # Arrange
        mock_api_client.get.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(RuntimeError, match="Failed to retrieve jobs"):
            repository.get_all()

    def test_get_all_uses_correct_endpoint(self, repository, mock_api_client):
        """Test que get_all utilise le bon endpoint."""
        # Arrange
        mock_api_client.get.return_value = []

        # Act
        repository.get_all()

        # Assert
        mock_api_client.get.assert_called_once_with("/v1/jobs/")
