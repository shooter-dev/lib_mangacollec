from abc import ABC, abstractmethod
from typing import Dict, Any

from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient


class IJobsEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les métiers dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des métiers.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_all_jobs(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des métiers disponibles sur MangaCollec.

        :return: Liste des métiers
        """
        pass
