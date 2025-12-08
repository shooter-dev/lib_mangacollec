"""Publisher entity."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Publisher:
    """Publisher entity."""

    id: str
    title: str
    closed: bool
    editions_count: int
    no_amazon: bool


@dataclass(frozen=True)
class PublisherListItem:
    """Publisher list item entity."""

    id: str
    title: str
