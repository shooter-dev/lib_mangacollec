from typing import List

from mangacollec.application.dto.job_responses import GetAllJobsV1Response
from mangacollec.domain.entities import Job
from mangacollec.domain.repositories.job_repository_interface import \
    IJobRepository


class InMemoryJobRepository(IJobRepository):
    def __init__(self):
        self._jobs: List[Job] = []

    def get_all(self) -> GetAllJobsV1Response:
        return GetAllJobsV1Response(jobs=self._jobs)

    def add(self, job: Job):
        self._jobs.append(job)
