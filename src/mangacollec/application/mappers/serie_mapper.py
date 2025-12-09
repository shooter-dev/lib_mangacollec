"""Mapper pour la conversion entre les réponses API et les entités Serie.

This module provides mapping functions between API responses and Serie entities.
"""

from mangacollec.domain.entities import Serie


class SerieMapper:
    """Mapper pour convertir entre API et entités Serie du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Serie:
        """Convertit la réponse API en entité Serie.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Serie
        """
        return Serie(
            id=data["id"],
            title=data["title"],
            type_id=data["type_id"],
            adult_content=data["adult_content"],
            editions_count=data["editions_count"],
            tasks_count=data["tasks_count"],
        )

    @staticmethod
    def to_dict(serie: Serie) -> dict:
        """Convertit l'entité Serie en dictionnaire.

        Args:
            serie: Entité Serie

        Returns:
            Dictionnaire représentant la série
        """
        return {
            "id": serie.id,
            "title": serie.title,
            "type_id": serie.type_id,
            "adult_content": serie.adult_content,
            "editions_count": serie.editions_count,
            "tasks_count": serie.tasks_count,
        }
