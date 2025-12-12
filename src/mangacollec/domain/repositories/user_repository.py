"""Interface du repository pour la ressource User.

This module defines the repository interface for User operations.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (
    GetMeCollectionV2Response,
    GetMeRecommendationsV1Response,
    GetUserCollectionByUsernameV2Response,
)


class IUserRepository(ABC):
    """Interface du repository pour User.

    Seules les opérations de lecture sont disponibles (pas de create/update/delete).
    """

    @abstractmethod
    def get_user_collection_by_username_v2(self, username: str) -> GetUserCollectionByUsernameV2Response:
        """Récupère la collection d'un utilisateur par son username.

        Args:
            username: Nom d'utilisateur

        Returns:
            GetUserCollectionByUsernameV2Response contenant:
                - editions: Liste des éditions de l'utilisateur
                - series: Liste des séries de l'utilisateur

        Raises:
            UserNotFoundException: Si l'utilisateur n'existe pas
        """

    @abstractmethod
    def get_me_collection_v2(self) -> GetMeCollectionV2Response:
        """Récupère la collection de l'utilisateur authentifié.

        Returns:
            GetMeCollectionV2Response contenant:
                - user_collection: Informations sur la collection utilisateur
                - editions: Liste des éditions
                - series: Liste des séries
        """

    @abstractmethod
    def get_me_recommendations_v1(self) -> GetMeRecommendationsV1Response:
        """Récupère les recommandations pour l'utilisateur authentifié.

        Returns:
            GetMeRecommendationsV1Response contenant:
                - volumes: Liste des volumes recommandés
        """
