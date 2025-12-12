"""Exceptions pour la ressource Serie.

This module contains custom exceptions for Serie-related operations.
"""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class SerieNotFoundException(MangacollecException):
    def __init__(self, serie_id: str) -> None:
        self.serie_id = serie_id
        super().__init__(f"Serie with ID '{serie_id}' not found.")
