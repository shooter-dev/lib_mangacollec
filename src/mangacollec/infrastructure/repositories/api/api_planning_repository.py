"""Implémentation du repository Planning via MangaCollecAPI.

This module provides the API implementation of the Planning repository.
"""

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers.planning_mapper import PlanningMapper
from mangacollec.domain.repositories import IPlanningRepository


class APIPlanningRepository(IPlanningRepository):
    """Implémentation du repository Planning via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_planning_v2(self, month: str) -> GetPlanningV2Response:
        """Récupère le planning des volumes pour un mois donné via l'API V2.

        Args:
            month: Date au format YYYY-MM-DD (ex: "2022-09-30")

        Returns:
            GetPlanningV2Response contenant tous les volumes, boxes et entités liées

        Raises:
            ValueError: Si le format de la date est invalide
            RuntimeError: Si la récupération échoue
        """
        try:
            response = self.client_api.get(f"/v2/planning/?month={month}")

            # Délégation au mapper
            return PlanningMapper.from_planning_v2_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve planning for month {month}: {e}") from e
