"""Read entities."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Read:
    """Read entity representing a manga reading record.

    Attributes:
        id: Unique identifier of the read
        user_id: ID of the user who read the volume
        volume_id: ID of the volume that was read
        created_at: Date and time when the read was created
    """

    id: str
    user_id: str
    volume_id: str
    created_at: datetime


@dataclass(frozen=True)
class ReadEdition:
    """ReadEdition entity with edition information.

    This entity represents an edition that is being read/followed automatically
    when a volume is marked as read.

    Attributes:
        id: Unique identifier of the read edition
        user_id: ID of the user reading the edition
        edition_id: ID of the edition being read
        reading: Whether the edition is currently being read
        created_at: Date and time when the read edition was created
    """

    id: str
    user_id: str
    edition_id: str
    reading: bool
    created_at: datetime


@dataclass(frozen=True)
class ReadDeleted:
    """ReadDeleted entity representing a deleted read record.

    Attributes:
        id: ID of the read that was deleted
        deleted: Whether the deletion was successful
    """

    id: str
    deleted: bool


@dataclass(frozen=True)
class ReadEditionDeleted:
    """ReadEditionDeleted entity representing a deleted read edition record.

    Attributes:
        id: ID of the read edition that was deleted
        deleted: Whether the deletion was successful
    """

    id: str
    deleted: bool
