from dataclasses import dataclass
from typing import List

from src.domain.entities.job import Job


@dataclass(frozen=True)
class GetAllJobsV1Response:
    jobs: List[Job]
