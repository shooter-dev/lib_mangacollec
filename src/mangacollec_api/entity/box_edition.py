import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class BoxEdition:
    id: str
    title: str
    publisher_id: str
    boxes_count: int
    adult_content: bool
    box_follow_editions_count: int

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id