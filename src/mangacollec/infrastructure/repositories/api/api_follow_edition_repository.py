"""API Follow Edition Repository implementation."""

from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import FollowEditionMapper
from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.exceptions import (
    FollowEditionNotFoundException,
    FollowEditionOperationException,
)
from mangacollec.domain.repositories import IFollowEditionRepository


class APIFollowEditionRepository(IFollowEditionRepository):
    """Implémentation du repository FollowEdition via MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def follow_edition_v1(self, edition_id: str, following: bool) -> FollowEdition:
        """Suit ou arrête de suivre une édition via l'API.

        Args:
            edition_id: Identifiant de l'édition à suivre/arrêter de suivre
            following: True pour suivre, False pour arrêter de suivre

        Returns:
            FollowEdition: L'objet FollowEdition créé/mis à jour

        Raises:
            FollowEditionOperationException: Si l'opération échoue
        """
        try:
            payload = {"edition_id": edition_id, "following": following}
            response = self.client_api.post("/v1/follow-editions", data=payload)

            # Délégation au mapper
            return FollowEditionMapper.from_dict(response)

        except Exception as e:
            raise FollowEditionOperationException(f"Failed to follow/unfollow edition '{edition_id}': {e}") from e

    def unfollow_edition_v1(self, follow_edition_id: str) -> bool:
        """Supprime un suivi d'édition via l'API.

        Args:
            follow_edition_id: Identifiant du suivi d'édition à supprimer

        Returns:
            bool: True si la suppression a réussi, False sinon

        Raises:
            FollowEditionNotFoundException: Si le suivi d'édition n'existe pas
        """
        try:
            # L'API retourne un objet JSON avec les données du suivi supprimé
            self.client_api.delete(f"/v1/follow-editions/{follow_edition_id}")
            return True

        except Exception as e:
            if "404" in str(e):
                raise FollowEditionNotFoundException(follow_edition_id) from e
            raise FollowEditionOperationException(f"Failed to delete follow edition '{follow_edition_id}': {e}") from e
