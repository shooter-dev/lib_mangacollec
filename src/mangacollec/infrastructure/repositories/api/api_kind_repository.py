"""Implémentation du repository Kind via MangaCollecAPI."""

from mangacollec.application.dto import GetAllKindsV1Response, GetAllKindsV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import KindMapper
from mangacollec.domain.repositories import IKindRepository


class APIKindRepository(IKindRepository):
    """Implémentation du repository Kind via MangaCollecAPI."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_all_kinds_v1(self) -> GetAllKindsV1Response:
        """Récupère tous les kinds via l'API V1.

        Returns:
            GetAllKindsV1Response contenant la liste des kinds

        Raises:
            RuntimeError: En cas d'erreur lors de la récupération des kinds
        """
        try:
            response = self.client_api.get("/v1/kinds")
            return KindMapper.from_all_kinds_v1_response(response)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve kinds from V1 API: {e}") from e

    def get_all_kinds_v2(self) -> GetAllKindsV2Response:
        """Récupère tous les kinds via l'API V2.

        Returns:
            GetAllKindsV2Response contenant la liste des kinds

        Raises:
            RuntimeError: En cas d'erreur lors de la récupération des kinds
        """
        try:
            response = self.client_api.get("/v2/kinds/")
            return KindMapper.from_all_kinds_v2_response(response)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve kinds from V2 API: {e}") from e
