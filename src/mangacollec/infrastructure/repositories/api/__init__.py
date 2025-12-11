"""API repositories."""

__all__ = [
    "APIAuthorRepository",
    "APIEditionRepository",
    "APIFollowEditionRepository",
    "APIJobRepository",
    "APIOfferRepository",
    "APIPublisherRepository",
]

from mangacollec.infrastructure.repositories.api.api_author_repository import \
    APIAuthorRepository
from mangacollec.infrastructure.repositories.api.api_edition_repository import \
    APIEditionRepository
from mangacollec.infrastructure.repositories.api.api_follow_edition_repository import \
    APIFollowEditionRepository
from mangacollec.infrastructure.repositories.api.api_job_repository import \
    APIJobRepository
from mangacollec.infrastructure.repositories.api.api_offer_repository import \
    APIOfferRepository
from mangacollec.infrastructure.repositories.api.api_publisher_repository import \
    APIPublisherRepository
