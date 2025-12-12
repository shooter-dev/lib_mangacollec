"""Entité User.

Cette entité représente un utilisateur avec ses informations de base.
----------
This entity represents a user with basic information.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """Entité User du domaine."""

    id: str
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    avatar_url: str | None = None


@dataclass(frozen=True)
class UserCollection:
    """Entité UserCollection du domaine représentant la collection d'un utilisateur."""

    id: str
    user_id: str
    total_editions: int = 0
    total_volumes: int = 0
    total_series: int = 0
    last_updated: str | None = None
