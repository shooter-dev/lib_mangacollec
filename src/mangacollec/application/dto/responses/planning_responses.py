"""Planning response DTOs.

This module contains Data Transfer Objects for Planning API responses.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         Serie, TypeSerie, Volume)


@dataclass(frozen=True)
class GetPlanningV2Response:
    """Response DTO pour GET /v2/planning/.

    Retourne tous les volumes et coffrets planifiés avec leurs entités liées.
    """

    volumes: list[Volume]
    editions: list[Edition]
    series: list[Serie]
    types: list[TypeSerie]
    boxes: list[Box]
    box_editions: list[BoxEdition]
    box_volumes: list[BoxVolume]
