"""Read use cases."""

from mangacollec.application.dto import (CreateReadsMultipleV1Response,
                                         DeleteReadsMultipleV1Response)
from mangacollec.domain.repositories import IReadRepository


class CreateReadsMultipleV1UseCase:
    """Use case for creating multiple read records.

    This use case allows marking multiple volumes as read in a single operation.
    The API automatically follows the associated editions when a volume is marked as read.
    """

    def __init__(self, repository: IReadRepository) -> None:
        """Initialize the use case.

        Args:
            repository: Read repository implementation
        """
        self.repository = repository

    def __call__(self, volume_ids: list[str]) -> CreateReadsMultipleV1Response:
        """Execute the use case to create multiple reads.

        Args:
            volume_ids: List of volume IDs to mark as read

        Returns:
            CreateReadsMultipleV1Response containing created reads and read editions

        Raises:
            ReadCreationException: If the creation fails
        """
        return self.repository.create_reads_multiple_v1(volume_ids)


class DeleteReadsMultipleV1UseCase:
    """Use case for deleting multiple read records.

    This use case allows removing multiple read records in a single operation.
    The API automatically unfollows the associated editions when a read is deleted
    if there are no other reads for that edition.
    """

    def __init__(self, repository: IReadRepository) -> None:
        """Initialize the use case.

        Args:
            repository: Read repository implementation
        """
        self.repository = repository

    def __call__(self, read_ids: list[str]) -> DeleteReadsMultipleV1Response:
        """Execute the use case to delete multiple reads.

        Args:
            read_ids: List of read IDs to delete

        Returns:
            DeleteReadsMultipleV1Response containing deleted reads and read editions

        Raises:
            ReadDeletionException: If the deletion fails
        """
        return self.repository.delete_reads_multiple_v1(read_ids)
