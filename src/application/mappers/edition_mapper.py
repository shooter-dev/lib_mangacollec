"""Mapper pour la conversion entre les réponses API et les entités Edition.

This module provides mapping functions between API responses and Edition entities.
"""

from src.application.dto.responses import GetEditionByIdV2Response
from src.application.mappers.serie_mapper import SerieMapper
from src.application.mappers.volume_mapper import VolumeMapper
from src.domain.entities import Edition


class EditionMapper:
    """Mapper pour convertir entre API et entités Edition du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Edition:
        """Convertit la réponse API en entité Edition.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Edition
        """
        return Edition(
            id=data["id"],
            title=data.get("title"),
            series_id=data["series_id"],
            publisher_id=data["publisher_id"],
            parent_edition_id=data.get("parent_edition_id"),
            volumes_count=data["volumes_count"],
            last_volume_number=data.get("last_volume_number"),
            commercial_stop=data["commercial_stop"],
            not_finished=data["not_finished"],
            follow_editions_count=data["follow_editions_count"],
        )

    @staticmethod
    def to_dict(edition: Edition) -> dict:
        """Convertit l'entité Edition en dictionnaire.

        Args:
            edition: Entité Edition

        Returns:
            Dictionnaire représentant l'édition
        """
        return {
            "id": edition.id,
            "title": edition.title,
            "series_id": edition.series_id,
            "publisher_id": edition.publisher_id,
            "parent_edition_id": edition.parent_edition_id,
            "volumes_count": edition.volumes_count,
            "last_volume_number": edition.last_volume_number,
            "commercial_stop": edition.commercial_stop,
            "not_finished": edition.not_finished,
            "follow_editions_count": edition.follow_editions_count,
        }

    @staticmethod
    def from_api_response(response: dict) -> GetEditionByIdV2Response:
        """Convertit la réponse complète de l'API V2 en GetEditionByIdV2Response.

        Args:
            response: Réponse API contenant editions, publishers, series, types, volumes

        Returns:
            GetEditionByIdV2Response contenant toutes les entités converties
        """
        from src.application.mappers.publisher_mapper import PublisherMapper
        from src.application.mappers.type_mapper import TypeMapper
        # Convertir les editions (liste)
        editions = [
            EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])
        ]

        # Convertir les publishers
        publishers = [
            PublisherMapper.from_dict(publisher_data)
            for publisher_data in response.get("publishers", [])
        ]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [
            TypeMapper.from_dict(type_data) for type_data in response.get("types", [])
        ]

        # Convertir les volumes
        volumes = [
            VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])
        ]

        return GetEditionByIdV2Response(
            editions=editions,
            publishers=publishers,
            series=series,
            types=types,
            volumes=volumes,
        )
