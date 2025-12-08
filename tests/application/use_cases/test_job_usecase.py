"""Tests unitaires pour les use cases Job."""

import pytest

from src.application.use_cases.job_usecase import GetAllJobsV1UseCase
from src.domain.entities.job import Job
from src.infrastructure.repositories.memory.inmemory_job_repository import InMemoryJobRepository


class TestGetAllJobsV1UseCase:
    """Tests pour GetAllJobsV1UseCase."""

    @pytest.fixture
    def job_repository(self):
        """Fixture pour créer un repository en mémoire."""
        return InMemoryJobRepository()

    @pytest.fixture
    def sample_jobs(self):
        """Fixture pour créer des jobs de test."""
        return [
            Job(id="1", title="Auteur"),
            Job(id="2", title="Dessinateur"),
        ]

    def test_get_all_jobs_success(self, job_repository, sample_jobs):
        """Test get_all avec succès."""
        # Arrange
        for job in sample_jobs:
            job_repository.add(job)
        use_case = GetAllJobsV1UseCase(job_repository)

        # Act
        result = use_case()

        # Assert
        assert len(result) == 2
        assert result[0] == sample_jobs[0]
        assert result[1] == sample_jobs[1]

    def test_get_all_jobs_empty(self, job_repository):
        """Test get_all avec un repository vide."""
        # Arrange
        use_case = GetAllJobsV1UseCase(job_repository)

        # Act
        result = use_case()

        # Assert
        assert len(result) == 0

    def test_get_all_jobs_returns_list(self, job_repository):
        """Test que get_all retourne une liste."""
        # Arrange
        use_case = GetAllJobsV1UseCase(job_repository)

        # Act
        result = use_case()

        # Assert
        assert isinstance(result, list)

    def test_get_all_jobs_with_single_job(self, job_repository):
        """Test get_all avec un seul job."""
        # Arrange
        job = Job(id="1", title="Auteur")
        job_repository.add(job)
        use_case = GetAllJobsV1UseCase(job_repository)

        # Act
        result = use_case()

        # Assert
        assert len(result) == 1
        assert result[0] == job
