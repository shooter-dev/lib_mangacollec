from abc import ABC, abstractmethod
from typing import Dict, Any

from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class IKindEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les genres de mangas dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des genres.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_all_kinds(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des genres disponibles sur MangaCollec.

        :return: Liste des genres
        """
        pass

    @abstractmethod
    def get_all_kinds_v2(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des genres disponibles sur MangaCollec.

        :return: Liste des genres
        """
        pass
