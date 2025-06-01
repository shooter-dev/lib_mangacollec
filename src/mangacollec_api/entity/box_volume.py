import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class BoxVolume:
    id: str
    box_id: str
    volume_id: str
    included: bool

    def __srt__(self):
        return self.id

    def __repr__(self):
        return self.id