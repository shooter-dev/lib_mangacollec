"""DTOs de réponse pour les Volumes.

This module contains response DTOs for Volume operations.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         NativeAdVolumeHomeFirst, Publisher,
                                         Serie, TypeSerie, Volume)


@dataclass(frozen=True)
class GetVolumeByIdV2Response:
    """Réponse de l'API pour GET /v2/volumes/{id} avec structure normalisée V2.

    Cette réponse contient le volume demandé et toutes ses relations :
    éditions, éditeurs, séries, types, coffrets, volumes de coffrets et éditions de coffrets.
    """

    volumes: list[Volume]
    editions: list[Edition]
    publishers: list[Publisher]
    series: list[Serie]
    types: list[TypeSerie]
    box_volumes: list[BoxVolume]
    boxes: list[Box]
    box_editions: list[BoxEdition]


@dataclass(frozen=True)
class GetVolumesNewsV2Response:
    """Réponse de l'API pour GET /v2/volumes/news avec publicité native optionnelle.

    Cette réponse contient les volumes récents avec leurs relations,
    mais sans les éditeurs. Peut inclure une publicité native optionnelle.
    """

    volumes: list[Volume]
    editions: list[Edition]
    series: list[Serie]
    types: list[TypeSerie]
    box_volumes: list[BoxVolume]
    boxes: list[Box]
    box_editions: list[BoxEdition]
    native_ad_volume_home_first: NativeAdVolumeHomeFirst | None
