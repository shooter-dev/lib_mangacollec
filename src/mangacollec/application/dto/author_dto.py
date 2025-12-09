"""DTOs pour la ressource Author.

This module contains Data Transfer Objects for Author operations.
"""

from dataclasses import dataclass


@dataclass
class SearchAuthor:
    """DTO pour la recherche d'auteurs par critères métier.

    Tous les champs sont optionnels pour permettre des filtres flexibles.

    Note:
        Pour rechercher par ID (technique), utiliser GetByIdAuthorUseCase.
        SearchAuthor est destiné aux recherches utilisateur (nom, prénom, etc.).
    """

    name: str | None = None
    first_name: str | None = None
    min_tasks_count: int | None = None
    max_tasks_count: int | None = None
