"""Follow Edition Deleted entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FollowEditionDeleted:
    """Entité FollowEditionDeleted pour les suivis d'éditions supprimés."""

    id: str
    deleted: bool
