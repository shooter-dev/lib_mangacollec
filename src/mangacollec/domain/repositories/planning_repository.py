"""Interface du repository Planning.

This module defines the repository interface for Planning operations.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetPlanningV2Response


class IPlanningRepository(ABC):
    """Interface du repository pour Planning."""

    @abstractmethod
    def get_planning_v2(self, month: str) -> GetPlanningV2Response:
        """Récupère le planning des volumes pour un mois donné via l'API V2.

        Args:
            month: Date au format YYYY-MM-DD (ex: "2022-09-30")

        Returns:
            GetPlanningV2Response contenant tous les volumes, boxes et entités liées

        Raises:
            ValueError: Si le format de la date est invalide
        """
        pass
