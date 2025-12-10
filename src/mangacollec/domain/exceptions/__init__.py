"""Domain exceptions package.

This package contains all custom exceptions for the domain layer.
"""

__all__ = [
    "MangacollecException",
    "AuthorNotFoundException",
    "EditionNotFoundException",
    "PublisherNotFoundException",
    "FollowEditionNotFoundException",
    "FollowEditionOperationException",
]

from mangacollec.domain.exceptions.author_exceptions import \
    AuthorNotFoundException
from mangacollec.domain.exceptions.base_exceptions import MangacollecException
from mangacollec.domain.exceptions.edition_exceptions import \
    EditionNotFoundException
from mangacollec.domain.exceptions.follow_edition_exceptions import (
    FollowEditionNotFoundException, FollowEditionOperationException)
from mangacollec.domain.exceptions.publisher_exceptions import \
    PublisherNotFoundException
