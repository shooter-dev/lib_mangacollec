"""Follow Edition exceptions."""

from mangacollec.domain.exceptions import MangacollecException


class FollowEditionNotFoundException(MangacollecException):
    """Exception levée quand un suivi d'édition n'est pas trouvé."""

    def __init__(self, follow_edition_id: str) -> None:
        """Initialise l'exception.

        Args:
            follow_edition_id: Identifiant du suivi d'édition non trouvé
        """
        self.follow_edition_id = follow_edition_id
        super().__init__(f"FollowEdition with ID '{follow_edition_id}' not found.")


class FollowEditionOperationException(MangacollecException):
    """Exception levée lors d'une erreur d'opération sur un suivi d'édition."""

    def __init__(self, message: str) -> None:
        """Initialise l'exception.

        Args:
            message: Message d'erreur détaillé
        """
        super().__init__(message)
