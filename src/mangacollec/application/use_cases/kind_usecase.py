"""Use cases pour les Kinds."""

from mangacollec.domain.entities import Kind
from mangacollec.domain.repositories import IKindRepository


class GetAllKindsV1UseCase:
    """Cas d'utilisation : récupérer tous les kinds via l'API V1."""

    def __init__(self, repo: IKindRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository des kinds
        """
        self.repo = repo

    def __call__(self) -> list[Kind]:
        """Récupère tous les kinds via l'API V1.

        Returns:
            Liste des kinds
        """
        response = self.repo.get_all_kinds_v1()
        return response.kinds


class GetAllKindsV2UseCase:
    """Cas d'utilisation : récupérer tous les kinds via l'API V2."""

    def __init__(self, repo: IKindRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository des kinds
        """
        self.repo = repo

    def __call__(self) -> list[Kind]:
        """Récupère tous les kinds via l'API V2.

        Returns:
            Liste des kinds
        """
        response = self.repo.get_all_kinds_v2()
        return response.kinds
