"""Possession repository interface."""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)


class IPossessionRepository(ABC):
    """Interface du repository pour Possession."""

    @abstractmethod
    def add_possessions_multiple_v1(self, volume_ids: list[str]) -> AddPossessionsMultipleV1Response:
        """Ajoute plusieurs possessions de volumes à la collection.

        Args:
            volume_ids: Liste des IDs de volumes à ajouter

        Returns:
            AddPossessionsMultipleV1Response: Réponse contenant les possessions et suivis créés
        """
        pass

    @abstractmethod
    def delete_possessions_multiple_v1(self, possession_ids: list[str]) -> DeletePossessionsMultipleV1Response:
        """Supprime plusieurs possessions de la collection.

        Args:
            possession_ids: Liste des IDs de possessions à supprimer

        Returns:
            DeletePossessionsMultipleV1Response: Réponse contenant les entités supprimées
        """
        pass
