"""ISBN value object."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ISBN:
    """ISBN value object."""

    value: str
