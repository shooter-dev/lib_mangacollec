from typing import Dict, Any

from mangacollec_api.interfaces.endpoints.job_endpoint_interface import IJobsEndpoint


class JobsEndpoint(IJobsEndpoint):
    """
    Implémentation des opérations pour les métiers dans l'API MangaCollec.
    """

    def get_all_jobs(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des métiers disponibles sur MangaCollec.

        :return: Liste des métiers
        """
        return self.client.get("/v1/jobs")
