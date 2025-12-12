"""API Possession Repository."""

from mangacollec.application.dto.possession_responses import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import PossessionMapper
from mangacollec.domain.exceptions import (
    PossessionCreationException,
    PossessionDeletionException,
)
from mangacollec.domain.repositories import IPossessionRepository


class APIPossessionRepository(IPossessionRepository):
    """Implémentation du repository Possession via MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def add_possessions_multiple_v1(self, volume_ids: list[str]) -> AddPossessionsMultipleV1Response:
        """Ajoute plusieurs possessions de volumes à la collection.

        Args:
            volume_ids: Liste des IDs de volumes à ajouter

        Returns:
            AddPossessionsMultipleV1Response: Réponse contenant les possessions et suivis créés

        Raises:
            PossessionCreationException: Si l'ajout échoue
        """
        try:
            data = {"volume_ids": volume_ids}
            response = self.client_api.post("/v1/possessions_multiple", data=data)

            return PossessionMapper.from_add_possessions_response(response)

        except Exception as e:
            raise PossessionCreationException(str(e)) from e

    def delete_possessions_multiple_v1(self, possession_ids: list[str]) -> DeletePossessionsMultipleV1Response:
        """Supprime plusieurs possessions de la collection.

        Args:
            possession_ids: Liste des IDs de possessions à supprimer

        Returns:
            DeletePossessionsMultipleV1Response: Réponse contenant les entités supprimées

        Raises:
            PossessionDeletionException: Si la suppression échoue
        """
        try:
            data = {"possession_ids": possession_ids}
            response = self.client_api.delete("/v1/possessions_multiple", data=data)

            return PossessionMapper.from_delete_possessions_response(response)

        except Exception as e:
            raise PossessionDeletionException(str(e)) from e
