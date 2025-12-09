"""API repositories."""

__all__ = [
    "APIAuthorRepository",
    "APIEditionRepository",
    "APIPublisherRepository",
]

from mangacollec.infrastructure.repositories.api.api_author_repository import APIAuthorRepository
from mangacollec.infrastructure.repositories.api.api_edition_repository import APIEditionRepository
from mangacollec.infrastructure.repositories.api.api_publisher_repository import APIPublisherRepository
