"""Implémentation du repository Edition via l'API MangaCollec.

This module provides the API implementation of the Edition repository.
"""

from src.application.dto.responses import GetEditionByIdV2Response
from src.application.interfaces.mangacollec_api_interface import IMangaCollecAPI
from src.application.mappers.edition_mapper import EditionMapper
from src.domain.execptions.edition_exceptions import EditionNotFoundException
from src.domain.repositories.edition_repository import IEditionRepository


class APIEditionRepository(IEditionRepository):
    """Implémentation du repository Edition via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_edition_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
        """Récupère une édition par son ID avec toutes les entités associées via l'API V2.

        Args:
            edition_id: UUID de l'édition

        Returns:
            GetEditionByIdV2Response contenant:
                - editions: Liste des éditions (peut contenir des éditions parentes/enfants)
                - publishers: Liste des publishers
                - series: Liste des séries
                - types: Liste des types de séries
                - volumes: Liste des volumes

        Raises:
            EditionNotFoundException: Si l'édition n'existe pas
        """
        try:
            response = self.client_api.get(f"/v2/editions/{edition_id}")

            if not response.get("editions") or len(response["editions"]) == 0:
                raise EditionNotFoundException(edition_id)

            # Utiliser le mapper pour convertir toute la réponse API
            return EditionMapper.from_api_response(response)

        except Exception as e:
            if isinstance(e, EditionNotFoundException):
                raise
            raise EditionNotFoundException(edition_id) from e
