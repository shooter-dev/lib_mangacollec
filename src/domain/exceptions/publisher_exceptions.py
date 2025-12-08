"""Publisher exceptions."""


class PublisherNotFoundException(Exception):
    """Exception raised when a publisher is not found."""

    def __init__(self, publisher_id: str):
        """
        Initialize the exception.

        Args:
            publisher_id: The id of the publisher that was not found.
        """
        self.publisher_id = publisher_id
        super().__init__(f"Publisher with id <{publisher_id}> not found.")
