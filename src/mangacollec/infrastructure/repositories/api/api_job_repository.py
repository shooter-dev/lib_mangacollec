"""Implémentation API du repository Job."""

from mangacollec.application.dto import GetAllJobsV1Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import JobMapper
from mangacollec.domain.repositories import IJobRepository


class APIJobRepository(IJobRepository):
    """Implémentation du repository Job via MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_all(self) -> GetAllJobsV1Response:
        """Récupère tous les jobs via l'API V1.

        Returns:
            GetAllJobsV1Response contenant la liste des jobs

        Raises:
            RuntimeError: Si la récupération échoue
        """
        try:
            response = self.client_api.get("/v1/jobs/")

            # ✅ CORRECT : Déléguer au mapper
            return JobMapper.from_all_jobs_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve jobs: {e}") from e
