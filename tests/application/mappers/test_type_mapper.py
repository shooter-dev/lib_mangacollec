"""Tests pour le TypeMapper.

This module contains unit tests for the TypeMapper.
"""

import pytest

from src.application.mappers.type_mapper import TypeMapper
from src.domain.entities import Type


class TestTypeMapper:
    """Tests pour le mapper Type."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Type."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

        type = TypeMapper.from_dict(data)

        assert isinstance(type, Type)
        assert type.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert type.title == "Manga"
        assert type.to_display is True

    def test_from_dict_not_displayed(self) -> None:
        """Test de conversion d'un type de série non affiché."""
        data = {
            "id": "test-id",
            "title": "Hidden Type",
            "to_display": False,
        }

        type = TypeMapper.from_dict(data)

        assert type.id == "test-id"
        assert type.title == "Hidden Type"
        assert type.to_display is False

    def test_from_dict_manhwa(self) -> None:
        """Test de conversion d'un type Manhwa."""
        data = {
            "id": "test-id",
            "title": "Manhwa",
            "to_display": True,
        }

        type = TypeMapper.from_dict(data)

        assert type.title == "Manhwa"
        assert type.to_display is True

    def test_to_dict(self) -> None:
        """Test de conversion d'un Type en dictionnaire."""
        type = Type(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Manga",
            to_display=True,
        )

        result = TypeMapper.to_dict(type)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

    def test_to_dict_not_displayed(self) -> None:
        """Test de conversion d'un type non affiché en dictionnaire."""
        type = Type(
            id="test-id",
            title="Hidden Type",
            to_display=False,
        )

        result = TypeMapper.to_dict(type)

        assert result == {
            "id": "test-id",
            "title": "Hidden Type",
            "to_display": False,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test Type",
            "to_display": True,
        }

        # dict -> entity -> dict
        type = TypeMapper.from_dict(original_data)
        result_data = TypeMapper.to_dict(type)

        assert result_data == original_data
