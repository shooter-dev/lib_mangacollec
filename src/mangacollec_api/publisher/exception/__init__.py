"""
Exceptions du domaine Publisher.
"""

from .publisher_exceptions import (
    PublisherError,
    PublisherNotFoundError,
    PublisherValidationError,
    PublisherCreationError,
    PublisherUpdateError,
    PublisherDeletionError,
    PublisherConversionError,
    PublisherDuplicateError,
)

__all__ = [
    "PublisherError",
    "PublisherNotFoundError",
    "PublisherValidationError",
    "PublisherCreationError",
    "PublisherUpdateError",
    "PublisherDeletionError",
    "PublisherConversionError",
    "PublisherDuplicateError",
]