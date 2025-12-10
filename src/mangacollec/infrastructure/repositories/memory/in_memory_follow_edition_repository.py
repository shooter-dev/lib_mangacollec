"""InMemory Follow Edition Repository implementation."""

import uuid
from datetime import datetime, timezone

from mangacollec.domain.entities import FollowEdition
from mangacollec.domain.exceptions import FollowEditionNotFoundException
from mangacollec.domain.repositories import IFollowEditionRepository


class InMemoryFollowEditionRepository(IFollowEditionRepository):
    """Implémentation en mémoire du repository FollowEdition (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un stockage en mémoire vide."""
        self._data: dict[str, FollowEdition] = {}
        self._user_id = "test-user-id"  # ID utilisateur fictif pour les tests

    def follow_edition_v1(self, edition_id: str, following: bool) -> FollowEdition:
        """Suit ou arrête de suivre une édition.

        Args:
            edition_id: Identifiant de l'édition à suivre/arrêter de suivre
            following: True pour suivre, False pour arrêter de suivre

        Returns:
            FollowEdition: L'objet FollowEdition créé/mis à jour
        """
        # Chercher un suivi existant pour cette édition
        existing_follow = None
        for follow in self._data.values():
            if follow.edition_id == edition_id and follow.user_id == self._user_id:
                existing_follow = follow
                break

        now = datetime.now(timezone.utc)

        if existing_follow:
            # Mise à jour du suivi existant
            updated_follow = FollowEdition(
                id=existing_follow.id,
                user_id=existing_follow.user_id,
                edition_id=existing_follow.edition_id,
                following=following,
                created_at=existing_follow.created_at,
                updated_at=now,
            )
            self._data[updated_follow.id] = updated_follow
            return updated_follow
        else:
            # Création d'un nouveau suivi
            new_follow = FollowEdition(
                id=str(uuid.uuid4()),
                user_id=self._user_id,
                edition_id=edition_id,
                following=following,
                created_at=now,
                updated_at=now,
            )
            self._data[new_follow.id] = new_follow
            return new_follow

    def unfollow_edition_v1(self, follow_edition_id: str) -> bool:
        """Supprime un suivi d'édition.

        Args:
            follow_edition_id: Identifiant du suivi d'édition à supprimer

        Returns:
            bool: True si la suppression a réussi, False sinon

        Raises:
            FollowEditionNotFoundException: Si le suivi d'édition n'existe pas
        """
        if follow_edition_id not in self._data:
            raise FollowEditionNotFoundException(follow_edition_id)

        del self._data[follow_edition_id]
        return True

    def get_by_id(self, follow_edition_id: str) -> FollowEdition | None:
        """Récupère un suivi d'édition par son ID.

        Args:
            follow_edition_id: Identifiant du suivi d'édition

        Returns:
            FollowEdition | None: Le suivi d'édition trouvé ou None
        """
        return self._data.get(follow_edition_id)

    def get_all(self) -> list[FollowEdition]:
        """Récupère tous les suivis d'édition.

        Returns:
            list[FollowEdition]: Liste de tous les suivis d'édition
        """
        return list(self._data.values())

    def clear(self) -> None:
        """Vide le stockage en mémoire (utile pour les tests)."""
        self._data.clear()
