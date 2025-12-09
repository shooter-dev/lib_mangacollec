"""Repositories interfaces."""

__all__ = [
    "IAuthorRepository",
    "IEditionRepository",
    "IPublisherRepository",
]

from mangacollec.domain.repositories.author_repository import IAuthorRepository
from mangacollec.domain.repositories.edition_repository import IEditionRepository
from mangacollec.domain.repositories.publisher_repository import IPublisherRepository
