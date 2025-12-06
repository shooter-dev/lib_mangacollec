"""Mapper pour la conversion entre les réponses API et les entités Publisher.

This module provides mapping functions between API responses and Publisher entities.
"""

from src.domain.entities import Publisher


class PublisherMapper:
    """Mapper pour convertir entre API et entités Publisher du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Publisher:
        """Convertit la réponse API en entité Publisher.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Publisher
        """
        return Publisher(
            id=data["id"],
            title=data["title"],
            closed=data["closed"],
            editions_count=data["editions_count"],
            no_amazon=data["no_amazon"],
        )

    @staticmethod
    def to_dict(publisher: Publisher) -> dict:
        """Convertit l'entité Publisher en dictionnaire.

        Args:
            publisher: Entité Publisher

        Returns:
            Dictionnaire représentant l'éditeur
        """
        return {
            "id": publisher.id,
            "title": publisher.title,
            "closed": publisher.closed,
            "editions_count": publisher.editions_count,
            "no_amazon": publisher.no_amazon,
        }
