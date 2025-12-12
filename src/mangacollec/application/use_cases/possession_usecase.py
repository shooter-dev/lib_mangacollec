"""Possession use cases."""

from mangacollec.application.dto.possession_responses import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.domain.repositories import IPossessionRepository


class AddPossessionsMultipleV1UseCase:
    """Cas d'utilisation : ajouter plusieurs possessions de volumes."""

    def __init__(self, repo: IPossessionRepository) -> None:
        """Initialise le use case avec le repository.

        Args:
            repo: Repository des possessions
        """
        self.repo = repo

    def __call__(self, volume_ids: list[str]) -> AddPossessionsMultipleV1Response:
        """Ajoute plusieurs volumes à la collection.

        Args:
            volume_ids: Liste des IDs de volumes à ajouter

        Returns:
            AddPossessionsMultipleV1Response: Réponse contenant les possessions et suivis créés
        """
        return self.repo.add_possessions_multiple_v1(volume_ids)


class DeletePossessionsMultipleV1UseCase:
    """Cas d'utilisation : supprimer plusieurs possessions de volumes."""

    def __init__(self, repo: IPossessionRepository) -> None:
        """Initialise le use case avec le repository.

        Args:
            repo: Repository des possessions
        """
        self.repo = repo

    def __call__(self, possession_ids: list[str]) -> DeletePossessionsMultipleV1Response:
        """Supprime plusieurs possessions de la collection.

        Args:
            possession_ids: Liste des IDs de possessions à supprimer

        Returns:
            DeletePossessionsMultipleV1Response: Réponse contenant les entités supprimées
        """
        return self.repo.delete_possessions_multiple_v1(possession_ids)
