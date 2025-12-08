"""Implémentation en mémoire du repository Author pour les tests.

This module provides an in-memory implementation of the Author repository for testing.
"""

from src.application.dto.responses import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from src.application.mappers.author_mapper import AuthorMapper
from src.domain.entities import Author, AuthorListItem
from src.domain.execptions.author_exceptions import AuthorNotFoundException
from src.domain.repositories.author_repository import IAuthorRepository


class InMemoryAuthorRepository(IAuthorRepository):
    """Implémentation en mémoire du repository Author (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un dictionnaire vide."""
        self._data: dict[str, Author] = {}

    def get_by_id_v2(self, author_id: str) -> GetAuthorByIdV2Response:
        """Récupère un auteur par son ID avec toutes ses relations.

        Args:
            author_id: UUID de l'auteur

        Returns:
            GetAuthorByIdV2Response contenant:
                - authors: Liste des auteurs (1 seul élément)
                - tasks: Liste des tâches (vide pour InMemory)
                - jobs: Liste des rôles/métiers (vide pour InMemory)
                - series: Liste des séries (vide pour InMemory)
                - editions: Liste des éditions (vide pour InMemory)
                - volumes: Liste des volumes (vide pour InMemory)

        Raises:
            AuthorNotFoundException: Si l'auteur n'existe pas

        Note:
            Cette implémentation retourne des listes vides pour les relations.
            Pour les tests nécessitant des relations, utiliser le mock API repository.
        """
        author = self._data.get(author_id)
        if author is None:
            raise AuthorNotFoundException(author_id)
        # Retourner GetAuthorByIdV2Response avec des listes vides pour les relations
        return GetAuthorByIdV2Response(
            authors=[author],
            tasks=[],
            jobs=[],
            series=[],
            editions=[],
            volumes=[],
        )

    def get_all_v2(self) -> GetAllAuthorsV2Response:
        """Récupère tous les auteurs.

        Returns:
            GetAllAuthorsV2Response contenant la liste des auteurs
        """
        return GetAllAuthorsV2Response(authors=list(self._data.values()))

    def get_list(self) -> list[AuthorListItem]:
        """Récupère la liste simplifiée des auteurs (id + full_name).

        Returns:
            Liste des entités AuthorListItem
        """
        all_authors_response = self.get_all_v2()
        return [AuthorMapper.to_list_item(author) for author in all_authors_response.authors]

    def add(self, author: Author) -> Author:
        """Ajoute un auteur au repository (méthode pour les tests).

        Args:
            author: Entité Author à ajouter

        Returns:
            L'entité Author ajoutée
        """
        self._data[author.id] = author
        return author

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._data.clear()
