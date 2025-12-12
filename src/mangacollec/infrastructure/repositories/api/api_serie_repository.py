"""Implémentation du repository Serie via l'API MangaCollec.

This module provides the API implementation of the Serie repository.
"""

from mangacollec.application.dto import GetAllSeriesV2Response, GetSerieByIdV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import SerieMapper
from mangacollec.domain.exceptions import SerieNotFoundException
from mangacollec.domain.repositories import ISerieRepository


class APISerieRepository(ISerieRepository):
    """Implémentation du repository Serie via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_serie_by_id_v2(self, serie_id: str) -> GetSerieByIdV2Response:
        """Récupère une série par son ID avec toutes ses relations via l'API.

        Args:
            serie_id: UUID de la série

        Returns:
            GetSerieByIdV2Response contenant la série et toutes ses relations

        Raises:
            SerieNotFoundException: Si la série n'existe pas
        """
        try:
            response = self.client_api.get(f"/v2/series/{serie_id}")

            if not response.get("series") or len(response["series"]) == 0:
                raise SerieNotFoundException(serie_id)

            # Utiliser le mapper pour convertir toute la réponse API
            return SerieMapper.from_api_response(response)

        except Exception as e:
            if isinstance(e, SerieNotFoundException):
                raise
            raise SerieNotFoundException(serie_id) from e

    def get_all_series_v2(self) -> GetAllSeriesV2Response:
        """Récupère toutes les séries avec leurs types via l'API.

        Returns:
            GetAllSeriesV2Response contenant la liste des séries et types
        """
        try:
            response = self.client_api.get("/v2/series/")
            return SerieMapper.from_all_series_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve series: {e}") from e
