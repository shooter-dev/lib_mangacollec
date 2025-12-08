"""Entité ClientMangaCollec.

Cette entité représente un client pour l'API MangaCollection.
----------
This entity represents a client for the MangaCollection API.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ClientMangaCollec:
    client_id: str
    client_secret: str
    username: str | None = None
    password: str | None = None
