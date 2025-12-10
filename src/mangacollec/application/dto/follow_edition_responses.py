"""Follow Edition DTOs for responses."""

from dataclasses import dataclass

from mangacollec.domain.entities import FollowEdition


@dataclass(frozen=True)
class FollowEditionV1Response:
    """DTO pour la réponse de suivi d'une édition (V1).

    Attributes:
        follow_edition: L'objet FollowEdition créé/mis à jour
    """

    follow_edition: FollowEdition
