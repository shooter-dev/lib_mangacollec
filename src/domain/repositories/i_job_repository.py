from abc import ABC, abstractmethod
from src.application.dto.responses.job_responses import GetAllJobsV1Response


class IJobRepository(ABC):
    @abstractmethod
    def get_all(self) -> GetAllJobsV1Response:
        pass
