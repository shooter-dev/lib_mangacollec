"""
Exceptions du domaine Genre.
"""

from .genre_exceptions import (
    GenreError,
    GenreNotFoundError,
    GenreValidationError,
    GenreCreationError,
    GenreUpdateError,
    GenreDeletionError,
    GenreConversionError,
    GenreDuplicateError,
)

__all__ = [
    "GenreError",
    "GenreNotFoundError",
    "GenreValidationError",
    "GenreCreationError",
    "GenreUpdateError",
    "GenreDeletionError",
    "GenreConversionError",
    "GenreDuplicateError",
]