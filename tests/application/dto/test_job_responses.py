"""Tests unitaires pour les DTOs de réponse Job."""

import pytest

from mangacollec.application.dto import GetAllJobsV1Response
from mangacollec.domain.entities import Job


class TestGetAllJobsV1Response:
    """Tests pour GetAllJobsV1Response."""

    def test_response_creation_with_jobs(self):
        """Test la création d'une réponse avec des jobs."""
        # Arrange
        jobs = [
            Job(id="1", title="Auteur"),
            Job(id="2", title="Dessinateur"),
        ]

        # Act
        response = GetAllJobsV1Response(jobs=jobs)

        # Assert
        assert response.jobs == jobs
        assert len(response.jobs) == 2

    def test_response_creation_empty(self):
        """Test la création d'une réponse vide."""
        # Act
        response = GetAllJobsV1Response(jobs=[])

        # Assert
        assert response.jobs == []
        assert len(response.jobs) == 0

    def test_response_immutability(self):
        """Test que la réponse est immuable."""
        # Arrange
        jobs = [Job(id="1", title="Auteur")]
        response = GetAllJobsV1Response(jobs=jobs)

        # Act & Assert
        with pytest.raises(Exception):  # FrozenInstanceError
            response.jobs = []

    def test_response_preserves_job_order(self):
        """Test que l'ordre des jobs est préservé."""
        # Arrange
        jobs = [
            Job(id="1", title="First"),
            Job(id="2", title="Second"),
            Job(id="3", title="Third"),
        ]

        # Act
        response = GetAllJobsV1Response(jobs=jobs)

        # Assert
        assert response.jobs[0].title == "First"
        assert response.jobs[1].title == "Second"
        assert response.jobs[2].title == "Third"
