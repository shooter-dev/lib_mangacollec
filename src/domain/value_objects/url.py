"""URL value object."""

from dataclasses import dataclass


@dataclass(frozen=True)
class URL:
    """URL value object."""

    value: str
