"""API Read repository implementation."""

from mangacollec.application.dto import (
    CreateReadsMultipleV1Response,
    DeleteReadsMultipleV1Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import ReadMapper
from mangacollec.domain.exceptions import ReadCreationException, ReadDeletionException
from mangacollec.domain.repositories import IReadRepository


class APIReadRepository(IReadRepository):
    """API implementation of the Read repository using MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialize the repository with an authenticated API client.

        Args:
            client_api: Authenticated MangaCollecAPI instance
        """
        self.client_api = client_api

    def create_reads_multiple_v1(self, volume_ids: list[str]) -> CreateReadsMultipleV1Response:
        """Create multiple read records via the API.

        Args:
            volume_ids: List of volume IDs to mark as read

        Returns:
            CreateReadsMultipleV1Response containing created reads and read editions

        Raises:
            ReadCreationException: If the creation fails
        """
        try:
            payload = [{"volume_id": volume_id} for volume_id in volume_ids]
            response = self.client_api.post("/v1/reads_multiple", data=payload)
            return ReadMapper.from_create_reads_response(response)
        except Exception as e:
            raise ReadCreationException(volume_ids, str(e)) from e

    def delete_reads_multiple_v1(self, read_ids: list[str]) -> DeleteReadsMultipleV1Response:
        """Delete multiple read records via the API.

        Args:
            read_ids: List of read IDs to delete

        Returns:
            DeleteReadsMultipleV1Response containing deleted reads and read editions

        Raises:
            ReadDeletionException: If the deletion fails
        """
        try:
            payload = [{"id": read_id} for read_id in read_ids]
            response = self.client_api.delete("/v1/reads_multiple", data=payload)
            return ReadMapper.from_delete_reads_response(response)
        except Exception as e:
            raise ReadDeletionException(read_ids, str(e)) from e
