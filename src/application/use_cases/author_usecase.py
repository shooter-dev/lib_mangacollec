"""Use cases pour la ressource Author.

This module contains all use cases for Author operations.
"""

from src.application.dto.author_dto import SearchAuthor
from src.domain.entities import (Author, AuthorListItem, Edition, Job, Serie,
                                 Task, Volume)
from src.domain.repositories.author_repository import IAuthorRepository


class GetByIdAuthorUseCase:
    """Cas d'utilisation : récupérer un auteur par ID avec toutes ses relations."""

    def __init__(self, repository: IAuthorRepository) -> None:
        self.repository = repository

    def __call__(
        self, author_id: str
    ) -> (tuple)[Author, list[Task], list[Job], list[Serie], list[Edition], list[Volume]]:
        """Exécute le use case.

        Args:
            author_id: UUID de l'auteur

        Returns:
            Tuple contenant:
                - Author: L'auteur
                - list[Task]: Liste des tâches
                - list[Job]: Liste des rôles/métiers
                - list[Serie]: Liste des séries
                - list[Edition]: Liste des éditions
                - list[Volume]: Liste des volumes

        Raises:
            AuthorNotFoundException: Si l'auteur n'existe pas
        """
        response = self.repository.get_by_id_v2(author_id)
        return (
            response.authors[0],
            response.tasks,
            response.jobs,
            response.series,
            response.editions,
            response.volumes,
        )


class GetAllAuthorUseCase:
    """Cas d'utilisation : récupérer tous les auteurs."""

    def __init__(self, repository: IAuthorRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[Author]:
        """Exécute le use case.

        Returns:
            Liste des auteurs
        """
        response = self.repository.get_all_v2()
        return response.authors


class GetListAuthorUseCase:
    """Cas d'utilisation : récupérer la liste simplifiée des auteurs."""

    def __init__(self, repository: IAuthorRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[AuthorListItem]:
        """Exécute le use case.

        Returns:
            Liste des entités AuthorListItem (id + full_name)
        """
        return self.repository.get_list()


class SearchAuthorUseCase:
    """Cas d'utilisation : rechercher des auteurs avec des critères de filtrage."""

    def __call__(self, criteria: SearchAuthor, author_list: list[Author]) -> list[Author]:
        """Filtre une liste d'auteurs selon les critères métier spécifiés.

        Args:
            criteria: Critères de recherche utilisateur (name, first_name, min/max_tasks_count)
            author_list: Liste des auteurs à filtrer

        Returns:
            Liste des auteurs correspondant aux critères (liste vide si aucun résultat)

        Note:
            Pour rechercher par ID, utiliser GetByIdAuthorUseCase.
        """
        filtered_authors = []

        for author in author_list:
            if criteria.name and criteria.name.lower() not in author.name.lower():
                continue
            if criteria.first_name:
                if not author.first_name:
                    continue
                if criteria.first_name.lower() not in author.first_name.lower():
                    continue
            if criteria.min_tasks_count and author.tasks_count < criteria.min_tasks_count:
                continue
            if criteria.max_tasks_count and author.tasks_count > criteria.max_tasks_count:
                continue

            filtered_authors.append(author)

        return filtered_authors
