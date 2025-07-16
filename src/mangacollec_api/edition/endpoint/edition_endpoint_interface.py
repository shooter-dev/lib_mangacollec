from abc import ABC, abstractmethod
from typing import Dict

from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class IEditionEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les editions dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des editions.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_edition_by_id(self, edition_id: str) -> Dict:
        """
        Récupère les informations d'une edition spécifique en utilisant son ID.

        :param edition_id: Identifiant d'une edition
        :return: Détails de l'edition demandé.
        """
        pass

    @abstractmethod
    def get_edition_by_id_v2(self, edition_id) -> Dict:
        """
        Récupère les informations d'une edition spécifique en utilisant son ID.

        :param edition_id: Identifiant d'une edition
        :return: Détails de l'edition demandé.
        """
        pass
