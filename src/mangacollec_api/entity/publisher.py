from dataclasses import dataclass
from typing import List


@dataclass
class Publisher:
    id: str
    title: str
    closed: bool
    editions_count: int
    no_amazon: bool

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id