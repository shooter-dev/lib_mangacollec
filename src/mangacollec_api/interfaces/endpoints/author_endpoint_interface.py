from abc import ABC, abstractmethod
from typing import Dict, Any

from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient


class IAuthorsEndpoint(ABC):
    """
    Interface définissant les opérations disponibles pour les auteurs dans l'API MangaCollec.
    """

    def __init__(self, client: IMangaCollecAPIClient):
        """
        Initialise l'endpoint des auteurs.

        :param client: Client API MangaCollec
        """
        self.client = client

    @abstractmethod
    def get_all_authors(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec.

        :return: Liste des auteurs
        """
        pass

    @abstractmethod
    def get_author_by_id(self, author_id: str) -> Dict[str, Any]:
        """
        Récupère un auteur spécifique à partir de son ID.

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        pass

    @abstractmethod
    def get_all_authors_v2(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des auteurs disponibles sur MangaCollec (API v2).

        :return: Liste des auteurs
        """
        pass

    @abstractmethod
    def get_author_by_id_v2(self, author_id: str) -> Dict[str, Any]:
        """
        Récupère un auteur spécifique à partir de son ID (API v2).

        :param author_id: Identifiant de l'auteur
        :return: Détails de l'auteur
        """
        pass 