"""Implémentation en mémoire du repository Serie pour les tests.

This module provides an in-memory implementation of the Serie repository for testing.
"""

from mangacollec.application.dto import GetAllSeriesV2Response, GetSerieByIdV2Response
from mangacollec.domain.entities import Serie, TypeSerie
from mangacollec.domain.exceptions import SerieNotFoundException
from mangacollec.domain.repositories import ISerieRepository


class InMemorySerieRepository(ISerieRepository):
    """Implémentation en mémoire du repository Serie (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un dictionnaire vide."""
        self._data: dict[str, Serie] = {}
        self._types: dict[str, TypeSerie] = {}

    def get_serie_by_id_v2(self, serie_id: str) -> GetSerieByIdV2Response:
        """Récupère une série par son ID avec toutes ses relations.

        Args:
            serie_id: UUID de la série

        Returns:
            GetSerieByIdV2Response contenant:
                - series: Liste des séries (1 seul élément)
                - types: Liste des types (vide pour InMemory)
                - kinds: Liste des genres (vide pour InMemory)
                - tasks: Liste des tâches (vide pour InMemory)
                - jobs: Liste des rôles/métiers (vide pour InMemory)
                - authors: Liste des auteurs (vide pour InMemory)
                - editions: Liste des éditions (vide pour InMemory)
                - publishers: Liste des éditeurs (vide pour InMemory)
                - volumes: Liste des volumes (vide pour InMemory)
                - box_editions: Liste des box éditions (vide pour InMemory)
                - boxes: Liste des coffrets (vide pour InMemory)
                - box_volumes: Liste des volumes dans coffrets (vide pour InMemory)

        Raises:
            SerieNotFoundException: Si la série n'existe pas

        Note:
            Cette implémentation retourne des listes vides pour les relations.
            Pour les tests nécessitant des relations, utiliser le mock API repository.
        """
        serie = self._data.get(serie_id)
        if serie is None:
            raise SerieNotFoundException(serie_id)

        return GetSerieByIdV2Response(
            series=[serie],
            types=[],
            kinds=[],
            tasks=[],
            jobs=[],
            authors=[],
            editions=[],
            publishers=[],
            volumes=[],
            box_editions=[],
            boxes=[],
            box_volumes=[],
        )

    def get_all_series_v2(self) -> GetAllSeriesV2Response:
        """Récupère toutes les séries avec leurs types.

        Returns:
            GetAllSeriesV2Response contenant la liste des séries et types
        """
        return GetAllSeriesV2Response(series=list(self._data.values()), types=list(self._types.values()))

    def add(self, serie: Serie) -> Serie:
        """Ajoute une série au repository (méthode pour les tests).

        Args:
            serie: Entité Serie à ajouter

        Returns:
            L'entité Serie ajoutée
        """
        self._data[serie.id] = serie
        return serie

    def add_type(self, type_serie: TypeSerie) -> TypeSerie:
        """Ajoute un type de série au repository (méthode pour les tests).

        Args:
            type_serie: Entité TypeSerie à ajouter

        Returns:
            L'entité TypeSerie ajoutée
        """
        self._types[type_serie.id] = type_serie
        return type_serie

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._data.clear()
        self._types.clear()
