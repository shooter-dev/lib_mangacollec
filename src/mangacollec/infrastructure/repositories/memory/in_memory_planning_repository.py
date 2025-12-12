"""Implémentation en mémoire du repository Planning pour les tests.

This module provides an in-memory implementation of the Planning repository.
"""

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.domain.entities import (
    Box,
    BoxEdition,
    BoxVolume,
    Edition,
    Serie,
    TypeSerie,
    Volume,
)
from mangacollec.domain.repositories import IPlanningRepository


class InMemoryPlanningRepository(IPlanningRepository):
    """Implémentation en mémoire du repository Planning (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec des listes vides."""
        self._planning_data: dict[str, GetPlanningV2Response] = {}

    def get_planning_v2(self, month: str) -> GetPlanningV2Response:
        """Récupère le planning des volumes pour un mois donné.

        Args:
            month: Date au format YYYY-MM-DD (ex: "2022-09-30")

        Returns:
            GetPlanningV2Response contenant tous les volumes, boxes et entités liées

        Raises:
            ValueError: Si le format de la date est invalide
        """
        # Retourner les données si elles existent, sinon retourner une réponse vide
        return self._planning_data.get(
            month,
            GetPlanningV2Response(
                volumes=[], editions=[], series=[], types=[], boxes=[], box_editions=[], box_volumes=[]
            ),
        )

    def add_planning(
        self,
        month: str,
        volumes: list[Volume] | None = None,
        editions: list[Edition] | None = None,
        series: list[Serie] | None = None,
        types: list[TypeSerie] | None = None,
        boxes: list[Box] | None = None,
        box_editions: list[BoxEdition] | None = None,
        box_volumes: list[BoxVolume] | None = None,
    ) -> None:
        """Ajoute un planning au repository (utile pour les tests).

        Args:
            month: Date au format YYYY-MM-DD
            volumes: Liste de volumes
            editions: Liste d'éditions
            series: Liste de séries
            types: Liste de types
            boxes: Liste de boxes
            box_editions: Liste de box_editions
            box_volumes: Liste de box_volumes
        """
        self._planning_data[month] = GetPlanningV2Response(
            volumes=volumes or [],
            editions=editions or [],
            series=series or [],
            types=types or [],
            boxes=boxes or [],
            box_editions=box_editions or [],
            box_volumes=box_volumes or [],
        )

    def clear(self) -> None:
        """Vide le repository (utile pour les tests)."""
        self._planning_data.clear()
