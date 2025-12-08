"""ASIN value object."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ASIN:
    """ASIN value object."""

    value: str