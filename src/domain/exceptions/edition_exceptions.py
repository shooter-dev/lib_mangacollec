"""Edition exceptions."""


class EditionNotFoundException(Exception):
    """Exception raised when an edition is not found."""

    def __init__(self, edition_id: str):
        """
        Initialize the exception.

        Args:
            edition_id: The id of the edition that was not found.
        """
        self.edition_id = edition_id
        super().__init__(f"Edition with id <{edition_id}> not found.")
