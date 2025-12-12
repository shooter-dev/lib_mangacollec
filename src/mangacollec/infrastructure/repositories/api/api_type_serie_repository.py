"""API TypeSerie repository implementation."""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import TypeSerieMapper
from mangacollec.domain.exceptions import TypeSerieRetrievalException
from mangacollec.domain.repositories import ITypeSerieRepository


class APITypeSerieRepository(ITypeSerieRepository):
    """Implémentation du repository TypeSerie via MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_all_types_v1(self) -> GetAllTypesSerieV1Response:
        """Récupère tous les types de séries via l'API V1.

        Returns:
            GetAllTypesSerieV1Response contenant la liste des types

        Raises:
            TypeSerieRetrievalException: Si la récupération échoue
        """
        try:
            response = self.client_api.get("/v1/types")

            # Déléguer au mapper
            return TypeSerieMapper.from_all_types_v1_response(response)

        except Exception as e:
            raise TypeSerieRetrievalException(str(e)) from e
