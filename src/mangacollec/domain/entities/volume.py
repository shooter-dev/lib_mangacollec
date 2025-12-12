"""Entité Volume.

Cette entité représente un volume d'une édition de manga.
----------
This entity represents a volume of a manga edition.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Volume:
    """Représente un volume d'une édition."""

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
    nb_pages: int | None
    content: str | None
