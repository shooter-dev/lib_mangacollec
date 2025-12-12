"""Interface du repository pour TypeSerie."""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetAllTypesSerieV1Response


class ITypeSerieRepository(ABC):
    """Interface du repository pour TypeSerie."""

    @abstractmethod
    def get_all_types_v1(self) -> GetAllTypesSerieV1Response:
        """Récupère tous les types de séries via l'API V1.

        Returns:
            GetAllTypesSerieV1Response contenant la liste des types
        """
        pass
