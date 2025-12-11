"""In-memory repositories implementations."""

__all__ = [
    "InMemoryAuthorRepository",
    "InMemoryEditionRepository",
    "InMemoryFollowEditionRepository",
    "InMemoryJobRepository",
    "InMemoryOfferRepository",
    "InMemoryPlanningRepository",
    "InMemoryPublisherRepository",
]

from mangacollec.infrastructure.repositories.memory.in_memory_author_repository import \
    InMemoryAuthorRepository
from mangacollec.infrastructure.repositories.memory.in_memory_edition_repository import \
    InMemoryEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_follow_edition_repository import \
    InMemoryFollowEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_job_repository import \
    InMemoryJobRepository
from mangacollec.infrastructure.repositories.memory.in_memory_offer_repository import \
    InMemoryOfferRepository
from mangacollec.infrastructure.repositories.memory.in_memory_planning_repository import \
    InMemoryPlanningRepository
from mangacollec.infrastructure.repositories.memory.in_memory_publisher_repository import \
    InMemoryPublisherRepository
