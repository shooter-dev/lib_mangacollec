"""Implémentation du repository Volume via l'API MangaCollec.

This module provides the API implementation of the Volume repository.
"""

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import VolumeMapper
from mangacollec.domain.exceptions import VolumeNotFoundException
from mangacollec.domain.repositories import IVolumeRepository


class APIVolumeRepository(IVolumeRepository):
    """Implémentation du repository Volume via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_by_id_v2(self, volume_id: str) -> GetVolumeByIdV2Response:
        """Récupère un volume par son ID avec toutes ses relations via l'API.

        Args:
            volume_id: UUID du volume

        Returns:
            GetVolumeByIdV2Response contenant le volume et toutes ses relations

        Raises:
            VolumeNotFoundException: Si le volume n'existe pas
        """
        try:
            response = self.client_api.get(f"/v2/volumes/{volume_id}")

            if not response.get("volumes") or len(response["volumes"]) == 0:
                raise VolumeNotFoundException(volume_id)

            return VolumeMapper.from_api_response(response)

        except Exception as e:
            if isinstance(e, VolumeNotFoundException):
                raise
            raise VolumeNotFoundException(volume_id) from e

    def get_volumes_news_v2(self) -> GetVolumesNewsV2Response:
        """Récupère les volumes récents avec publicité native via l'API.

        Returns:
            GetVolumesNewsV2Response contenant les volumes récents et la publicité native

        Raises:
            RuntimeError: Si une erreur survient lors de la récupération
        """
        try:
            response = self.client_api.get("/v2/volumes/news")
            return VolumeMapper.from_volumes_news_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve volumes news: {e}") from e
