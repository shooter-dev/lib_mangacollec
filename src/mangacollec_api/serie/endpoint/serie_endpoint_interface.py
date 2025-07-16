from abc import ABC, abstractmethod
from typing import Dict, Any, List

from mangacollec_api.client.client_interface import IMangaCollecAPIClient
from mangacollec_api.serie.entity.serie import Serie
from mangacollec_api.serie.entity.serie_endpoint_entity import SerieEndpointEntity


class ISerieEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les séries dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des séries.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_all_series(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des séries disponibles sur MangaCollec.

        :return: Liste des séries
        """
        pass

    @abstractmethod
    def get_series_by_id(self, series_id: str) -> Dict[str, Any]:
        """
        Récupère une série spécifique à partir de son ID.

        :param series_id: Identifiant de la série
        :return: Détails de la série
        """
        pass

    @abstractmethod
    def get_all_series_v2(self) -> List[Serie]:
        """
        Récupère la liste complète des séries disponibles sur MangaCollec (API v2).

        :return: Liste des séries
        """
        pass

    @abstractmethod
    def get_series_by_id_v2(self, series_id: str) -> SerieEndpointEntity:
        """
        Récupère une série spécifique à partir de son ID (API v2).

        :param series_id: Identifiant de la série
        :return: Détails de la série
        """
        pass