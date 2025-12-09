"""Entité Serie.

Cette entité représente une série de manga.
----------
This entity represents a manga series.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Serie:
    """Représente une série de manga."""

    id: str
    title: str
    type_id: str
    adult_content: bool
    editions_count: int
    tasks_count: int
