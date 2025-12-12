"""Repositories interfaces."""

__all__ = [
    "IAuthorRepository",
    "IEditionRepository",
    "IFollowEditionRepository",
    "IJobRepository",
    "IKindRepository",
    "IOfferRepository",
    "IPlanningRepository",
    "IPossessionRepository",
    "IPublisherRepository",
    "IReadRepository",
    "ISerieRepository",
    "ITypeSerieRepository",
    "IUserRepository",
    "IVolumeRepository",
]

from mangacollec.domain.repositories.author_repository_interface import (
    IAuthorRepository,
)
from mangacollec.domain.repositories.edition_repository_interface import (
    IEditionRepository,
)
from mangacollec.domain.repositories.follow_edition_repository_interface import (
    IFollowEditionRepository,
)
from mangacollec.domain.repositories.job_repository_interface import IJobRepository
from mangacollec.domain.repositories.kind_repository_interface import IKindRepository
from mangacollec.domain.repositories.offer_repository_interface import IOfferRepository
from mangacollec.domain.repositories.planning_repository_interface import (
    IPlanningRepository,
)
from mangacollec.domain.repositories.possession_repository_interface import (
    IPossessionRepository,
)
from mangacollec.domain.repositories.publisher_repository_interface import (
    IPublisherRepository,
)
from mangacollec.domain.repositories.read_repository_interface import IReadRepository
from mangacollec.domain.repositories.serie_repository_interface import ISerieRepository
from mangacollec.domain.repositories.type_serie_repository_interface import (
    ITypeSerieRepository,
)
from mangacollec.domain.repositories.user_repository import IUserRepository
from mangacollec.domain.repositories.volume_repository_interface import (
    IVolumeRepository,
)
