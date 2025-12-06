"""Entité Job.

Cette entité représente un rôle/métier d'un auteur (ex: Auteur, Auteur original, etc.).
----------
This entity represents a job/role of an author (e.g., Author, Original Author, etc.).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    """Représente un rôle/métier dans une série."""

    id: str
    title: str
