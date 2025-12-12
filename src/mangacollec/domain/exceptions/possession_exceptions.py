"""Possession exceptions."""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class PossessionNotFoundException(MangacollecException):
    """Exception levée quand une possession n'est pas trouvée."""

    def __init__(self, possession_id: str) -> None:
        """Initialise l'exception.

        Args:
            possession_id: ID de la possession non trouvée
        """
        self.possession_id = possession_id
        super().__init__(f"Possession with ID '{possession_id}' not found.")


class PossessionCreationException(MangacollecException):
    """Exception levée lors d'une erreur de création de possession."""

    def __init__(self, message: str) -> None:
        """Initialise l'exception.

        Args:
            message: Message d'erreur
        """
        super().__init__(f"Possession creation failed: {message}")


class PossessionDeletionException(MangacollecException):
    """Exception levée lors d'une erreur de suppression de possession."""

    def __init__(self, message: str) -> None:
        """Initialise l'exception.

        Args:
            message: Message d'erreur
        """
        super().__init__(f"Possession deletion failed: {message}")
