"""Read response DTOs."""

from dataclasses import dataclass

from mangacollec.domain.entities import (Read, ReadDeleted, ReadEdition,
                                         ReadEditionDeleted)


@dataclass(frozen=True)
class CreateReadsMultipleV1Response:
    """Response DTO for creating multiple read records.

    This DTO contains reads and read_editions returned from the API.

    Attributes:
        reads: List of created read records
        read_editions: List of created read edition records (auto-follow)
    """

    reads: list[Read]
    read_editions: list[ReadEdition]


@dataclass(frozen=True)
class DeleteReadsMultipleV1Response:
    """Response DTO for deleting multiple read records.

    This DTO contains deleted reads and read_editions returned from the API.

    Attributes:
        reads: List of deleted read records
        read_editions: List of deleted read edition records
    """

    reads: list[ReadDeleted]
    read_editions: list[ReadEditionDeleted]
