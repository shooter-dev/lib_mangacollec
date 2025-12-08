import pytest

from src.application.use_cases.job_usecase import GetAllJobUseCase
from src.domain.entities.job import Job
from tests.infrastructure.repositories.memory.in_memory_job_repository import InMemoryJobRepository


@pytest.fixture
def job_repository():
    return InMemoryJobRepository()


def test_get_all_jobs(job_repository):
    # Arrange
    job1 = Job(id="1", title="Author")
    job2 = Job(id="2", title="Illustrator")
    job_repository.add(job1)
    job_repository.add(job2)

    use_case = GetAllJobUseCase(job_repository)

    # Act
    result = use_case()

    # Assert
    assert len(result) == 2
    assert result[0] == job1
    assert result[1] == job2
