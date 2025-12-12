"""Infrastructure repositories package."""

__all__ = [
    "APIAuthorRepository",
    "APIEditionRepository",
    "APIFollowEditionRepository",
    "APIJobRepository",
    "APIKindRepository",
    "APIOfferRepository",
    "APIPlanningRepository",
    "APIPossessionRepository",
    "APIPublisherRepository",
    "APIReadRepository",
    "APISerieRepository",
    "APITypeSerieRepository",
    "APIUserRepository",
    "APIVolumeRepository",
    "InMemoryAuthorRepository",
    "InMemoryEditionRepository",
    "InMemoryFollowEditionRepository",
    "InMemoryJobRepository",
    "InMemoryKindRepository",
    "InMemoryOfferRepository",
    "InMemoryPlanningRepository",
    "InMemoryPossessionRepository",
    "InMemoryPublisherRepository",
    "InMemoryReadRepository",
    "InMemorySerieRepository",
    "InMemoryTypeSerieRepository",
    "InMemoryUserRepository",
    "InMemoryVolumeRepository",
]

from mangacollec.infrastructure.repositories.api.api_author_repository import \
    APIAuthorRepository
from mangacollec.infrastructure.repositories.api.api_edition_repository import \
    APIEditionRepository
from mangacollec.infrastructure.repositories.api.api_follow_edition_repository import \
    APIFollowEditionRepository
from mangacollec.infrastructure.repositories.api.api_job_repository import \
    APIJobRepository
from mangacollec.infrastructure.repositories.api.api_kind_repository import \
    APIKindRepository
from mangacollec.infrastructure.repositories.api.api_offer_repository import \
    APIOfferRepository
from mangacollec.infrastructure.repositories.api.api_planning_repository import \
    APIPlanningRepository
from mangacollec.infrastructure.repositories.api.api_possession_repository import \
    APIPossessionRepository
from mangacollec.infrastructure.repositories.api.api_publisher_repository import \
    APIPublisherRepository
from mangacollec.infrastructure.repositories.api.api_read_repository import \
    APIReadRepository
from mangacollec.infrastructure.repositories.api.api_serie_repository import \
    APISerieRepository
from mangacollec.infrastructure.repositories.api.api_type_serie_repository import \
    APITypeSerieRepository
from mangacollec.infrastructure.repositories.api.api_user_repository import \
    APIUserRepository
from mangacollec.infrastructure.repositories.api.api_volume_repository import \
    APIVolumeRepository
from mangacollec.infrastructure.repositories.memory.in_memory_author_repository import \
    InMemoryAuthorRepository
from mangacollec.infrastructure.repositories.memory.in_memory_edition_repository import \
    InMemoryEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_follow_edition_repository import \
    InMemoryFollowEditionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_job_repository import \
    InMemoryJobRepository
from mangacollec.infrastructure.repositories.memory.in_memory_kind_repository import \
    InMemoryKindRepository
from mangacollec.infrastructure.repositories.memory.in_memory_offer_repository import \
    InMemoryOfferRepository
from mangacollec.infrastructure.repositories.memory.in_memory_planning_repository import \
    InMemoryPlanningRepository
from mangacollec.infrastructure.repositories.memory.in_memory_possession_repository import \
    InMemoryPossessionRepository
from mangacollec.infrastructure.repositories.memory.in_memory_publisher_repository import \
    InMemoryPublisherRepository
from mangacollec.infrastructure.repositories.memory.in_memory_read_repository import \
    InMemoryReadRepository
from mangacollec.infrastructure.repositories.memory.in_memory_serie_repository import \
    InMemorySerieRepository
from mangacollec.infrastructure.repositories.memory.in_memory_type_serie_repository import \
    InMemoryTypeSerieRepository
from mangacollec.infrastructure.repositories.memory.in_memory_user_repository import \
    InMemoryUserRepository
from mangacollec.infrastructure.repositories.memory.in_memory_volume_repository import \
    InMemoryVolumeRepository
