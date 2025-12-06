"""Entité TypeSerie.

Cette entité représente un type de série (Manga, Manhwa, etc.).
----------
This entity represents a series type (Manga, Manhwa, etc.).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TypeSerie:
    """Représente un type de série."""

    id: str
    title: str
    to_display: bool
