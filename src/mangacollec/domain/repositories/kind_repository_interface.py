"""Interface du repository pour les Kinds."""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetAllKindsV1Response, GetAllKindsV2Response


class IKindRepository(ABC):
    """Interface du repository pour les Kinds.

    Méthodes disponibles:
    - get_all_kinds_v1() -> GetAllKindsV1Response : GET /v1/kinds
    - get_all_kinds_v2() -> GetAllKindsV2Response : GET /v2/kinds
    """

    @abstractmethod
    def get_all_kinds_v1(self) -> GetAllKindsV1Response:
        """Récupère tous les kinds via l'API V1.

        Returns:
            GetAllKindsV1Response contenant la liste des kinds

        Raises:
            RuntimeError: En cas d'erreur lors de la récupération des kinds
        """
        pass

    @abstractmethod
    def get_all_kinds_v2(self) -> GetAllKindsV2Response:
        """Récupère tous les kinds via l'API V2.

        Returns:
            GetAllKindsV2Response contenant la liste des kinds

        Raises:
            RuntimeError: En cas d'erreur lors de la récupération des kinds
        """
        pass
