"""
Exceptions du domaine Edition.
"""

from .edition_exceptions import (
    EditionError,
    EditionNotFoundError,
    EditionValidationError,
    EditionCreationError,
    EditionUpdateError,
    EditionDeletionError,
    EditionConversionError,
    EditionAvailabilityError,
)

__all__ = [
    "EditionError",
    "EditionNotFoundError",
    "EditionValidationError",
    "EditionCreationError",
    "EditionUpdateError",
    "EditionDeletionError",
    "EditionConversionError",
    "EditionAvailabilityError",
]