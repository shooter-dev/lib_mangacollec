"""Read exceptions."""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class ReadCreationException(MangacollecException):
    """Exception raised when read creation fails.

    Attributes:
        volume_ids: List of volume IDs that failed to be marked as read
    """

    def __init__(self, volume_ids: list[str], message: str | None = None) -> None:
        """Initialize the exception.

        Args:
            volume_ids: List of volume IDs that failed
            message: Optional custom error message
        """
        self.volume_ids = volume_ids
        default_message = f"Failed to create reads for volumes: {', '.join(volume_ids)}"
        super().__init__(message or default_message)


class ReadDeletionException(MangacollecException):
    """Exception raised when read deletion fails.

    Attributes:
        read_ids: List of read IDs that failed to be deleted
    """

    def __init__(self, read_ids: list[str], message: str | None = None) -> None:
        """Initialize the exception.

        Args:
            read_ids: List of read IDs that failed
            message: Optional custom error message
        """
        self.read_ids = read_ids
        default_message = f"Failed to delete reads: {', '.join(read_ids)}"
        super().__init__(message or default_message)
