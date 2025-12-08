"""Tests unitaires pour JobMapper."""

import pytest

from src.application.dto.responses.job_responses import GetAllJobsV1Response
from src.application.mappers.job_mapper import JobMapper
from src.domain.entities.job import Job


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
        with pytest.raises(Exception):  # FrozenInstanceError
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
