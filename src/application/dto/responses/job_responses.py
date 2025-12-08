"""DTOs de réponse pour la ressource Job."""

from dataclasses import dataclass

from src.domain.entities.job import Job


@dataclass(frozen=True)
class GetAllJobsV1Response:
    """DTO de réponse pour l'endpoint GET /v1/jobs/.

    Attributes:
        jobs: Liste des jobs retournés par l'API
    """

    jobs: list[Job]
