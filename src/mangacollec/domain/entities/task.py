"""Entité Task.

Cette entité représente une tâche liant un auteur, un rôle et une série.
----------
This entity represents a task linking an author, a role, and a series.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """Représente une tâche (relation auteur-rôle-série)."""

    id: str
    job_id: str
    series_id: str
    author_id: str
