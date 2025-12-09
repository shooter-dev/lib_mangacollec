"""Interface du repository pour la ressource Author.

This module defines the repository interface for Author operations.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from mangacollec.domain.entities import AuthorListItem


class IAuthorRepository(ABC):
    """Interface du repository pour Author.

    Seules les opérations de lecture sont disponibles (pas de create/update/delete).
    """

    @abstractmethod
    def get_by_id_v2(self, author_id: str) -> GetAuthorByIdV2Response:
        """Récupère un auteur par son ID avec toutes ses relations.

        Args:
            author_id: UUID de l'auteur

        Returns:
            GetAuthorByIdV2Response contenant:
                - authors: Liste des auteurs (1 seul élément)
                - tasks: Liste des tâches
                - jobs: Liste des rôles/métiers
                - series: Liste des séries
                - editions: Liste des éditions
                - volumes: Liste des volumes

        Raises:
            AuthorNotFoundException: Si l'auteur n'existe pas
        """

    @abstractmethod
    def get_all_v2(self) -> GetAllAuthorsV2Response:
        """Récupère tous les auteurs avec leurs informations complètes.

        Returns:
            GetAllAuthorsV2Response contenant la liste des auteurs
        """

    @abstractmethod
    def get_list(self) -> list[AuthorListItem]:
        """Récupère la liste simplifiée des auteurs (id + full_name).

        Returns:
            Liste des entités AuthorListItem
        """
