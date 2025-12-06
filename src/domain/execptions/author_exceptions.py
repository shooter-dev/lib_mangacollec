"""Exceptions pour la ressource Author.

This module contains custom exceptions for Author-related operations.
"""

from src.domain.execptions.base_exeptions import MangacollecException


class AuthorNotFoundException(MangacollecException):
    def __init__(self, author_id: str) -> None:
        self.author_id = author_id
        super().__init__(f"Author with ID '{author_id}' not found.")
