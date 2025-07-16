from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    id: str
    name: str
    first_name: str | None
    tasks_count: int

    def __str__(self):
        if self.first_name is None:
            return self.name

        return self.name + " " + self.first_name

    def __repr__(self):
        return self.id
