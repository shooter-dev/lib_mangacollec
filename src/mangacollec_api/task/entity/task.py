from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    id: str
    job_id: str
    series_id: str
    author_id: str



    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id