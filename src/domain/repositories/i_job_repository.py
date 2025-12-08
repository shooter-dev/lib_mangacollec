"""Interface du repository pour Job."""

from abc import ABC, abstractmethod

from src.application.dto.responses.job_responses import GetAllJobsV1Response


class IJobRepository(ABC):
    """Interface du repository pour Job."""

    @abstractmethod
    def get_all(self) -> GetAllJobsV1Response:
        """Récupère tous les jobs via l'API.

        Returns:
            GetAllJobsV1Response contenant la liste des jobs
        """
        pass
