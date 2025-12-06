"""Implémentation du repository Author via l'API MangaCollec.

This module provides the API implementation of the Author repository.
"""

from src.application.dto.responses import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from src.application.interfaces.mangacollec_api_interface import IMangaCollecAPI
from src.application.mappers.author_mapper import AuthorMapper
from src.domain.entities import AuthorListItem
from src.domain.execptions.author_exceptions import AuthorNotFoundException
from src.domain.repositories.author_repository import IAuthorRepository


class APIAuthorRepository(IAuthorRepository):
    """Implémentation du repository Author via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_by_id_v2(self, author_id: str) -> GetAuthorByIdV2Response:
        """Récupère un auteur par son ID avec toutes ses relations via l'API.

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
        try:
            response = self.client_api.get(f"/v2/authors/{author_id}")

            if not response.get("authors") or len(response["authors"]) == 0:
                raise AuthorNotFoundException(author_id)

            # Utiliser le mapper pour convertir toute la réponse API
            return AuthorMapper.from_api_response(response)

        except Exception as e:
            if isinstance(e, AuthorNotFoundException):
                raise
            raise AuthorNotFoundException(author_id) from e

    def get_all_v2(self) -> GetAllAuthorsV2Response:
        """Récupère tous les auteurs via l'API.

        Returns:
            GetAllAuthorsV2Response contenant la liste des auteurs
        """
        try:
            response = self.client_api.get("/v2/authors/")
            return AuthorMapper.from_all_authors_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve authors: {e}") from e

    def get_list(self) -> list[AuthorListItem]:
        """Récupère la liste simplifiée des auteurs (id + full_name).

        Returns:
            Liste des entités AuthorListItem
        """
        all_authors_response = self.get_all_v2()
        return [AuthorMapper.to_list_item(author) for author in all_authors_response.authors]
