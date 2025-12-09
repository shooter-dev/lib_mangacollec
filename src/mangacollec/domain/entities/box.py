"""Box entity."""

from dataclasses import dataclass
from typing import Optional

from mangacollec.domain.value_objects import ASIN, ISBN, URL


@dataclass(frozen=True)
class Box:
    """Box entity."""

    id: str
    title: Optional[str]
    number: int
    release_date: Optional[str]
    isbn: Optional[ISBN]
    asin: Optional[ASIN]
    commercial_stop: bool
    box_edition_id: str
    box_possessions_count: Optional[int]
    image_url: Optional[URL]
