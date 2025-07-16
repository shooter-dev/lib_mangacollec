"""
Exceptions du domaine Kind.
"""

from .kind_exceptions import (
    KindError,
    KindNotFoundError,
    KindValidationError,
    KindCreationError,
    KindUpdateError,
    KindDeletionError,
    KindConversionError,
    KindTypeError,
)

__all__ = [
    "KindError",
    "KindNotFoundError",
    "KindValidationError",
    "KindCreationError",
    "KindUpdateError",
    "KindDeletionError",
    "KindConversionError",
    "KindTypeError",
]