"""Exceptions pour la ressource Edition.

This module contains custom exceptions for Edition-related operations.
"""

from src.domain.execptions.base_exeptions import MangacollecException


class EditionNotFoundException(MangacollecException):
    """Exception levée quand une édition n'est pas trouvée."""

    def __init__(self, edition_id: str) -> None:
        """Initialise l'exception.

        Args:
            edition_id: ID de l'édition non trouvée
        """
        self.edition_id = edition_id
        super().__init__(f"Edition with ID '{edition_id}' not found.")
