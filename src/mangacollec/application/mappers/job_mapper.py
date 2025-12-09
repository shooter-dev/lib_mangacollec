"""Mapper pour la conversion entre les réponses API et les entités Job.

This module provides mapping functions between API responses and Job entities.
"""

from mangacollec.application.dto import GetAllJobsV1Response
from mangacollec.domain.entities import Job


class JobMapper:
    """Mapper pour convertir entre API et entités du domaine."""

    @staticmethod
    def from_dict(data: dict) -> Job:
        """Convertit la réponse API en entité Job.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité Job
        """
        return Job(
            id=data["id"],
            title=data["title"],
        )

    @staticmethod
    def to_dict(job: Job) -> dict:
        """Convertit l'entité Job en dictionnaire.

        Args:
            job: Entité Job

        Returns:
            Dictionnaire représentant le job
        """
        return {
            "id": job.id,
            "title": job.title,
        }

    @staticmethod
    def from_all_jobs_response(response: list) -> GetAllJobsV1Response:
        """Convertit la réponse de l'API V1 pour get_all en GetAllJobsV1Response.

        Args:
            response: Réponse API contenant la liste des jobs (tableau direct)

        Returns:
            GetAllJobsV1Response contenant la liste des jobs
        """
        # L'API V1 retourne directement un tableau, pas un objet avec clé "jobs"
        jobs = [JobMapper.from_dict(job_data) for job_data in response]

        return GetAllJobsV1Response(jobs=jobs)
