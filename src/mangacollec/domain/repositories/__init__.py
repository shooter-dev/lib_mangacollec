"""Repositories interfaces."""

__all__ = [
    "IAuthorRepository",
    "IEditionRepository",
    "IFollowEditionRepository",
    "IJobRepository",
    "IKindRepository",
    "IOfferRepository",
    "IPlanningRepository",
    "IPublisherRepository",
]

from mangacollec.domain.repositories.author_repository_interface import \
    IAuthorRepository
from mangacollec.domain.repositories.edition_repository_interface import \
    IEditionRepository
from mangacollec.domain.repositories.follow_edition_repository_interface import \
    IFollowEditionRepository
from mangacollec.domain.repositories.job_repository_interface import \
    IJobRepository
from mangacollec.domain.repositories.kind_repository import IKindRepository
from mangacollec.domain.repositories.offer_repository_interface import \
    IOfferRepository
from mangacollec.domain.repositories.planning_repository import \
    IPlanningRepository
from mangacollec.domain.repositories.publisher_repository_interface import \
    IPublisherRepository
