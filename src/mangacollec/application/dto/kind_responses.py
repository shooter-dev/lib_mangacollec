"""DTOs de réponse pour les Kinds."""

from dataclasses import dataclass

from mangacollec.domain.entities import Kind


@dataclass(frozen=True)
class GetAllKindsV1Response:
    """Réponse de l'API V1 pour récupérer tous les kinds.

    Attributes:
        kinds: Liste des kinds récupérés
    """

    kinds: list[Kind]


@dataclass(frozen=True)
class GetAllKindsV2Response:
    """Réponse de l'API V2 pour récupérer tous les kinds.

    Attributes:
        kinds: Liste des kinds récupérés
    """

    kinds: list[Kind]
