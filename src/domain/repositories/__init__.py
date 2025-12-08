"""Repositories interfaces."""

__all__ = [
    "IAuthorRepository",
    "IEditionRepository",
    "IPublisherRepository",
]

from src.domain.repositories.author_repository import IAuthorRepository
from src.domain.repositories.edition_repository import IEditionRepository
from src.domain.repositories.publisher_repository import IPublisherRepository
