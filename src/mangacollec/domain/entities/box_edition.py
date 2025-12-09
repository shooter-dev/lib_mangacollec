"""BoxEdition entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BoxEdition:
    """BoxEdition entity."""

    id: str
    title: str | None
    publisher_id: str
    boxes_count: int
    adult_content: bool
    box_follow_editions_count: int
