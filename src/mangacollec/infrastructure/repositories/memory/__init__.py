"""In-memory repositories implementations."""

__all__ = [
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
    "InMemoryVolumeRepository",
]

from mangacollec.infrastructure.repositories.memory.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_edition_repository import (
    InMemoryEditionRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_follow_edition_repository import (
    InMemoryFollowEditionRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_job_repository import (
    InMemoryJobRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_kind_repository import (
    InMemoryKindRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_offer_repository import (
    InMemoryOfferRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_planning_repository import (
    InMemoryPlanningRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_possession_repository import (
    InMemoryPossessionRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_publisher_repository import (
    InMemoryPublisherRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_read_repository import (
    InMemoryReadRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_serie_repository import (
    InMemorySerieRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_type_serie_repository import (
    InMemoryTypeSerieRepository,
)
from mangacollec.infrastructure.repositories.memory.in_memory_volume_repository import (
    InMemoryVolumeRepository,
)
