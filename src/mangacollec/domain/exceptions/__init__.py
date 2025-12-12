"""Domain exceptions package.

This package contains all custom exceptions for the domain layer.
"""

__all__ = [
    "AmazonOfferNotFoundException",
    "AuthorNotFoundException",
    "BDFugueOfferNotFoundException",
    "EditionNotFoundException",
    "FollowEditionNotFoundException",
    "FollowEditionOperationException",
    "KindNotFoundException",
    "MangacollecException",
    "PossessionCreationException",
    "PossessionDeletionException",
    "PossessionNotFoundException",
    "PublisherNotFoundException",
    "ReadCreationException",
    "ReadDeletionException",
    "SerieNotFoundException",
    "TypeSerieNotFoundException",
    "TypeSerieRetrievalException",
    "UserNotFoundException",
    "VolumeNotFoundException",
]

from mangacollec.domain.exceptions.author_exceptions import AuthorNotFoundException
from mangacollec.domain.exceptions.base_exceptions import MangacollecException
from mangacollec.domain.exceptions.edition_exceptions import EditionNotFoundException
from mangacollec.domain.exceptions.follow_edition_exceptions import (
    FollowEditionNotFoundException,
    FollowEditionOperationException,
)
from mangacollec.domain.exceptions.kind_exceptions import KindNotFoundException
from mangacollec.domain.exceptions.offer_exceptions import (
    AmazonOfferNotFoundException,
    BDFugueOfferNotFoundException,
)
from mangacollec.domain.exceptions.possession_exceptions import (
    PossessionCreationException,
    PossessionDeletionException,
    PossessionNotFoundException,
)
from mangacollec.domain.exceptions.publisher_exceptions import (
    PublisherNotFoundException,
)
from mangacollec.domain.exceptions.read_exceptions import (
    ReadCreationException,
    ReadDeletionException,
)
from mangacollec.domain.exceptions.serie_exceptions import SerieNotFoundException
from mangacollec.domain.exceptions.type_serie_exceptions import (
    TypeSerieNotFoundException,
    TypeSerieRetrievalException,
)
from mangacollec.domain.exceptions.user_exceptions import UserNotFoundException
from mangacollec.domain.exceptions.volume_exceptions import VolumeNotFoundException
