from typing import List

from src.domain.entities.job import Job
from src.domain.repositories.i_job_repository import IJobRepository


class GetAllJobUseCase:
    def __init__(self, repository: IJobRepository):
        self.repository = repository

    def __call__(self) -> List[Job]:
        response = self.repository.get_all()
        return response.jobs
