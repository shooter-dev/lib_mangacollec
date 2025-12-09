from dataclasses import dataclass
from typing import List

from mangacollec.domain.entities.publisher import Publisher


@dataclass(frozen=True)
class GetAllPublishersV2Response:
    publishers: List[Publisher]
