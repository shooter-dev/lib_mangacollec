"""In-memory repositories."""

__all__ = [
    "InMemoryAuthorRepository",
    "InMemoryEditionRepository",
    "InMemoryPublisherRepository",
]

from tests.infrastructure.repositories.memory.in_memory_author_repository import InMemoryAuthorRepository
from tests.infrastructure.repositories.memory.in_memory_edition_repository import InMemoryEditionRepository
from tests.infrastructure.repositories.memory.in_memory_publisher_repository import InMemoryPublisherRepository
