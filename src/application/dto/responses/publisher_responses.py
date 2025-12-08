"""Publisher responses."""

from dataclasses import dataclass

from src.domain.entities.box import Box
from src.domain.entities.box_edition import BoxEdition
from src.domain.entities.edition import Edition
from src.domain.entities.publisher import Publisher
from src.domain.entities.serie import Serie
from src.domain.entities.type import Type
from src.domain.entities.volume import Volume


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
    types: list[Type]
    volumes: list[Volume]
    boxes: list[Box]
