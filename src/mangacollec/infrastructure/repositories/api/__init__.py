"""API repositories."""

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
    "APIVolumeRepository",
]

from mangacollec.infrastructure.repositories.api.api_author_repository import (
    APIAuthorRepository,
)
from mangacollec.infrastructure.repositories.api.api_edition_repository import (
    APIEditionRepository,
)
from mangacollec.infrastructure.repositories.api.api_follow_edition_repository import (
    APIFollowEditionRepository,
)
from mangacollec.infrastructure.repositories.api.api_job_repository import (
    APIJobRepository,
)
from mangacollec.infrastructure.repositories.api.api_kind_repository import (
    APIKindRepository,
)
from mangacollec.infrastructure.repositories.api.api_offer_repository import (
    APIOfferRepository,
)
from mangacollec.infrastructure.repositories.api.api_planning_repository import (
    APIPlanningRepository,
)
from mangacollec.infrastructure.repositories.api.api_possession_repository import (
    APIPossessionRepository,
)
from mangacollec.infrastructure.repositories.api.api_publisher_repository import (
    APIPublisherRepository,
)
from mangacollec.infrastructure.repositories.api.api_read_repository import (
    APIReadRepository,
)
from mangacollec.infrastructure.repositories.api.api_serie_repository import (
    APISerieRepository,
)
from mangacollec.infrastructure.repositories.api.api_type_serie_repository import (
    APITypeSerieRepository,
)
from mangacollec.infrastructure.repositories.api.api_volume_repository import (
    APIVolumeRepository,
)
