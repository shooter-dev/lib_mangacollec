"""Use cases pour la ressource Job."""

from mangacollec.domain.entities.job import Job
from mangacollec.domain.repositories.i_job_repository import IJobRepository


class GetAllJobsV1UseCase:
    """Cas d'utilisation : récupérer tous les jobs via l'API V1.

    Ce use case permet de récupérer la liste complète des jobs (métiers/rôles)
    disponibles dans la base de données.
    """

    def __init__(self, repository: IJobRepository) -> None:
        """Initialise le use case avec un repository.

        Args:
            repository: Repository Job implémentant IJobRepository
        """
        self.repository = repository

    def __call__(self) -> list[Job]:
        """Exécute le use case.

        Returns:
            Liste des jobs disponibles
        """
        response = self.repository.get_all()
        return response.jobs
