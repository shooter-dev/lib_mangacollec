from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    id: str
    title: str
