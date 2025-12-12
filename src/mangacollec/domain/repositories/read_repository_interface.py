"""Read repository interface."""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (
    CreateReadsMultipleV1Response,
    DeleteReadsMultipleV1Response,
)


class IReadRepository(ABC):
    """Interface for Read repository.

    This repository handles read operations (manga volumes marked as read).
    """

    @abstractmethod
    def create_reads_multiple_v1(self, volume_ids: list[str]) -> CreateReadsMultipleV1Response:
        """Create multiple read records for the given volumes.

        Args:
            volume_ids: List of volume IDs to mark as read

        Returns:
            CreateReadsMultipleV1Response containing created reads and related editions

        Raises:
            ReadCreationException: If the creation fails
        """
        pass

    @abstractmethod
    def delete_reads_multiple_v1(self, read_ids: list[str]) -> DeleteReadsMultipleV1Response:
        """Delete multiple read records.

        Args:
            read_ids: List of read IDs to delete

        Returns:
            DeleteReadsMultipleV1Response containing deleted reads and related editions

        Raises:
            ReadDeletionException: If the deletion fails
        """
        pass
