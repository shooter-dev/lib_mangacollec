"""Tests unitaires pour JobMapper."""

from dataclasses import FrozenInstanceError

import pytest

from mangacollec.application.dto import GetAllJobsV1Response
from mangacollec.application.mappers import JobMapper
from mangacollec.domain.entities import Job


class TestJobMapperFromDict:
    """Tests pour la méthode from_dict."""

    def test_from_dict_with_valid_data(self):
        """Test la conversion d'un dict valide en Job."""
        # Arrange
        data = {"id": "dc7b6062-6aae-49ee-87a2-95d47ab52600", "title": "Auteur"}

        # Act
        job = JobMapper.from_dict(data)

        # Assert
        assert isinstance(job, Job)
        assert job.id == "dc7b6062-6aae-49ee-87a2-95d47ab52600"
        assert job.title == "Auteur"

    def test_from_dict_immutability(self):
        """Test que l'entité Job créée est immuable."""
        # Arrange
        data = {"id": "1", "title": "Test"}

        # Act
        job = JobMapper.from_dict(data)

        # Assert
        with pytest.raises(FrozenInstanceError):
            job.id = "2"


class TestJobMapperToDict:
    """Tests pour la méthode to_dict."""

    def test_to_dict_with_valid_job(self):
        """Test la conversion d'un Job en dictionnaire."""
        # Arrange
        job = Job(id="dc7b6062-6aae-49ee-87a2-95d47ab52600", title="Auteur")

        # Act
        result = JobMapper.to_dict(job)

        # Assert
        assert isinstance(result, dict)
        assert result["id"] == "dc7b6062-6aae-49ee-87a2-95d47ab52600"
        assert result["title"] == "Auteur"

    def test_to_dict_contains_all_fields(self):
        """Test que to_dict retourne tous les champs."""
        # Arrange
        job = Job(id="1", title="Test")

        # Act
        result = JobMapper.to_dict(job)

        # Assert
        assert len(result) == 2
        assert "id" in result
        assert "title" in result


class TestJobMapperFromAllJobsResponse:
    """Tests pour la méthode from_all_jobs_response."""

    def test_from_all_jobs_response_with_valid_data(self):
        """Test la conversion d'une réponse API en GetAllJobsV1Response."""
        # Arrange
        response = [
            {"id": "dc7b6062-6aae-49ee-87a2-95d47ab52600", "title": "Auteur"},
            {"id": "88bb716c-1bcc-4b78-8c98-10a738e2fbbc", "title": "Auteur original"},
        ]

        # Act
        result = JobMapper.from_all_jobs_response(response)

        # Assert
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 2
        assert result.jobs[0].id == "dc7b6062-6aae-49ee-87a2-95d47ab52600"
        assert result.jobs[0].title == "Auteur"
        assert result.jobs[1].id == "88bb716c-1bcc-4b78-8c98-10a738e2fbbc"
        assert result.jobs[1].title == "Auteur original"

    def test_from_all_jobs_response_with_empty_list(self):
        """Test la conversion d'une liste vide."""
        # Arrange
        response = []

        # Act
        result = JobMapper.from_all_jobs_response(response)

        # Assert
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 0

    def test_from_all_jobs_response_preserves_order(self):
        """Test que l'ordre des jobs est préservé."""
        # Arrange
        response = [
            {"id": "1", "title": "First"},
            {"id": "2", "title": "Second"},
            {"id": "3", "title": "Third"},
        ]

        # Act
        result = JobMapper.from_all_jobs_response(response)

        # Assert
        assert result.jobs[0].title == "First"
        assert result.jobs[1].title == "Second"
        assert result.jobs[2].title == "Third"


class TestJobMapperErrorHandling:
    """Tests pour la gestion des erreurs dans le mapper."""

    def test_from_dict_with_missing_id(self):
        """Test from_dict avec un ID manquant."""
        # Arrange
        data = {"title": "Auteur"}  # ID manquant

        # Act & Assert
        with pytest.raises(KeyError, match="id"):
            JobMapper.from_dict(data)

    def test_from_dict_with_missing_title(self):
        """Test from_dict avec un title manquant."""
        # Arrange
        data = {"id": "1"}  # title manquant

        # Act & Assert
        with pytest.raises(KeyError, match="title"):
            JobMapper.from_dict(data)

    def test_from_dict_with_empty_data(self):
        """Test from_dict avec un dictionnaire vide."""
        # Arrange
        data = {}

        # Act & Assert
        with pytest.raises(KeyError):
            JobMapper.from_dict(data)

    def test_from_dict_with_invalid_data_type(self):
        """Test from_dict avec un type de données invalide."""
        # Arrange
        data = "invalid_data"

        # Act & Assert
        with pytest.raises(TypeError):
            JobMapper.from_dict(data)  # type: ignore

    def test_to_dict_with_none(self):
        """Test to_dict avec None."""
        # Arrange
        job = None

        # Act & Assert
        with pytest.raises(TypeError):
            JobMapper.to_dict(job)  # type: ignore

    def test_from_all_jobs_response_with_invalid_type(self):
        """Test from_all_jobs_response avec un type invalide."""
        # Arrange
        response = "not_a_list"

        # Act & Assert
        with pytest.raises(TypeError):
            JobMapper.from_all_jobs_response(response)  # type: ignore

    def test_from_all_jobs_response_with_invalid_item_type(self):
        """Test from_all_jobs_response avec des éléments invalides."""
        # Arrange
        response = [{"id": "1"}, {"not_a_dict": "invalid"}]

        # Act & Assert
        with pytest.raises(KeyError, match="title"):
            JobMapper.from_all_jobs_response(response)

    def test_from_all_jobs_response_with_none_item(self):
        """Test from_all_jobs_response avec un élément None."""
        # Arrange
        response = [{"id": "1", "title": "Test"}, None]

        # Act & Assert
        with pytest.raises(TypeError):
            JobMapper.from_all_jobs_response(response)  # type: ignore
