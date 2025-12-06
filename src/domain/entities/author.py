"""Entité Author.

Cette entité représente un auteur de manga avec ses informations de base.
----------
This entity represents a manga author with basic information.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Author:
    id: str
    name: str
    first_name: str | None
    tasks_count: int


@dataclass(frozen=True)
class AuthorListItem:
    id: str
    full_name: str
