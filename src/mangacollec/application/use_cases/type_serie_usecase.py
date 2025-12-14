"""TypeSerie use cases."""

from mangacollec.domain.entities import TypeSerie
from mangacollec.domain.repositories import ITypeSerieRepository


class GetAllTypesSerieV1UseCase:
    """Cas d'utilisation : récupérer tous les types de séries (V1).

    Ce use case permet de récupérer la liste complète des types de séries
    disponibles dans le système (Manga, Manhwa, BD, Comics, etc.).
    """

    def __init__(self, repo: ITypeSerieRepository) -> None:
        """Initialise le use case.

        Args:
            repo: Repository pour accéder aux types de séries
        """
        self.repo = repo

    def __call__(self) -> list[TypeSerie]:
        """Exécute le use case.

        Returns:
            Liste des types de séries

        Raises:
            TypeSerieRetrievalException: Si la récupération échoue
        """
        response = self.repo.get_all_types_v1()
        return response.types
