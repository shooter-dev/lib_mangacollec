"""Implémentation en mémoire du repository Edition pour les tests.

This module provides an in-memory implementation of the Edition repository for testing.
"""

from mangacollec.application.dto import GetEditionByIdV2Response
from mangacollec.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume
from mangacollec.domain.exceptions import EditionNotFoundException
from mangacollec.domain.repositories import (
    IEditionRepository,
)


class InMemoryEditionRepository(IEditionRepository):
    """Implémentation en mémoire du repository Edition (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec des dictionnaires vides."""
        self._editions: dict[str, Edition] = {}
        self._publishers: dict[str, Publisher] = {}
        self._series: dict[str, Serie] = {}
        self._types: dict[str, TypeSerie] = {}
        self._volumes: dict[str, list[Volume]] = {}  # Clé: edition_id

    def get_edition_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
        """Récupère une édition par son ID avec toutes les entités associées.

        Args:
            edition_id: UUID de l'édition

        Returns:
            GetEditionByIdV2Response contenant:
                - editions: Liste des éditions (1 seul élément)
                - publishers: Liste des publishers (1 seul)
                - series: Liste des séries
                - types: Liste des types de séries
                - volumes: Liste des volumes

        Raises:
            EditionNotFoundException: Si l'édition n'existe pas

        Note:
            Cette implémentation retourne des listes minimales pour les tests.
            Pour les tests nécessitant des relations complètes, utiliser le mock API repository.
        """
        edition = self._editions.get(edition_id)
        if edition is None:
            raise EditionNotFoundException(edition_id)

        # Récupérer le publisher associé
        publisher = self._publishers.get(edition.publisher_id)
        if publisher is None:
            # Créer un publisher par défaut si non trouvé
            publisher = Publisher(
                id=edition.publisher_id,
                title="Unknown Publisher",
                closed=False,
                editions_count=0,
                no_amazon=False,
            )

        # Récupérer la série associée
        serie = self._series.get(edition.series_id)
        series = [serie] if serie else []

        # Récupérer le type de série associé
        types = []
        if serie:
            type_serie = self._types.get(serie.type_id)
            if type_serie:
                types = [type_serie]

        # Récupérer les volumes associés à cette édition
        volumes = self._volumes.get(edition_id, [])

        return GetEditionByIdV2Response(
            editions=[edition],
            publishers=[publisher],
            series=series,
            types=types,
            volumes=volumes,
        )

    def add_edition(self, edition: Edition) -> Edition:
        """Ajoute une édition au repository (méthode pour les tests).

        Args:
            edition: Entité Edition à ajouter

        Returns:
            L'entité Edition ajoutée
        """
        self._editions[edition.id] = edition
        return edition

    def add_publisher(self, publisher: Publisher) -> Publisher:
        """Ajoute un publisher au repository (méthode pour les tests).

        Args:
            publisher: Entité Publisher à ajouter

        Returns:
            L'entité Publisher ajoutée
        """
        self._publishers[publisher.id] = publisher
        return publisher

    def add_serie(self, serie: Serie) -> Serie:
        """Ajoute une série au repository (méthode pour les tests).

        Args:
            serie: Entité Serie à ajouter

        Returns:
            L'entité Serie ajoutée
        """
        self._series[serie.id] = serie
        return serie

    def add_type(self, type_serie: TypeSerie) -> TypeSerie:
        """Ajoute un type de série au repository (méthode pour les tests).

        Args:
            type_serie: Entité Type à ajouter

        Returns:
            L'entité Type ajoutée
        """
        self._types[type_serie.id] = type_serie
        return type_serie

    def add_volumes(self, edition_id: str, volumes: list[Volume]) -> list[Volume]:
        """Ajoute des volumes au repository (méthode pour les tests).

        Args:
            edition_id: ID de l'édition
            volumes: Liste des volumes à ajouter

        Returns:
            La liste des volumes ajoutés
        """
        self._volumes[edition_id] = volumes
        return volumes

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._editions.clear()
        self._publishers.clear()
        self._series.clear()
        self._types.clear()
        self._volumes.clear()
