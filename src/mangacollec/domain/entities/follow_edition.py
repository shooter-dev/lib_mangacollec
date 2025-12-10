"""Follow Edition entity."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class FollowEdition:
    """Entité FollowEdition du domaine."""

    id: str
    user_id: str
    edition_id: str
    following: bool
    created_at: datetime
    updated_at: datetime
