"""
Exceptions du domaine Author.
"""

from .author_exceptions import (
    AuthorError,
    AuthorNotFoundError,
    AuthorValidationError,
    AuthorCreationError,
    AuthorUpdateError,
    AuthorDeletionError,
    AuthorConversionError,
)

__all__ = [
    "AuthorError",
    "AuthorNotFoundError",
    "AuthorValidationError",
    "AuthorCreationError",
    "AuthorUpdateError",
    "AuthorDeletionError",
    "AuthorConversionError",
]