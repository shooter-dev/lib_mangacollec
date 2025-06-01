from dataclasses import dataclass
from typing import List


@dataclass
class Genre:
    id: str
    title: str
    to_display: bool



    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id