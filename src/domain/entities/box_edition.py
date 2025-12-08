"""BoxEdition entity."""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BoxEdition:
    """BoxEdition entity."""

    id: str
    title: Optional[str]
    publisher_id: str
    boxes_count: int
    adult_content: bool
    box_follow_editions_count: int