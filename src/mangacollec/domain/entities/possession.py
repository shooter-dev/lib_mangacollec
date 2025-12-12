"""Possession entity."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Possession:
    """Entité Possession du domaine."""

    id: str
    user_id: str
    volume_id: str
    created_at: datetime


@dataclass(frozen=True)
class PossessionDeleted:
    """Entité PossessionDeleted pour les possessions supprimées."""

    id: str
    deleted: bool
