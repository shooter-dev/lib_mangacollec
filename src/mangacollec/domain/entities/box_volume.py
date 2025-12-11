"""Entité BoxVolume.

Cette entité représente un volume dans un coffret (box).
----------
This entity represents a volume within a box set.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BoxVolume:
    """Représente un volume faisant partie d'un coffret."""

    id: str
    title: str | None
    number: int
    release_date: str | None
    isbn: str | None
    asin: str | None
    edition_id: str
    possessions_count: int | None
    not_sold: bool
    image_url: str | None
