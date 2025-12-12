"""Implémentation en mémoire du repository Volume pour les tests.

This module provides an in-memory implementation of the Volume repository for testing.
"""

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.domain.exceptions import VolumeNotFoundException
from mangacollec.domain.repositories import IVolumeRepository


class InMemoryVolumeRepository(IVolumeRepository):
    """Implémentation en mémoire du repository Volume (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec un dictionnaire vide."""
        self._data: dict[str, GetVolumeByIdV2Response] = {}
        self._news_data: GetVolumesNewsV2Response | None = None

    def get_by_id_v2(self, volume_id: str) -> GetVolumeByIdV2Response:
        """Récupère un volume par son ID avec toutes ses relations.

        Args:
            volume_id: UUID du volume

        Returns:
            GetVolumeByIdV2Response contenant le volume et ses relations

        Raises:
            VolumeNotFoundException: Si le volume n'existe pas
        """
        response = self._data.get(volume_id)
        if response is None:
            raise VolumeNotFoundException(volume_id)
        return response

    def get_volumes_news_v2(self) -> GetVolumesNewsV2Response:
        """Récupère les volumes récents avec publicité native.

        Returns:
            GetVolumesNewsV2Response contenant les volumes récents et la publicité native

        Note:
            Retourne une réponse vide par défaut si aucune donnée n'a été ajoutée.
        """
        if self._news_data is None:
            return GetVolumesNewsV2Response(
                volumes=[],
                editions=[],
                series=[],
                types=[],
                box_volumes=[],
                boxes=[],
                box_editions=[],
                native_ad_volume_home_first=None,
            )
        return self._news_data

    def add_volume(self, volume_id: str, response: GetVolumeByIdV2Response) -> None:
        """Ajoute un volume au repository (méthode pour les tests).

        Args:
            volume_id: UUID du volume
            response: Réponse complète contenant le volume et ses relations
        """
        self._data[volume_id] = response

    def set_news(self, news_response: GetVolumesNewsV2Response) -> None:
        """Définit les volumes récents (méthode pour les tests).

        Args:
            news_response: Réponse contenant les volumes récents
        """
        self._news_data = news_response

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._data.clear()
        self._news_data = None
