"""Implémentation InMemory du repository User.

This module provides the in-memory implementation of the User repository for testing.
"""

from mangacollec.application.dto import (GetMeCollectionV2Response,
                                         GetMeRecommendationsV1Response,
                                         GetUserCollectionByUsernameV2Response)
from mangacollec.application.mappers import UserMapper
from mangacollec.domain.entities import User
from mangacollec.domain.repositories import IUserRepository


class InMemoryUserRepository(IUserRepository):
    """Implémentation en mémoire du repository User (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository en mémoire avec des données de test."""
        # Données de test pour get_user_collection_by_username
        self._user_collections: dict[str, dict] = {
            "shooterdev": {
                "editions": [
                    {
                        "id": "edition-123",
                        "title": "Edition Collector",
                        "series_id": "series-456",
                        "publisher_id": "publisher-789",
                        "parent_edition_id": None,
                        "volumes_count": 72,
                        "last_volume_number": 72,
                        "commercial_stop": False,
                        "not_finished": False,
                        "follow_editions_count": 1443,
                    },
                    {
                        "id": "edition-124",
                        "title": None,
                        "series_id": "series-457",
                        "publisher_id": "publisher-790",
                        "parent_edition_id": None,
                        "volumes_count": 50,
                        "last_volume_number": None,
                        "commercial_stop": False,
                        "not_finished": True,
                        "follow_editions_count": 500,
                    },
                ],
                "series": [
                    {
                        "id": "series-456",
                        "title": "Naruto",
                        "type_id": "type-001",
                        "adult_content": False,
                        "editions_count": 2,
                        "tasks_count": 2,
                    },
                    {
                        "id": "series-457",
                        "title": "One Piece",
                        "type_id": "type-001",
                        "adult_content": False,
                        "editions_count": 1,
                        "tasks_count": 1,
                    },
                ],
            }
        }

        # Données de test pour get_me_collection
        self._me_collection = {
            "editions": [
                {
                    "id": "edition-789",
                    "title": "Personal Edition",
                    "series_id": "series-101",
                    "publisher_id": "publisher-202",
                    "parent_edition_id": None,
                    "volumes_count": 25,
                    "last_volume_number": 25,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 300,
                }
            ],
            "series": [
                {
                    "id": "series-101",
                    "title": "My Favorite Series",
                    "type_id": "type-002",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 1,
                }
            ],
        }

        # Données de test pour get_me_recommendations
        self._me_recommendations = [
            {
                "id": "volume-111",
                "title": "Recommended Volume 1",
                "number": 1,
                "release_date": "2025-12-01",
                "isbn": "9791032724743",
                "asin": "B0FC1DWL9R",
                "edition_id": "edition-111",
                "possessions_count": 59,
                "not_sold": False,
                "image_url": "https://example.com/image1.jpg",
                "nb_pages": None,
                "content": None,
            },
            {
                "id": "volume-112",
                "title": None,
                "number": 2,
                "release_date": "2025-12-08",
                "isbn": "9791032724744",
                "asin": "B0FC1DWL9S",
                "edition_id": "edition-112",
                "possessions_count": 45,
                "not_sold": False,
                "image_url": "https://example.com/image2.jpg",
                "nb_pages": 200,
                "content": None,
            },
        ]

    def get_user_collection_by_username_v2(self, username: str) -> GetUserCollectionByUsernameV2Response:
        """Récupère la collection d'un utilisateur par son username en mémoire.

        Args:
            username: Nom d'utilisateur

        Returns:
            GetUserCollectionByUsernameV2Response contenant:
                - editions: Liste des éditions de l'utilisateur
                - series: Liste des séries de l'utilisateur

        Raises:
            UserNotFoundException: Si l'utilisateur n'existe pas
        """
        if username not in self._user_collections:
            from mangacollec.domain.exceptions import UserNotFoundException

            raise UserNotFoundException(username)

        collection_data = self._user_collections[username]
        return UserMapper.from_user_collection_response(collection_data)

    def get_me_collection_v2(self) -> GetMeCollectionV2Response:
        """Récupère la collection de l'utilisateur authentifié en mémoire.

        Returns:
            GetMeCollectionV2Response contenant:
                - user_collection: Informations sur la collection utilisateur
                - editions: Liste des éditions
                - series: Liste des séries

        Raises:
            UserNotFoundException: Si la collection n'existe pas
        """
        if self._me_collection is None:
            from mangacollec.domain.exceptions import UserNotFoundException

            raise UserNotFoundException("me")

        return UserMapper.from_me_collection_response(self._me_collection, "me")

    def get_me_recommendations_v1(self) -> GetMeRecommendationsV1Response:
        """Récupère les recommandations pour l'utilisateur authentifié en mémoire.

        Returns:
            GetMeRecommendationsV1Response contenant les volumes recommandés

        Raises:
            UserNotFoundException: Si les recommandations n'existent pas
        """
        if self._me_recommendations is None:
            from mangacollec.domain.exceptions import UserNotFoundException

            raise UserNotFoundException("me")

        return UserMapper.from_recommendations_response(self._me_recommendations)

    def add_user_collection(self, username: str, collection_data: dict) -> None:
        """Ajoute une collection utilisateur pour les tests.

        Args:
            username: Nom d'utilisateur
            collection_data: Données de la collection (editions et series)
        """
        self._user_collections[username] = collection_data

    def clear_data(self) -> None:
        """Nettoie toutes les données en mémoire (pour les tests)."""
        self._user_collections.clear()

    def set_me_recommendations(self, recommendations: list) -> None:
        """Définit les recommandations pour l'utilisateur authentifié (pour les tests).

        Args:
            recommendations: Liste de volumes ou de dictionnaires de volumes
        """
        if recommendations and isinstance(recommendations[0], dict):
            self._me_recommendations = recommendations
        else:
            # Convertir les objets Volume en dictionnaires
            self._me_recommendations = [
                {
                    "id": vol.id,
                    "title": vol.title,
                    "number": vol.number,
                    "release_date": vol.release_date,
                    "isbn": vol.isbn,
                    "asin": vol.asin,
                    "edition_id": vol.edition_id,
                    "possessions_count": vol.possessions_count,
                    "not_sold": vol.not_sold,
                    "image_url": vol.image_url,
                    "nb_pages": vol.nb_pages,
                    "content": vol.content,
                }
                for vol in recommendations
            ]

    def save(self, user: User) -> None:
        """Sauvegarde un utilisateur (alias pour save_user).

        Args:
            user: Entité User à sauvegarder
        """
        self.save_user(user)

    def save_user(self, user: User) -> None:
        """Sauvegarde un utilisateur (pour les tests).

        Args:
            user: Entité User à sauvegarder
        """
        # Méthode pour les tests - ne fait rien pour l'instant
        pass
