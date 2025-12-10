"""Mapper pour la conversion entre les réponses API et les entités Author.

This module provides mapping functions between API responses and Author entities.
"""

from mangacollec.application.dto import (GetAllAuthorsV2Response,
                                         GetAuthorByIdV2Response)
from mangacollec.application.mappers.edition_mapper import EditionMapper
from mangacollec.application.mappers.job_mapper import JobMapper
from mangacollec.application.mappers.serie_mapper import SerieMapper
from mangacollec.application.mappers.task_mapper import TaskMapper
from mangacollec.application.mappers.volume_mapper import VolumeMapper
from mangacollec.domain.entities import Author, AuthorListItem


class AuthorMapper:
    """Mapper pour convertir entre API et entités du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Author:
        """Convertit la réponse API en entité Author.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Author
        """
        return Author(
            id=data["id"],
            name=data["name"],
            first_name=data.get("first_name"),
            tasks_count=data.get("tasks_count", 0),
        )

    @staticmethod
    def to_dict(author: Author) -> dict:
        """Convertit l'entité Author en dictionnaire.

        Args:
            author: Entité Author

        Returns:
            Dictionnaire représentant l'auteur
        """
        return {
            "id": author.id,
            "name": author.name,
            "first_name": author.first_name,
            "tasks_count": author.tasks_count,
        }

    @staticmethod
    def to_list_item(author: Author) -> AuthorListItem:
        """Convertit une entité Author en AuthorListItem.

        Args:
            author: Entité Author

        Returns:
            Entité AuthorListItem avec id et full_name
        """
        first_name = author.first_name if author.first_name else ""
        full_name = f"{first_name} {author.name}".strip()

        return AuthorListItem(
            id=author.id,
            full_name=full_name,
        )

    @staticmethod
    def from_all_authors_response(response: dict) -> GetAllAuthorsV2Response:
        """Convertit la réponse de l'API V2 pour get_all en GetAllAuthorsV2Response.

        Args:
            response: Réponse API contenant authors

        Returns:
            GetAllAuthorsV2Response contenant la liste des auteurs
        """
        # Convertir les authors
        authors = [AuthorMapper.from_dict(author_data) for author_data in response.get("authors", [])]

        return GetAllAuthorsV2Response(authors=authors)

    @staticmethod
    def from_api_response(response: dict) -> GetAuthorByIdV2Response:
        """Convertit la réponse complète de l'API V2 en GetAuthorByIdV2Response.

        Args:
            response: Réponse API contenant authors, tasks, jobs, series, editions, volumes

        Returns:
            GetAuthorByIdV2Response contenant toutes les entités converties
        """
        # Convertir les authors (liste)
        authors = [AuthorMapper.from_dict(author_data) for author_data in response.get("authors", [])]

        # Convertir les tasks
        tasks = [TaskMapper.from_dict(task_data) for task_data in response.get("tasks", [])]

        # Convertir les jobs
        jobs = [JobMapper.from_dict(job_data) for job_data in response.get("jobs", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les volumes
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response.get("volumes", [])]

        return GetAuthorByIdV2Response(
            authors=authors,
            tasks=tasks,
            jobs=jobs,
            series=series,
            editions=editions,
            volumes=volumes,
        )
