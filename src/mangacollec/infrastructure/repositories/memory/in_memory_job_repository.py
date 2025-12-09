"""Implémentation en mémoire du repository Job pour les tests."""

from mangacollec.application.dto import GetAllJobsV1Response
from mangacollec.domain.entities import Job
from mangacollec.domain.repositories import IJobRepository


class InMemoryJobRepository(IJobRepository):
    """Implémentation en mémoire du repository Job (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un dictionnaire vide."""
        self._jobs: dict[str, Job] = {}

    def get_all(self) -> GetAllJobsV1Response:
        """Récupère tous les jobs.

        Returns:
            GetAllJobsV1Response contenant la liste des jobs
        """
        return GetAllJobsV1Response(jobs=list(self._jobs.values()))

    def add(self, job: Job) -> None:
        """Ajoute un job au repository (utile pour les tests).

        Args:
            job: Job à ajouter
        """
        self._jobs[job.id] = job

    def clear(self) -> None:
        """Vide le repository (utile pour les tests)."""
        self._jobs.clear()
