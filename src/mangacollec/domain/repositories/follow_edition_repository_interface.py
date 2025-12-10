"""Follow Edition repository interface."""

from abc import ABC, abstractmethod

from mangacollec.domain.entities import FollowEdition


class IFollowEditionRepository(ABC):
    """Interface du repository pour FollowEdition."""

    @abstractmethod
    def follow_edition_v1(self, edition_id: str, following: bool) -> FollowEdition:
        """Suit ou arrête de suivre une édition.

        Args:
            edition_id: Identifiant de l'édition à suivre/arrêter de suivre
            following: True pour suivre, False pour arrêter de suivre

        Returns:
            FollowEdition: L'objet FollowEdition créé/mis à jour

        Raises:
            FollowEditionOperationException: Si l'opération échoue
        """
        pass

    @abstractmethod
    def unfollow_edition_v1(self, follow_edition_id: str) -> bool:
        """Supprime un suivi d'édition.

        Args:
            follow_edition_id: Identifiant du suivi d'édition à supprimer

        Returns:
            bool: True si la suppression a réussi, False sinon

        Raises:
            FollowEditionNotFoundException: Si le suivi d'édition n'existe pas
        """
        pass
