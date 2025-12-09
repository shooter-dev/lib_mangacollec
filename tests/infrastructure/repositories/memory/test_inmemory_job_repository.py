"""Tests unitaires pour InMemoryJobRepository."""

import pytest

from mangacollec.application.dto.responses.job_responses import GetAllJobsV1Response
from mangacollec.domain.entities import Job
from mangacollec.infrastructure.repositories.memory.inmemory_job_repository import \
    InMemoryJobRepository


class TestInMemoryJobRepository:
    """Tests pour InMemoryJobRepository."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository."""
        return InMemoryJobRepository()

    @pytest.fixture
    def sample_jobs(self):
        """Fixture pour créer des jobs de test."""
        return [
            Job(id="1", title="Auteur"),
            Job(id="2", title="Dessinateur"),
            Job(id="3", title="Scénariste"),
        ]

    def test_get_all_empty(self, repository):
        """Test get_all quand le repository est vide."""
        # Act
        result = repository.get_all()

        # Assert
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 0

    def test_get_all_with_jobs(self, repository, sample_jobs):
        """Test get_all avec des jobs."""
        # Arrange
        for job in sample_jobs:
            repository.add(job)

        # Act
        result = repository.get_all()

        # Assert
        assert isinstance(result, GetAllJobsV1Response)
        assert len(result.jobs) == 3
        assert all(isinstance(job, Job) for job in result.jobs)

    def test_add_job(self, repository):
        """Test l'ajout d'un job."""
        # Arrange
        job = Job(id="1", title="Test")

        # Act
        repository.add(job)
        result = repository.get_all()

        # Assert
        assert len(result.jobs) == 1
        assert result.jobs[0] == job

    def test_add_multiple_jobs(self, repository, sample_jobs):
        """Test l'ajout de plusieurs jobs."""
        # Act
        for job in sample_jobs:
            repository.add(job)
        result = repository.get_all()

        # Assert
        assert len(result.jobs) == 3

    def test_add_duplicate_id_overwrites(self, repository):
        """Test que l'ajout d'un job avec un ID existant écrase l'ancien."""
        # Arrange
        job1 = Job(id="1", title="First")
        job2 = Job(id="1", title="Second")

        # Act
        repository.add(job1)
        repository.add(job2)
        result = repository.get_all()

        # Assert
        assert len(result.jobs) == 1
        assert result.jobs[0].title == "Second"

    def test_clear(self, repository, sample_jobs):
        """Test la méthode clear."""
        # Arrange
        for job in sample_jobs:
            repository.add(job)
        assert len(repository.get_all().jobs) == 3

        # Act
        repository.clear()
        result = repository.get_all()

        # Assert
        assert len(result.jobs) == 0

    def test_clear_empty_repository(self, repository):
        """Test clear sur un repository déjà vide."""
        # Act
        repository.clear()
        result = repository.get_all()

        # Assert
        assert len(result.jobs) == 0
