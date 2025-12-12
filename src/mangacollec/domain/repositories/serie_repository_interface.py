"""Interface du repository pour Serie.

Cette interface définit les méthodes de récupération et de manipulation
des données des séries de mangas.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetAllSeriesV2Response, GetSerieByIdV2Response


class ISerieRepository(ABC):
    """Interface du repository pour les séries de manga."""

    @abstractmethod
    def get_all_series_v2(self) -> GetAllSeriesV2Response:
        """Récupère toutes les séries avec leurs types via l'API V2.

        Returns:
            GetAllSeriesV2Response: Réponse contenant les séries et types
        """
        pass

    @abstractmethod
    def get_serie_by_id_v2(self, serie_id: str) -> GetSerieByIdV2Response:
        """Récupère une série par son ID avec toutes ses relations via l'API V2.

        Args:
            serie_id: UUID de la série

        Returns:
            GetSerieByIdV2Response: Réponse contenant la série et toutes ses relations

        Raises:
            SerieNotFoundException: Si la série n'existe pas
        """
        pass
