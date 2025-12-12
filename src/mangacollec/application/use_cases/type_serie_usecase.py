"""TypeSerie use cases."""

from mangacollec.application.dto.type_serie_responses import GetAllTypesSerieV1Response
from mangacollec.domain.repositories.type_serie_repository_interface import (
    ITypeSerieRepository,
)


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

    def __call__(self) -> GetAllTypesSerieV1Response:
        """Exécute le use case.

        Returns:
            GetAllTypesSerieV1Response contenant tous les types de séries

        Raises:
            TypeSerieRetrievalException: Si la récupération échoue
        """
        return self.repo.get_all_types_v1()
