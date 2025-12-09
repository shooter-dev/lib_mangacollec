"""Publisher responses."""

from dataclasses import dataclass

from mangacollec.domain.entities.box import Box
from mangacollec.domain.entities.box_edition import BoxEdition
from mangacollec.domain.entities.edition import Edition
from mangacollec.domain.entities.publisher import Publisher
from mangacollec.domain.entities.serie import Serie
from mangacollec.domain.entities.type import Type
from mangacollec.domain.entities.volume import Volume


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
