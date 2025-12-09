"""Exceptions pour la ressource Author.

This module contains custom exceptions for Author-related operations.
"""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class AuthorNotFoundException(MangacollecException):
    def __init__(self, author_id: str) -> None:
        self.author_id = author_id
        super().__init__(f"Author with ID '{author_id}' not found.")
