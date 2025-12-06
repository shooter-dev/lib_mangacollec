"""Mapper pour la conversion entre les réponses API et les entités Job.

This module provides mapping functions between API responses and Job entities.
"""

from src.domain.entities import Job


class JobMapper:
    """Mapper pour convertir entre API et entités Job du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Job:
        """Convertit la réponse API en entité Job.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Job
        """
        return Job(
            id=data["id"],
            title=data["title"],
        )

    @staticmethod
    def to_dict(job: Job) -> dict:
        """Convertit l'entité Job en dictionnaire.

        Args:
            job: Entité Job

        Returns:
            Dictionnaire représentant le job
        """
        return {
            "id": job.id,
            "title": job.title,
        }
