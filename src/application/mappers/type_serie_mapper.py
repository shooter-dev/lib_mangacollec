"""Mapper pour la conversion entre les réponses API et les entités TypeSerie.

This module provides mapping functions between API responses and TypeSerie entities.
"""

from src.domain.entities import TypeSerie


class TypeSerieMapper:
    """Mapper pour convertir entre API et entités TypeSerie du domaine."""

    @staticmethod
    def from_dict(data: dict) -> TypeSerie:
        """Convertit la réponse API en entité TypeSerie.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité TypeSerie
        """
        return TypeSerie(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"],
        )

    @staticmethod
    def to_dict(type_serie: TypeSerie) -> dict:
        """Convertit l'entité TypeSerie en dictionnaire.

        Args:
            type_serie: Entité TypeSerie

        Returns:
            Dictionnaire représentant le type de série
        """
        return {
            "id": type_serie.id,
            "title": type_serie.title,
            "to_display": type_serie.to_display,
        }
