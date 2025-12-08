from dataclasses import dataclass
from typing import List

from src.domain.entities.box import Box
from src.domain.entities.box_edition import BoxEdition
from src.domain.entities.edition import Edition
from src.domain.entities.publisher import Publisher
from src.domain.entities.serie import Serie
from src.domain.entities.type_serie import TypeSerie
from src.domain.entities.volume import Volume


@dataclass(frozen=True)
class GetPublisherByIdV2Response:
    publishers: List[Publisher]
    editions: List[Edition]
    box_editions: List[BoxEdition]
    series: List[Serie]
    types: List[TypeSerie]
    volumes: List[Volume]
    boxes: List[Box]
