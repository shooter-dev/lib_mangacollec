from dataclasses import dataclass
from typing import List

from mangacollec.domain.entities.box import Box
from mangacollec.domain.entities.box_edition import BoxEdition
from mangacollec.domain.entities.edition import Edition
from mangacollec.domain.entities.publisher import Publisher
from mangacollec.domain.entities.serie import Serie
from mangacollec.domain import TypeSerie
from mangacollec.domain.entities.volume import Volume


@dataclass(frozen=True)
class GetPublisherByIdV2Response:
    publishers: List[Publisher]
    editions: List[Edition]
    box_editions: List[BoxEdition]
    series: List[Serie]
    types: List[TypeSerie]
    volumes: List[Volume]
    boxes: List[Box]
