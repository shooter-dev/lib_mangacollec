"""Mapper pour la conversion entre les réponses API et les entités NativeAdVolumeHomeFirst.

This module provides mapping functions between API responses and NativeAdVolumeHomeFirst entities.
"""

from mangacollec.domain.entities import NativeAdVolumeHomeFirst


class NativeAdVolumeHomeFirstMapper:
    """Mapper pour convertir entre API et entités NativeAdVolumeHomeFirst du domaine."""

    @staticmethod
    def from_dict(data: dict) -> NativeAdVolumeHomeFirst:
        """Convertit la réponse API en entité NativeAdVolumeHomeFirst.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité NativeAdVolumeHomeFirst
        """
        return NativeAdVolumeHomeFirst(
            id=data["id"],
            volume_id=data["volume_id"],
            title=data["title"],
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
        )

    @staticmethod
    def to_dict(native_ad: NativeAdVolumeHomeFirst) -> dict:
        """Convertit l'entité NativeAdVolumeHomeFirst en dictionnaire.

        Args:
            native_ad: Entité NativeAdVolumeHomeFirst

        Returns:
            Dictionnaire représentant la publicité native
        """
        return {
            "id": native_ad.id,
            "volume_id": native_ad.volume_id,
            "title": native_ad.title,
            "start_date": native_ad.start_date,
            "end_date": native_ad.end_date,
        }
