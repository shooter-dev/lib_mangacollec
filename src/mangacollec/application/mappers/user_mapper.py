"""Mapper pour la conversion entre les réponses API et les entités User.

This module provides mapping functions between API responses and User entities.
"""

from mangacollec.application.dto import (
    GetMeCollectionV2Response,
    GetMeRecommendationsV1Response,
    GetUserCollectionByUsernameV2Response,
)
from mangacollec.application.mappers.edition_mapper import EditionMapper
from mangacollec.application.mappers.serie_mapper import SerieMapper
from mangacollec.application.mappers.volume_mapper import VolumeMapper
from mangacollec.domain.entities import User, UserCollection


class UserMapper:
    """Mapper pour convertir entre API et entités du domaine."""

    @staticmethod
    def from_dict(data: dict) -> User:
        """Convertit la réponse API en entité User.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité User
        """
        return User(
            id=data["id"],
            username=data["username"],
            email=data.get("email"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            avatar_url=data.get("avatar_url"),
        )

    @staticmethod
    def to_dict(user: User) -> dict:
        """Convertit l'entité User en dictionnaire.

        Args:
            user: Entité User

        Returns:
            Dictionnaire représentant l'utilisateur
        """
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "avatar_url": user.avatar_url,
        }

    @staticmethod
    def from_user_collection_data(username: str, editions: list, series: list) -> UserCollection:
        """Crée une UserCollection à partir des données de collection.

        Args:
            username: Nom d'utilisateur
            editions: Liste des éditions
            series: Liste des séries

        Returns:
            UserCollection avec les statistiques calculées
        """
        # Générer un ID basé sur le username
        collection_id = f"collection-{username}"

        # Calculer les statistiques
        total_editions = len(editions)
        total_series = len(set(edition.series_id for edition in editions))
        total_volumes = sum(edition.volumes_count for edition in editions if hasattr(edition, "volumes_count"))

        return UserCollection(
            id=collection_id,
            user_id=f"user-{username}",
            total_editions=total_editions,
            total_volumes=total_volumes,
            total_series=total_series,
        )

    @staticmethod
    def from_user_collection_response(response: dict) -> GetUserCollectionByUsernameV2Response:
        """Convertit la réponse de l'API pour get_user_collection_by_username.

        Args:
            response: Réponse API contenant editions et series

        Returns:
            GetUserCollectionByUsernameV2Response contenant les entités converties
        """
        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        return GetUserCollectionByUsernameV2Response(
            editions=editions,
            series=series,
        )

    @staticmethod
    def from_me_collection_response(response: dict, username: str = "me") -> GetMeCollectionV2Response:
        """Convertit la réponse de l'API pour get_me_collection.

        Args:
            response: Réponse API contenant editions et series
            username: Username de l'utilisateur authentifié (défaut: "me")

        Returns:
            GetMeCollectionV2Response contenant les entités converties
        """
        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        # Créer la user_collection à partir des données
        user_collection = UserMapper.from_user_collection_data(username, editions, series)

        return GetMeCollectionV2Response(
            user_collection=user_collection,
            editions=editions,
            series=series,
        )

    @staticmethod
    def from_dict_collection(data: dict) -> UserCollection:
        """Convertit la réponse API en entité UserCollection.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité UserCollection
        """
        return UserCollection(
            id=data["id"],
            user_id=data["user_id"],
            total_editions=data.get("total_editions", 0),
            total_volumes=data.get("total_volumes", 0),
            total_series=data.get("total_series", 0),
            last_updated=data.get("last_updated"),
        )

    @staticmethod
    def to_dict_collection(user_collection: UserCollection) -> dict:
        """Convertit l'entité UserCollection en dictionnaire.

        Args:
            user_collection: Entité UserCollection

        Returns:
            Dictionnaire représentant la collection utilisateur
        """
        return {
            "id": user_collection.id,
            "user_id": user_collection.user_id,
            "total_editions": user_collection.total_editions,
            "total_volumes": user_collection.total_volumes,
            "total_series": user_collection.total_series,
            "last_updated": user_collection.last_updated,
        }

    @staticmethod
    def from_user_collection_username_v2_response(response: dict) -> GetUserCollectionByUsernameV2Response:
        """Convertit la réponse de l'API V2 pour get_user_collection_by_username.

        Args:
            response: Réponse API contenant editions et series

        Returns:
            GetUserCollectionByUsernameV2Response contenant les entités converties
        """
        return UserMapper.from_user_collection_response(response)

    @staticmethod
    def from_me_collection_v2_response(response: dict, username: str = "me") -> GetMeCollectionV2Response:
        """Convertit la réponse de l'API V2 pour get_me_collection.

        Args:
            response: Réponse API contenant user_collection, editions et series
            username: Username de l'utilisateur authentifié (défaut: "me")

        Returns:
            GetMeCollectionV2Response contenant les entités converties
        """
        # Extraire le user_collection directement de la réponse
        user_collection_data = response.get("user_collection", {})
        user_collection = UserMapper.from_dict_collection(user_collection_data)

        # Convertir les editions
        editions = [EditionMapper.from_dict(edition_data) for edition_data in response.get("editions", [])]

        # Convertir les series
        series = [SerieMapper.from_dict(serie_data) for serie_data in response.get("series", [])]

        return GetMeCollectionV2Response(
            user_collection=user_collection,
            editions=editions,
            series=series,
        )

    @staticmethod
    def from_me_recommendations_v1_response(response: dict) -> GetMeRecommendationsV1Response:
        """Convertit la réponse de l'API V1 pour get_me_recommendations.

        Args:
            response: Réponse API contenant les volumes recommandés

        Returns:
            GetMeRecommendationsV1Response contenant les volumes convertis
        """
        return UserMapper.from_recommendations_response(response)

    @staticmethod
    def from_recommendations_response(response: dict) -> GetMeRecommendationsV1Response:
        """Convertit la réponse de l'API pour get_me_recommendations.

        Args:
            response: Réponse API contenant les volumes recommandés

        Returns:
            GetMeRecommendationsV1Response contenant les volumes convertis
        """
        # La réponse est une liste directe de volumes
        volumes = [VolumeMapper.from_dict(volume_data) for volume_data in response]

        return GetMeRecommendationsV1Response(volumes=volumes)
