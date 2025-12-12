"""Mapper pour la conversion entre les réponses API et les entités Serie.

This module provides mapping functions between API responses and Serie entities.
"""

from mangacollec.application.dto import (GetAllSeriesV2Response,
                                         GetSerieByIdV2Response)
from mangacollec.domain.entities import Serie, SerieListItem


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
            kinds_ids=data.get("kinds_ids"),
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
            "kinds_ids": serie.kinds_ids,
        }

    @staticmethod
    def to_list_item(serie: Serie) -> SerieListItem:
        """Convertit une entité Serie en SerieListItem.

        Args:
            serie: Entité Serie

        Returns:
            Entité SerieListItem avec id et title
        """
        return SerieListItem(
            id=serie.id,
            title=serie.title,
        )

    @staticmethod
    def from_all_series_response(response: dict) -> GetAllSeriesV2Response:
        """Convertit la réponse de l'API V2 pour get_all en GetAllSeriesV2Response.

        Args:
            response: Réponse API contenant series et types

        Returns:
            GetAllSeriesV2Response contenant la liste des séries et types
        """
        from mangacollec.application.mappers.type_mapper import TypeSerieMapper

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response.get("types", [])]

        return GetAllSeriesV2Response(series=series, types=types)

    @staticmethod
    def from_api_response(response: dict) -> GetSerieByIdV2Response:
        """Convertit la réponse complète de l'API V2 en GetSerieByIdV2Response.

        Args:
            response: Réponse API contenant series et toutes les entités liées

        Returns:
            GetSerieByIdV2Response contenant toutes les entités converties
        """
        from mangacollec.application.mappers.author_mapper import AuthorMapper
        from mangacollec.application.mappers.box_edition_mapper import \
            BoxEditionMapper
        from mangacollec.application.mappers.box_mapper import BoxMapper
        from mangacollec.application.mappers.box_volume_mapper import \
            BoxVolumeMapper
        from mangacollec.application.mappers.edition_mapper import \
            EditionMapper
        from mangacollec.application.mappers.job_mapper import JobMapper
        from mangacollec.application.mappers.kind_mapper import KindMapper
        from mangacollec.application.mappers.publisher_mapper import \
            PublisherMapper
        from mangacollec.application.mappers.task_mapper import TaskMapper
        from mangacollec.application.mappers.type_mapper import TypeSerieMapper
        from mangacollec.application.mappers.volume_mapper import VolumeMapper

        # Convertir les series (liste)
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les types
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response.get("types", [])]

        # Convertir les kinds
        kinds = [KindMapper.from_dict(kind_data) for kind_data in response.get("kinds", [])]

        # Convertir les tasks
        tasks = [TaskMapper.from_dict(task_data) for task_data in response.get("tasks", [])]

        # Convertir les jobs
        jobs = [JobMapper.from_dict(job_data) for job_data in response.get("jobs", [])]

        # Convertir les authors
        authors = [AuthorMapper.from_dict(author_data) for author_data in response.get("authors", [])]

        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les publishers
        publishers = [PublisherMapper.from_dict(publisher_data) for publisher_data in response.get("publishers", [])]

        # Convertir les volumes
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])]

        # Convertir les box_editions
        box_editions = [
            BoxEditionMapper.from_dict(box_edition_data) for box_edition_data in response.get("box_editions", [])
        ]

        # Convertir les boxes
        boxes = [BoxMapper.from_dict(box_data) for box_data in response.get("boxes", [])]

        # Convertir les box_volumes
        box_volumes = [
            BoxVolumeMapper.from_dict(box_volume_data) for box_volume_data in response.get("box_volumes", [])
        ]

        return GetSerieByIdV2Response(
            series=series,
            types=types,
            kinds=kinds,
            tasks=tasks,
            jobs=jobs,
            authors=authors,
            editions=editions,
            publishers=publishers,
            volumes=volumes,
            box_editions=box_editions,
            boxes=boxes,
            box_volumes=box_volumes,
        )
