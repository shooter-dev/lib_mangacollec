"""Use cases pour la ressource Edition.

This module contains all use cases for Edition operations.
"""

from src.domain.entities import Edition, Publisher, Serie, Type, Volume
from src.domain.repositories.edition_repository import IEditionRepository


class GetEditionByIdV2UseCase:
    """Cas d'utilisation : récupérer une édition par ID avec toutes les entités associées (V2)."""

    def __init__(self, repository: IEditionRepository) -> None:
        """Initialise le use case.

        Args:
            repository: Repository d'éditions
        """
        self.repository = repository

    def __call__(
        self, edition_id: str
    ) -> tuple[list[Edition], list[Publisher], list[Serie], list[Type], list[Volume]]:
        """Exécute le use case.

        Args:
            edition_id: UUID de l'édition

        Returns:
            Tuple contenant:
                - list[Edition]: Liste des éditions (peut contenir des éditions parentes/enfants)
                - list[Publisher]: Liste des éditeurs
                - list[Serie]: Liste des séries
                - list[TypeSerie]: Liste des types de séries
                - list[Volume]: Liste des volumes

        Raises:
            EditionNotFoundException: Si l'édition n'existe pas
        """
        response = self.repository.get_edition_by_id_v2(edition_id)

        # Convertir le DTO en tuple
        return (
            response.editions,
            response.publishers,
            response.series,
            response.types,
            response.volumes,
        )
