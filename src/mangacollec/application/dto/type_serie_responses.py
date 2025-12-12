"""TypeSerie response DTOs."""

from dataclasses import dataclass

from mangacollec.domain.entities.type_serie import TypeSerie


@dataclass(frozen=True)
class GetAllTypesSerieV1Response:
    """Réponse de l'API pour la récupération de tous les types de séries (V1).

    Attributes:
        types: Liste de tous les types de séries disponibles
    """

    types: list[TypeSerie]
