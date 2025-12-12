"""TypeSerie exceptions."""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class TypeSerieNotFoundException(MangacollecException):
    """Exception levée lorsqu'un type de série n'est pas trouvé."""

    def __init__(self, type_serie_id: str) -> None:
        """Initialise l'exception.

        Args:
            type_serie_id: ID du type de série non trouvé
        """
        self.type_serie_id = type_serie_id
        super().__init__(f"TypeSerie with ID '{type_serie_id}' not found.")


class TypeSerieRetrievalException(MangacollecException):
    """Exception levée lors d'une erreur de récupération des types de séries."""

    def __init__(self, message: str) -> None:
        """Initialise l'exception.

        Args:
            message: Message d'erreur
        """
        super().__init__(f"Failed to retrieve types: {message}")
