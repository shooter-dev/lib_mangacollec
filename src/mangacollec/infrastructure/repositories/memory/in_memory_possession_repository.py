"""In-memory Possession Repository."""

from datetime import datetime

from mangacollec.application.dto import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.domain.entities import (
    FollowEdition,
    FollowEditionDeleted,
    LoanDeleted,
    Possession,
    PossessionDeleted,
)
from mangacollec.domain.repositories import IPossessionRepository


class InMemoryPossessionRepository(IPossessionRepository):
    """Implémentation en mémoire du repository Possession (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec des structures de données vides."""
        self._possessions: dict[str, Possession] = {}
        self._follow_editions: dict[str, FollowEdition] = {}
        self._loans: dict[str, dict] = {}

    def add_possessions_multiple_v1(self, volume_ids: list[str]) -> AddPossessionsMultipleV1Response:
        """Ajoute plusieurs possessions de volumes à la collection.

        Args:
            volume_ids: Liste des IDs de volumes à ajouter

        Returns:
            AddPossessionsMultipleV1Response: Réponse contenant les possessions et suivis créés
        """
        possessions_created = []
        follow_editions_created = []

        for volume_id in volume_ids:
            # Créer une possession
            possession_id = f"possession-{len(self._possessions) + 1}"
            possession = Possession(
                id=possession_id,
                user_id="user-test",
                volume_id=volume_id,
                created_at=datetime.now(),
            )
            self._possessions[possession_id] = possession
            possessions_created.append(possession)

            # Créer un suivi d'édition (simulation)
            follow_edition_id = f"follow-edition-{len(self._follow_editions) + 1}"
            follow_edition = FollowEdition(
                id=follow_edition_id,
                user_id="user-test",
                edition_id=f"edition-{volume_id}",
                following=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            self._follow_editions[follow_edition_id] = follow_edition
            follow_editions_created.append(follow_edition)

        return AddPossessionsMultipleV1Response(
            possessions=possessions_created,
            follow_editions=follow_editions_created,
        )

    def delete_possessions_multiple_v1(self, possession_ids: list[str]) -> DeletePossessionsMultipleV1Response:
        """Supprime plusieurs possessions de la collection.

        Args:
            possession_ids: Liste des IDs de possessions à supprimer

        Returns:
            DeletePossessionsMultipleV1Response: Réponse contenant les entités supprimées
        """
        possessions_deleted = []
        follow_editions_deleted = []
        loans_deleted = []

        for possession_id in possession_ids:
            if possession_id in self._possessions:
                # Supprimer la possession
                del self._possessions[possession_id]
                possessions_deleted.append(PossessionDeleted(id=possession_id, deleted=True))

                # Simuler la suppression d'un suivi d'édition
                follow_edition_id = f"follow-edition-{possession_id}"
                follow_editions_deleted.append(FollowEditionDeleted(id=follow_edition_id, deleted=True))

                # Simuler la suppression d'un prêt si existant
                if possession_id in self._loans:
                    loan_id = f"loan-{possession_id}"
                    del self._loans[possession_id]
                    loans_deleted.append(LoanDeleted(id=loan_id, deleted=True))

        return DeletePossessionsMultipleV1Response(
            possessions=possessions_deleted,
            follow_editions=follow_editions_deleted,
            loans=loans_deleted,
        )
