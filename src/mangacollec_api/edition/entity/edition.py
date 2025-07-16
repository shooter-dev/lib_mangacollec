from typing import Dict

from mangacollec_api.core.interfaces.entity import Entity


class Edition(Entity):

    def __init__(
        self,
        id: str,
        title: str,
        series_id: str,
        publisher_id: str,
        parent_edition_id: str | None,
        volumes_count: int,
        last_volume_number: int | None,
        commercial_stop: bool,
        not_finished: bool,
        follow_editions_count: int,
    ):
        self.id: str = id
        self.title: str = title
        self.series_id: str = series_id
        self.publisher_id: str = publisher_id
        self.parent_edition_id: str | None = parent_edition_id
        self.volumes_count: int = volumes_count
        self.last_volume_number: int | None = last_volume_number
        self.commercial_stop: bool = commercial_stop
        self.not_finished: bool = not_finished
        self.follow_editions_count: int = follow_editions_count

    def to_dict(self) -> Dict[str, any]:
        return {}

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id
