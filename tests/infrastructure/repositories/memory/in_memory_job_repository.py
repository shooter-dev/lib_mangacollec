from typing import List

from src.application.dto.responses.job_responses import GetAllJobsV1Response
from src.domain.entities.job import Job
from src.domain.repositories.i_job_repository import IJobRepository


class InMemoryJobRepository(IJobRepository):
    def __init__(self):
        self._jobs: List[Job] = []

    def get_all(self) -> GetAllJobsV1Response:
        return GetAllJobsV1Response(jobs=self._jobs)

    def add(self, job: Job):
        self._jobs.append(job)
