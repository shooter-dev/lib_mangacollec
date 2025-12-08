"""Mapper for converting between API responses and Type entities.

This module provides mapping functions between API responses and Type entities.
"""

from src.domain.entities.type import Type


class TypeMapper:
    """Mapper for converting between API and domain Type entities."""

    @staticmethod
    def from_dict(data: dict) -> Type:
        """Converts the API response to a Type entity.

        Args:
            data: Dictionary containing the API data.

        Returns:
            A Type entity.
        """
        return Type(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"],
        )

    @staticmethod
    def to_dict(type_entity: Type) -> dict:
        """Converts a Type entity to a dictionary.

        Args:
            type_entity: A Type entity.

        Returns:
            A dictionary representing the series type.
        """
        return {
            "id": type_entity.id,
            "title": type_entity.title,
            "to_display": type_entity.to_display,
        }
