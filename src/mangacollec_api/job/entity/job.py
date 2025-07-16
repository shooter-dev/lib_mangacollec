from dataclasses import dataclass
from typing import List


@dataclass
class Job:
    id: str
    title: str

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id
