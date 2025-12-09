"""Entité Edition.

Cette entité représente une édition d'une série de manga.
----------
This entity represents an edition of a manga series.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Edition:
    """Représente une édition d'une série."""

    id: str
    title: str | None
    series_id: str
    publisher_id: str
    parent_edition_id: str | None
    volumes_count: int
    last_volume_number: int | None
    commercial_stop: bool
    not_finished: bool
    follow_editions_count: int
