"""Exceptions pour la ressource User.

This module contains custom exceptions for User-related operations.
"""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class UserNotFoundException(MangacollecException):
    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__(f"User with username '{username}' not found.")
