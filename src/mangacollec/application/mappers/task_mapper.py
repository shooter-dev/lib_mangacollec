"""Mapper pour la conversion entre les réponses API et les entités Task.

This module provides mapping functions between API responses and Task entities.
"""

from mangacollec.domain.entities import Task


class TaskMapper:
    """Mapper pour convertir entre API et entités Task du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Task:
        """Convertit la réponse API en entité Task.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Task
        """
        return Task(
            id=data["id"],
            job_id=data["job_id"],
            series_id=data["series_id"],
            author_id=data["author_id"],
        )

    @staticmethod
    def to_dict(task: Task) -> dict:
        """Convertit l'entité Task en dictionnaire.

        Args:
            task: Entité Task

        Returns:
            Dictionnaire représentant la task
        """
        return {
            "id": task.id,
            "job_id": task.job_id,
            "series_id": task.series_id,
            "author_id": task.author_id,
        }
