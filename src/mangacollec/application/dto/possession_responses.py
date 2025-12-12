"""Possession responses DTOs."""

from dataclasses import dataclass

from mangacollec.domain.entities import (FollowEdition, FollowEditionDeleted,
                                         LoanDeleted, Possession,
                                         PossessionDeleted)


@dataclass(frozen=True)
class AddPossessionsMultipleV1Response:
    """Réponse pour l'ajout multiple de possessions.

    Attributes:
        possessions: Liste des possessions créées
        follow_editions: Liste des suivis d'éditions créés automatiquement
    """

    possessions: list[Possession]
    follow_editions: list[FollowEdition]


@dataclass(frozen=True)
class DeletePossessionsMultipleV1Response:
    """Réponse pour la suppression multiple de possessions.

    Attributes:
        possessions: Liste des possessions supprimées
        follow_editions: Liste des suivis d'éditions supprimés automatiquement
        loans: Liste des prêts supprimés automatiquement
    """

    possessions: list[PossessionDeleted]
    follow_editions: list[FollowEditionDeleted]
    loans: list[LoanDeleted]
