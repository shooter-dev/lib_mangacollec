"""Use cases pour les Kinds."""

from mangacollec.application.dto import (GetAllKindsV1Response,
                                         GetAllKindsV2Response)
from mangacollec.domain.repositories import IKindRepository


class GetAllKindsV1UseCase:
    """Cas d'utilisation : récupérer tous les kinds via l'API V1."""

    def __init__(self, repo: IKindRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository des kinds
        """
        self.repo = repo

    def __call__(self) -> GetAllKindsV1Response:
        """Récupère tous les kinds via l'API V1.

        Returns:
            GetAllKindsV1Response contenant la liste des kinds
        """
        return self.repo.get_all_kinds_v1()


class GetAllKindsV2UseCase:
    """Cas d'utilisation : récupérer tous les kinds via l'API V2."""

    def __init__(self, repo: IKindRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository des kinds
        """
        self.repo = repo

    def __call__(self) -> GetAllKindsV2Response:
        """Récupère tous les kinds via l'API V2.

        Returns:
            GetAllKindsV2Response contenant la liste des kinds
        """
        return self.repo.get_all_kinds_v2()
