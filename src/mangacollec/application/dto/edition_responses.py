"""Response DTOs pour Edition.

This module contains response DTOs for Edition operations.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import (Edition, Publisher, Serie, TypeSerie,
                                         Volume)


@dataclass(frozen=True)
class GetEditionByIdV2Response:
    """Réponse pour GetEditionByIdV2.

    Structure normalisée V2 avec des tableaux séparés pour chaque type d'entité.
    """

    editions: list[Edition]
    publishers: list[Publisher]
    series: list[Serie]
    types: list[TypeSerie]
    volumes: list[Volume]
