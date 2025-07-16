from abc import ABC, abstractmethod
from typing import Dict, Any

from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class IPublisherEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les publishers dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des publishers.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_all_publishers(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des publishers disponibles sur MangaCollec.

        :return: Liste des publishers
        """
        pass

    @abstractmethod
    def get_all_publishers_v2(self) -> Dict[str, Any]:
        """
        Récupère une liste complète des publishers disponibles sur MangaCollec.

        :return: Liste des publishers
        """
        pass

    @abstractmethod
    def get_publisher_by_id(self, publishers_id: str) -> Dict[str, Any]:
        """
        Récupère une publisher spécifique à partir de son ID.

        :param publishers_id: Identifiant de la publisher
        :return: Détails de la publisher
        """
        pass

    @abstractmethod
    def get_publisher_by_id_v2(self, publishers_id: str) -> Dict[str, Any]:
        """
        Récupère un publisher spécifique à partir de son ID.

        :param publishers_id: Identifiant de la publisher
        :return: Détails du publisher
        """
        pass