"""Entité Publisher.

Cette entité représente un éditeur de manga.
----------
This entity represents a manga publisher.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Publisher:
    """Représente un éditeur de manga."""

    id: str
    title: str
    closed: bool
    editions_count: int
    no_amazon: bool
