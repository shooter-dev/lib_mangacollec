"""Author exceptions."""


class AuthorNotFoundException(Exception):
    """Exception raised when an author is not found."""

    def __init__(self, author_id: str):
        """
        Initialize the exception.

        Args:
            author_id: The id of the author that was not found.
        """
        self.author_id = author_id
        super().__init__(f"Author with id <{author_id}> not found.")
