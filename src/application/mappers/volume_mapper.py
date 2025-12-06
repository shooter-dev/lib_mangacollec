"""Mapper pour la conversion entre les réponses API et les entités Volume.

This module provides mapping functions between API responses and Volume entities.
"""

from src.domain.entities import Volume


class VolumeMapper:
    """Mapper pour convertir entre API et entités Volume du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Volume:
        """Convertit la réponse API en entité Volume.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Volume
        """
        return Volume(
            id=data["id"],
            title=data.get("title"),
            number=data["number"],
            release_date=data.get("release_date"),
            isbn=data.get("isbn"),
            asin=data.get("asin"),
            edition_id=data["edition_id"],
            possessions_count=data.get("possessions_count"),
            not_sold=data["not_sold"],
            image_url=data.get("image_url"),
        )

    @staticmethod
    def to_dict(volume: Volume) -> dict:
        """Convertit l'entité Volume en dictionnaire.

        Args:
            volume: Entité Volume

        Returns:
            Dictionnaire représentant le volume
        """
        return {
            "id": volume.id,
            "title": volume.title,
            "number": volume.number,
            "release_date": volume.release_date,
            "isbn": volume.isbn,
            "asin": volume.asin,
            "edition_id": volume.edition_id,
            "possessions_count": volume.possessions_count,
            "not_sold": volume.not_sold,
            "image_url": volume.image_url,
        }
