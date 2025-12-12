"""Implémentation du repository User via l'API MangaCollec.

This module provides the API implementation of the User repository.
"""

from mangacollec.application.dto import (
    GetMeCollectionV2Response,
    GetMeRecommendationsV1Response,
    GetUserCollectionByUsernameV2Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import UserMapper
from mangacollec.domain.exceptions import UserNotFoundException
from mangacollec.domain.repositories import IUserRepository


class APIUserRepository(IUserRepository):
    """Implémentation du repository User via MangaCollecAPI."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_user_collection_by_username_v2(self, username: str) -> GetUserCollectionByUsernameV2Response:
        """Récupère la collection d'un utilisateur par son username via l'API.

        Args:
            username: Nom d'utilisateur

        Returns:
            GetUserCollectionByUsernameV2Response contenant:
                - editions: Liste des éditions de l'utilisateur
                - series: Liste des séries de l'utilisateur

        Raises:
            UserNotFoundException: Si l'utilisateur n'existe pas
        """
        try:
            response = self.client_api.get(f"/v2/user/{username}/collection")

            if not response.get("editions") or len(response["editions"]) == 0:
                raise UserNotFoundException(username)

            # Utiliser le mapper pour convertir toute la réponse API
            return UserMapper.from_user_collection_response(response)

        except Exception as e:
            if isinstance(e, UserNotFoundException):
                raise
            raise UserNotFoundException(username) from e

    def get_me_collection_v2(self) -> GetMeCollectionV2Response:
        """Récupère la collection de l'utilisateur authentifié via l'API.

        Returns:
            GetMeCollectionV2Response contenant:
                - user_collection: Informations sur la collection utilisateur
                - editions: Liste des éditions
                - series: Liste des séries
        """
        try:
            response = self.client_api.get("/v2/users/me/collection")

            # Utiliser le mapper pour convertir toute la réponse API
            return UserMapper.from_me_collection_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve user collection: {e}") from e

    def get_me_recommendations_v1(self) -> GetMeRecommendationsV1Response:
        """Récupère les recommandations pour l'utilisateur authentifié via l'API.

        Returns:
            GetMeRecommendationsV1Response contenant les volumes recommandés
        """
        try:
            response = self.client_api.get("/v1/users/me/recommendation")

            # La réponse est une liste directe de volumes
            return UserMapper.from_recommendations_response(response)

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve user recommendations: {e}") from e
