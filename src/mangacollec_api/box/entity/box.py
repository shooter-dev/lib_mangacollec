import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Box:
    id: str
    title: str
    number: int
    release_date: datetime
    isbn: str
    asin: str
    commercial_stop: bool
    box_edition_id: str
    box_possessions_count: int
    image_url: str

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id