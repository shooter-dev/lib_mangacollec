"""Read mapper for converting between API responses and domain entities."""

from datetime import datetime

from mangacollec.application.dto.read_responses import (
    CreateReadsMultipleV1Response,
    DeleteReadsMultipleV1Response,
)
from mangacollec.domain.entities import (
    Read,
    ReadDeleted,
    ReadEdition,
    ReadEditionDeleted,
)


class ReadMapper:
    """Mapper for converting between Read entities and API responses."""

    @staticmethod
    def from_read_dict(data: dict) -> Read:
        """Convert API dict to Read entity.

        Args:
            data: Dictionary from API containing read data

        Returns:
            Read entity with converted data
        """
        return Read(
            id=data["id"],
            user_id=data["user_id"],
            volume_id=data["volume_id"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
        )

    @staticmethod
    def from_read_edition_dict(data: dict) -> ReadEdition:
        """Convert API dict to ReadEdition entity.

        Args:
            data: Dictionary from API containing read edition data

        Returns:
            ReadEdition entity with converted data
        """
        return ReadEdition(
            id=data["id"],
            user_id=data["user_id"],
            edition_id=data["edition_id"],
            reading=data["reading"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
        )

    @staticmethod
    def from_read_deleted_dict(data: dict) -> ReadDeleted:
        """Convert API dict to ReadDeleted entity.

        Args:
            data: Dictionary from API containing deleted read data

        Returns:
            ReadDeleted entity with converted data
        """
        return ReadDeleted(
            id=data["id"],
            deleted=data["deleted"],
        )

    @staticmethod
    def from_read_edition_deleted_dict(data: dict) -> ReadEditionDeleted:
        """Convert API dict to ReadEditionDeleted entity.

        Args:
            data: Dictionary from API containing deleted read edition data

        Returns:
            ReadEditionDeleted entity with converted data
        """
        return ReadEditionDeleted(
            id=data["id"],
            deleted=data["deleted"],
        )

    @staticmethod
    def to_read_dict(read: Read) -> dict:
        """Convert Read entity to dictionary.

        Args:
            read: Read entity to convert

        Returns:
            Dictionary representation of the read
        """
        return {
            "id": read.id,
            "user_id": read.user_id,
            "volume_id": read.volume_id,
            "created_at": read.created_at.isoformat().replace("+00:00", "Z"),
        }

    @staticmethod
    def to_read_edition_dict(read_edition: ReadEdition) -> dict:
        """Convert ReadEdition entity to dictionary.

        Args:
            read_edition: ReadEdition entity to convert

        Returns:
            Dictionary representation of the read edition
        """
        return {
            "id": read_edition.id,
            "user_id": read_edition.user_id,
            "edition_id": read_edition.edition_id,
            "reading": read_edition.reading,
            "created_at": read_edition.created_at.isoformat().replace("+00:00", "Z"),
        }

    @staticmethod
    def to_read_deleted_dict(read_deleted: ReadDeleted) -> dict:
        """Convert ReadDeleted entity to dictionary.

        Args:
            read_deleted: ReadDeleted entity to convert

        Returns:
            Dictionary representation of the deleted read
        """
        return {
            "id": read_deleted.id,
            "deleted": read_deleted.deleted,
        }

    @staticmethod
    def to_read_edition_deleted_dict(read_edition_deleted: ReadEditionDeleted) -> dict:
        """Convert ReadEditionDeleted entity to dictionary.

        Args:
            read_edition_deleted: ReadEditionDeleted entity to convert

        Returns:
            Dictionary representation of the deleted read edition
        """
        return {
            "id": read_edition_deleted.id,
            "deleted": read_edition_deleted.deleted,
        }

    @staticmethod
    def from_create_reads_response(response: dict) -> CreateReadsMultipleV1Response:
        """Convert API create response to CreateReadsMultipleV1Response.

        Args:
            response: Response from API containing reads and read_editions

        Returns:
            CreateReadsMultipleV1Response with converted entities
        """
        reads = [ReadMapper.from_read_dict(read_data) for read_data in response.get("reads", [])]
        read_editions = [
            ReadMapper.from_read_edition_dict(read_edition_data)
            for read_edition_data in response.get("read_editions", [])
        ]

        return CreateReadsMultipleV1Response(reads=reads, read_editions=read_editions)

    @staticmethod
    def from_delete_reads_response(response: dict) -> DeleteReadsMultipleV1Response:
        """Convert API delete response to DeleteReadsMultipleV1Response.

        Args:
            response: Response from API containing deleted reads and read_editions

        Returns:
            DeleteReadsMultipleV1Response with converted entities
        """
        reads = [ReadMapper.from_read_deleted_dict(read_data) for read_data in response.get("reads", [])]
        read_editions = [
            ReadMapper.from_read_edition_deleted_dict(read_edition_data)
            for read_edition_data in response.get("read_editions", [])
        ]

        return DeleteReadsMultipleV1Response(reads=reads, read_editions=read_editions)
