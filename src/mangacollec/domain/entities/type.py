"""Type entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Type:
    """Represents a series type."""

    id: str
    title: str
    to_display: bool
