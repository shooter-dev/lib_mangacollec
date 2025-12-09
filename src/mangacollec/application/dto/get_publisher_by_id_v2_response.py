from dataclasses import dataclass
from typing import List

from mangacollec.domain.entities import TypeSerie, Box, BoxEdition, Edition, Publisher, Serie, Volume


@dataclass(frozen=True)
class GetPublisherByIdV2Response:
    publishers: List[Publisher]
    editions: List[Edition]
    box_editions: List[BoxEdition]
    series: List[Serie]
    types: List[TypeSerie]
    volumes: List[Volume]
    boxes: List[Box]
