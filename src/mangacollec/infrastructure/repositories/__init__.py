"""Infrastructure repositories package."""

__all__ = [
    "APIAuthorRepository",
    "APIEditionRepository",
    "APIFollowEditionRepository",
    "APIJobRepository",
    "APIPublisherRepository",
    "InMemoryAuthorRepository",
    "InMemoryEditionRepository",
    "InMemoryFollowEditionRepository",
    "InMemoryJobRepository",
    "InMemoryPublisherRepository",
]

from mangacollec.infrastructure.repositories.api.api_author_repository import \
    APIAuthorRepository
from mangacollec.infrastructure.repositories.api.api_edition_repository import \
    APIEditionRepository
from mangacollec.infrastructure.repositories.api.api_follow_edition_repository import \
    APIFollowEditionRepository
from mangacollec.infrastructure.repositories.api.api_job_repository import \
    APIJobRepository
from mangacollec.infrastructure.repositories.api.api_publisher_repository import \
    APIPublisherRepository
from mangacollec.infrastructure.repositories.memory.in_memory_author_repository import \
    InMemoryAuthorRepository
from mangacollec.infrastructure.repositories.memory.in_memory_edition_repository import \
    InMemoryEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_follow_edition_repository import \
    InMemoryFollowEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_job_repository import \
    InMemoryJobRepository
from mangacollec.infrastructure.repositories.memory.in_memory_publisher_repository import \
    InMemoryPublisherRepository
