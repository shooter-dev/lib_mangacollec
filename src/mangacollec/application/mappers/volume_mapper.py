"""Mapper pour la conversion entre les réponses API et les entités Volume.

This module provides mapping functions between API responses and Volume entities.
"""

from typing import TYPE_CHECKING

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.domain.entities import Volume

if TYPE_CHECKING:
    pass


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
            nb_pages=data.get("nb_pages"),
            content=data.get("content"),
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
            "nb_pages": volume.nb_pages,
            "content": volume.content,
        }

    @staticmethod
    def from_api_response(response: dict) -> GetVolumeByIdV2Response:
        """Convertit la réponse complète de l'API V2 en GetVolumeByIdV2Response.

        Args:
            response: Réponse API contenant volumes et toutes les entités liées

        Returns:
            GetVolumeByIdV2Response contenant toutes les entités converties
        """
        # Import local pour éviter l'import circulaire
        from mangacollec.application.mappers.box_edition_mapper import BoxEditionMapper
        from mangacollec.application.mappers.box_mapper import BoxMapper
        from mangacollec.application.mappers.box_volume_mapper import BoxVolumeMapper
        from mangacollec.application.mappers.edition_mapper import EditionMapper
        from mangacollec.application.mappers.publisher_mapper import PublisherMapper
        from mangacollec.application.mappers.serie_mapper import SerieMapper
        from mangacollec.application.mappers.type_serie_mapper import TypeSerieMapper

        # Convertir les volumes (liste)
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])]

        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les publishers
        publishers = [PublisherMapper.from_dict(publisher_data) for publisher_data in response.get("publishers", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response.get("types", [])]

        # Convertir les box_volumes
        box_volumes = [
            BoxVolumeMapper.from_dict(box_volume_data) for box_volume_data in response.get("box_volumes", [])
        ]

        # Convertir les boxes
        boxes = [BoxMapper.from_dict(box_data) for box_data in response.get("boxes", [])]

        # Convertir les box_editions
        box_editions = [
            BoxEditionMapper.from_dict(box_edition_data) for box_edition_data in response.get("box_editions", [])
        ]

        return GetVolumeByIdV2Response(
            volumes=volumes,
            editions=editions,
            publishers=publishers,
            series=series,
            types=types,
            box_volumes=box_volumes,
            boxes=boxes,
            box_editions=box_editions,
        )

    @staticmethod
    def from_volumes_news_response(response: dict) -> GetVolumesNewsV2Response:
        """Convertit la réponse de l'API V2 pour get_volumes_news en GetVolumesNewsV2Response.

        Cette méthode diffère de from_api_response car:
        - Pas de publishers dans la réponse
        - Ajout d'un champ native_ad_volume_home_first optionnel

        Args:
            response: Réponse API contenant volumes récents et publicité native optionnelle

        Returns:
            GetVolumesNewsV2Response contenant toutes les entités et la publicité native
        """
        # Import local pour éviter l'import circulaire
        from mangacollec.application.mappers.box_edition_mapper import BoxEditionMapper
        from mangacollec.application.mappers.box_mapper import BoxMapper
        from mangacollec.application.mappers.box_volume_mapper import BoxVolumeMapper
        from mangacollec.application.mappers.edition_mapper import EditionMapper
        from mangacollec.application.mappers.native_ad_volume_home_first_mapper import (
            NativeAdVolumeHomeFirstMapper,
        )
        from mangacollec.application.mappers.serie_mapper import SerieMapper
        from mangacollec.application.mappers.type_serie_mapper import TypeSerieMapper

        # Convertir les volumes (liste)
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])]

        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response.get("types", [])]

        # Convertir les box_volumes
        box_volumes = [
            BoxVolumeMapper.from_dict(box_volume_data) for box_volume_data in response.get("box_volumes", [])
        ]

        # Convertir les boxes
        boxes = [BoxMapper.from_dict(box_data) for box_data in response.get("boxes", [])]

        # Convertir les box_editions
        box_editions = [
            BoxEditionMapper.from_dict(box_edition_data) for box_edition_data in response.get("box_editions", [])
        ]

        # Convertir la publicité native (optionnelle)
        native_ad_data = response.get("native_ad_volume_home_first")
        native_ad = NativeAdVolumeHomeFirstMapper.from_dict(native_ad_data) if native_ad_data else None

        return GetVolumesNewsV2Response(
            volumes=volumes,
            editions=editions,
            series=series,
            types=types,
            box_volumes=box_volumes,
            boxes=boxes,
            box_editions=box_editions,
            native_ad_volume_home_first=native_ad,
        )
