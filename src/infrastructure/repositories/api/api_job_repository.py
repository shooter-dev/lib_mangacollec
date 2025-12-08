import requests
from typing import List

from src.application.dto.responses.job_responses import GetAllJobsV1Response
from src.application.mappers.job_mapper import JobMapper
from src.domain.entities.job import Job
from src.domain.repositories.i_job_repository import IJobRepository


class ApiJobRepository(IJobRepository):
    def __init__(self, base_url: str = "https://api.mangacollec.com"):
        self.base_url = base_url

    def get_all(self) -> GetAllJobsV1Response:
        response = requests.get(f"{self.base_url}/v1/jobs")
        response.raise_for_status()
        data = response.json()
        jobs = [JobMapper.to_entity(item) for item in data]
        return GetAllJobsV1Response(jobs=jobs)
