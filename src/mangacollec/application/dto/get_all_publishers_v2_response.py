from dataclasses import dataclass
from typing import List

from mangacollec.domain.entities import Publisher


@dataclass(frozen=True)
class GetAllPublishersV2Response:
    publishers: List[Publisher]
