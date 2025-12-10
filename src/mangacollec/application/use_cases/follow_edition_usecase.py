"""Follow Edition use cases."""

from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.repositories import IFollowEditionRepository


class FollowEditionV1UseCase:
    """Cas d'utilisation : suivre ou arrêter de suivre une édition."""

    def __init__(self, repo: IFollowEditionRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository pour les opérations de suivi d'édition
        """
        self.repo = repo

    def __call__(self, edition_id: str, following: bool) -> FollowEdition:
        """Suit ou arrête de suivre une édition.

        Args:
            edition_id: Identifiant de l'édition à suivre/arrêter de suivre
            following: True pour suivre, False pour arrêter de suivre

        Returns:
            FollowEdition: L'objet FollowEdition créé/mis à jour

        Raises:
            FollowEditionOperationException: Si l'opération échoue
        """
        return self.repo.follow_edition_v1(edition_id, following)


class UnfollowEditionV1UseCase:
    """Cas d'utilisation : supprimer un suivi d'édition."""

    def __init__(self, repo: IFollowEditionRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository pour les opérations de suivi d'édition
        """
        self.repo = repo

    def __call__(self, follow_edition_id: str) -> bool:
        """Supprime un suivi d'édition.

        Args:
            follow_edition_id: Identifiant du suivi d'édition à supprimer

        Returns:
            bool: True si la suppression a réussi, False sinon

        Raises:
            FollowEditionNotFoundException: Si le suivi d'édition n'existe pas
        """
        return self.repo.unfollow_edition_v1(follow_edition_id)
