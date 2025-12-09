"""Interface du repository pour les éditions.

This module defines the repository interface for edition operations.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import GetEditionByIdV2Response


class IEditionRepository(ABC):
    """Interface du repository pour Edition."""

    @abstractmethod
    def get_edition_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
        """Récupère une édition par son ID avec toutes les entités associées (API V2).

        Args:
            edition_id: UUID de l'édition

        Returns:
            GetEditionByIdV2Response contenant:
                - editions: Liste des éditions (peut contenir des éditions parentes/enfants)
                - publishers: Liste des publishers (normalement 1 seul)
                - series: Liste des séries
                - types: Liste des types de séries
                - volumes: Liste des volumes

        Raises:
            EditionNotFoundException: Si l'édition n'existe pas
        """
        pass
