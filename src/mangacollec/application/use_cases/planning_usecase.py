"""Use cases pour Planning.

This module contains use cases for Planning operations.
"""

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.domain.repositories import IPlanningRepository


class GetPlanningV2UseCase:
    """Cas d'utilisation : récupérer le planning V2 pour un mois donné."""

    def __init__(self, repo: IPlanningRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository Planning
        """
        self.repo = repo

    def __call__(self, month: str) -> GetPlanningV2Response:
        """Récupère le planning pour un mois donné.

        Args:
            month: Date au format YYYY-MM-DD (ex: "2022-09-30")

        Returns:
            GetPlanningV2Response contenant tous les volumes, boxes et entités liées

        Raises:
            ValueError: Si le format de la date est invalide
        """
        return self.repo.get_planning_v2(month)
