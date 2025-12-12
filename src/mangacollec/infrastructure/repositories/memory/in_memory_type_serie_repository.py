"""In-memory TypeSerie repository implementation."""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.domain.entities import TypeSerie
from mangacollec.domain.repositories import ITypeSerieRepository


class InMemoryTypeSerieRepository(ITypeSerieRepository):
    """Implémentation en mémoire du repository TypeSerie pour les tests."""

    def __init__(self) -> None:
        """Initialise le repository avec un stockage en mémoire."""
        self._data: dict[str, TypeSerie] = {}

    def get_all_types_v1(self) -> GetAllTypesSerieV1Response:
        """Récupère tous les types de séries.

        Returns:
            GetAllTypesSerieV1Response contenant tous les types stockés
        """
        types = list(self._data.values())
        return GetAllTypesSerieV1Response(types=types)

    def add(self, type_serie: TypeSerie) -> None:
        """Ajoute un type de série au repository (méthode helper pour les tests).

        Args:
            type_serie: Type de série à ajouter
        """
        self._data[type_serie.id] = type_serie

    def clear(self) -> None:
        """Vide le repository (méthode helper pour les tests)."""
        self._data.clear()
