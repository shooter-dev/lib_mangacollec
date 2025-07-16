from typing import List, Dict

from mangacollec_api.core.interfaces.entity import Entity


class Serie(Entity):

    def __init__(
        self,
        id: str,
        title: str,
        type_id: str,
        adult_content: bool,
        editions_count: int,
        tasks_count: int,
        kinds_ids: List[str] | None = None,
    ):
        self.id: str = id
        self.title: str = title
        self.type_id: str = type_id
        self.adult_content: bool = adult_content
        self.editions_count: int = editions_count
        self.tasks_count: int = tasks_count
        self.kinds_ids: List[str] | None = kinds_ids

    def to_dict(self) -> Dict[str, any]:
        return {
            "id": self.id,
            "title": self.title,
            "type_id": self.type_id,
            "adult_content": self.adult_content,
            "editions_count": self.editions_count,
            "tasks_count": self.tasks_count,
            "kinds_ids": [],
        }

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id
