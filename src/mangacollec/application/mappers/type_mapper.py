"""Mapper for converting between API responses and TypeSerie entities.

This module provides mapping functions between API responses and TypeSerie entities.
"""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.domain.entities import TypeSerie


class TypeSerieMapper:
    """Mapper for converting between API and domain TypeSerie entities."""

    @staticmethod
    def from_dict(data: dict) -> TypeSerie:
        """Converts the API response to a TypeSerie entity.

        Args:
            data: Dictionary containing the API data.

        Returns:
            A TypeSerie entity.
        """
        return TypeSerie(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"],
        )

    @staticmethod
    def to_dict(type_entity: TypeSerie) -> dict:
        """Converts a TypeSerie entity to a dictionary.

        Args:
            type_entity: A TypeSerie entity.

        Returns:
            A dictionary representing the series type.
        """
        return {
            "id": type_entity.id,
            "title": type_entity.title,
            "to_display": type_entity.to_display,
        }

    @staticmethod
    def from_all_types_v1_response(response: list) -> GetAllTypesSerieV1Response:
        """Converts the API V1 response for get_all to GetAllTypesSerieV1Response.

        Args:
            response: Liste directe de dictionnaires de types depuis l'API

        Returns:
            GetAllTypesSerieV1Response contenant tous les types convertis
        """
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response]
        return GetAllTypesSerieV1Response(types=types)
