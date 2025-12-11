"""Mapper pour la conversion entre les réponses API et les entités BoxVolume.

This module provides mapping functions between API responses and BoxVolume entities.
"""

from mangacollec.domain.entities import BoxVolume


class BoxVolumeMapper:
    """Mapper pour convertir entre API et entités BoxVolume du domaine."""

    @staticmethod
    def from_dict(data: dict) -> BoxVolume:
        """Convertit la réponse API en entité BoxVolume.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité BoxVolume
        """
        return BoxVolume(
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
    def to_dict(box_volume: BoxVolume) -> dict:
        """Convertit l'entité BoxVolume en dictionnaire.

        Args:
            box_volume: Entité BoxVolume

        Returns:
            Dictionnaire représentant le box_volume
        """
        return {
            "id": box_volume.id,
            "title": box_volume.title,
            "number": box_volume.number,
            "release_date": box_volume.release_date,
            "isbn": box_volume.isbn,
            "asin": box_volume.asin,
            "edition_id": box_volume.edition_id,
            "possessions_count": box_volume.possessions_count,
            "not_sold": box_volume.not_sold,
            "image_url": box_volume.image_url,
        }
