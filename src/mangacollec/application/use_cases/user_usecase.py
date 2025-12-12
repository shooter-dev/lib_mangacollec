"""Use cases pour la ressource User.

This module contains all use cases for User operations.
"""

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.domain.repositories import IUserRepository


class GetUserCollectionByUsernameV2UseCase:
    """Cas d'utilisation : récupérer la collection d'un utilisateur par son username."""

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def __call__(self, username: str) -> GetUserCollectionByUsernameV2Response:
        """Exécute le use case.

        Args:
            username: Nom d'utilisateur

        Returns:
            GetUserCollectionByUsernameV2Response contenant:
                - editions: Liste des éditions de l'utilisateur
                - series: Liste des séries de l'utilisateur

        Raises:
            UserNotFoundException: Si l'utilisateur n'existe pas
        """
        return self.repository.get_user_collection_by_username_v2(username)


class GetMeCollectionV2UseCase:
    """Cas d'utilisation : récupérer la collection de l'utilisateur authentifié."""

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def __call__(self) -> GetMeCollectionV2Response:
        """Exécute le use case.

        Returns:
            GetMeCollectionV2Response contenant:
                - user_collection: Informations sur la collection utilisateur
                - editions: Liste des éditions
                - series: Liste des séries
        """
        return self.repository.get_me_collection_v2()


class GetMeRecommendationsV1UseCase:
    """Cas d'utilisation : récupérer les recommandations pour l'utilisateur authentifié."""

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def __call__(self) -> GetMeRecommendationsV1Response:
        """Exécute le use case.

        Returns:
            GetMeRecommendationsV1Response contenant les volumes recommandés
        """
        return self.repository.get_me_recommendations_v1()
