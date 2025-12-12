"""Entité NativeAdVolumeHomeFirst.

Cette entité représente une publicité native affichée sur la page d'accueil des volumes.
----------
This entity represents a native ad displayed on the volumes home page.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NativeAdVolumeHomeFirst:
    """Représente une publicité native pour la page d'accueil des volumes."""

    id: str
    volume_id: str
    title: str
    start_date: str | None
    end_date: str | None
