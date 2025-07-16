"""
Exceptions du domaine Serie.
"""

from .serie_exceptions import (
    SerieError,
    SerieNotFoundError,
    SerieValidationError,
    SerieCreationError,
    SerieUpdateError,
    SerieDeletionError,
    SerieConversionError,
    SerieStatusError,
)

__all__ = [
    "SerieError",
    "SerieNotFoundError",
    "SerieValidationError",
    "SerieCreationError",
    "SerieUpdateError",
    "SerieDeletionError",
    "SerieConversionError",
    "SerieStatusError",
]