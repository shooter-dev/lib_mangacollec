"""Kind-specific exceptions."""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class KindNotFoundException(MangacollecException):
    """Exception levée lorsqu'un kind n'est pas trouvé."""

    def __init__(self, kind_id: str) -> None:
        """Initialise l'exception.

        Args:
            kind_id: ID du kind non trouvé
        """
        self.kind_id = kind_id
        super().__init__(f"Kind with ID '{kind_id}' not found.")
