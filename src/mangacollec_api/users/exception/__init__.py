"""
Exceptions du domaine User.
"""

from .user_exceptions import (
    UserError,
    UserNotFoundError,
    UserValidationError,
    UserCreationError,
    UserUpdateError,
    UserDeletionError,
    UserConversionError,
    UserAuthenticationError,
    UserPermissionError,
    UserDuplicateError,
)

__all__ = [
    "UserError",
    "UserNotFoundError",
    "UserValidationError",
    "UserCreationError",
    "UserUpdateError",
    "UserDeletionError",
    "UserConversionError",
    "UserAuthenticationError",
    "UserPermissionError",
    "UserDuplicateError",
]