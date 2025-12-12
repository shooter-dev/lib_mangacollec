"""Implémentation en mémoire du repository Kind."""

from mangacollec.application.dto import GetAllKindsV1Response, GetAllKindsV2Response
from mangacollec.domain.entities import Kind
from mangacollec.domain.repositories import IKindRepository


class InMemoryKindRepository(IKindRepository):
    """Implémentation en mémoire du repository Kind (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un stockage en mémoire."""
        self._data: dict[str, Kind] = {}

    def get_all_kinds_v1(self) -> GetAllKindsV1Response:
        """Récupère tous les kinds (version V1).

        Returns:
            GetAllKindsV1Response contenant la liste des kinds
        """
        kinds = list(self._data.values())
        return GetAllKindsV1Response(kinds=kinds)

    def get_all_kinds_v2(self) -> GetAllKindsV2Response:
        """Récupère tous les kinds (version V2).

        Returns:
            GetAllKindsV2Response contenant la liste des kinds
        """
        kinds = list(self._data.values())
        return GetAllKindsV2Response(kinds=kinds)

    def add(self, kind: Kind) -> None:
        """Ajoute un kind au repository.

        Args:
            kind: Kind à ajouter
        """
        self._data[kind.id] = kind

    def clear(self) -> None:
        """Supprime tous les kinds du repository."""
        self._data.clear()
