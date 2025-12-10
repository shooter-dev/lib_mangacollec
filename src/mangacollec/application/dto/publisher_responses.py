"""Publisher responses."""

from dataclasses import dataclass

from mangacollec.domain.entities import (Box, BoxEdition, Edition, Publisher,
                                         Serie, TypeSerie, Volume)


@dataclass(frozen=True)
class GetAllPublishersV2Response:
    """Get all publishers response."""

    publishers: list[Publisher]


@dataclass(frozen=True)
class GetPublisherByIdV2Response:
    """Get publisher by id response."""

    publishers: list[Publisher]
    editions: list[Edition]
    box_editions: list[BoxEdition]
    series: list[Serie]
    types: list[TypeSerie]
    volumes: list[Volume]
    boxes: list[Box]
