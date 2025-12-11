"""Mapper pour la conversion entre les réponses API et les DTOs Planning.

This module provides mapping functions between API responses and Planning DTOs.
"""

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.application.mappers.box_edition_mapper import BoxEditionMapper
from mangacollec.application.mappers.box_mapper import BoxMapper
from mangacollec.application.mappers.box_volume_mapper import BoxVolumeMapper
from mangacollec.application.mappers.edition_mapper import EditionMapper
from mangacollec.application.mappers.serie_mapper import SerieMapper
from mangacollec.application.mappers.type_mapper import TypeSerieMapper
from mangacollec.application.mappers.volume_mapper import VolumeMapper


class PlanningMapper:
    """Mapper pour convertir entre API et DTOs Planning."""

    @staticmethod
    def from_planning_v2_response(response: dict) -> GetPlanningV2Response:
        """Convertit la réponse complète de l'API V2 en GetPlanningV2Response.

        Args:
            response: Réponse API contenant volumes, editions, series, types,
                     boxes, box_editions et box_volumes

        Returns:
            GetPlanningV2Response contenant toutes les entités converties
        """
        # Convertir les volumes
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])]

        # Convertir les éditions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les séries
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response.get("types", [])]

        # Convertir les boxes
        boxes = [BoxMapper.from_dict(box_data) for box_data in response.get("boxes", [])]

        # Convertir les box_editions
        box_editions = [
            BoxEditionMapper.from_dict(box_edition_data) for box_edition_data in response.get("box_editions", [])
        ]

        # Convertir les box_volumes
        box_volumes = [
            BoxVolumeMapper.from_dict(box_volume_data) for box_volume_data in response.get("box_volumes", [])
        ]

        return GetPlanningV2Response(
            volumes=volumes,
            editions=editions,
            series=series,
            types=types,
            boxes=boxes,
            box_editions=box_editions,
            box_volumes=box_volumes,
        )
