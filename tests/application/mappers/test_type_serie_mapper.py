"""Tests pour le TypeSerieMapper.

This module contains unit tests for the TypeSerieMapper.
"""

import pytest

from src.application.mappers.type_serie_mapper import TypeSerieMapper
from src.domain.entities import TypeSerie


class TestTypeSerieMapper:
    """Tests pour le mapper TypeSerie."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en TypeSerie."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

        type_serie = TypeSerieMapper.from_dict(data)

        assert isinstance(type_serie, TypeSerie)
        assert type_serie.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert type_serie.title == "Manga"
        assert type_serie.to_display is True

    def test_from_dict_not_displayed(self) -> None:
        """Test de conversion d'un type de série non affiché."""
        data = {
            "id": "test-id",
            "title": "Hidden Type",
            "to_display": False,
        }

        type_serie = TypeSerieMapper.from_dict(data)

        assert type_serie.id == "test-id"
        assert type_serie.title == "Hidden Type"
        assert type_serie.to_display is False

    def test_from_dict_manhwa(self) -> None:
        """Test de conversion d'un type Manhwa."""
        data = {
            "id": "test-id",
            "title": "Manhwa",
            "to_display": True,
        }

        type_serie = TypeSerieMapper.from_dict(data)

        assert type_serie.title == "Manhwa"
        assert type_serie.to_display is True

    def test_to_dict(self) -> None:
        """Test de conversion d'un TypeSerie en dictionnaire."""
        type_serie = TypeSerie(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Manga",
            to_display=True,
        )

        result = TypeSerieMapper.to_dict(type_serie)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

    def test_to_dict_not_displayed(self) -> None:
        """Test de conversion d'un type non affiché en dictionnaire."""
        type_serie = TypeSerie(
            id="test-id",
            title="Hidden Type",
            to_display=False,
        )

        result = TypeSerieMapper.to_dict(type_serie)

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
        type_serie = TypeSerieMapper.from_dict(original_data)
        result_data = TypeSerieMapper.to_dict(type_serie)

        assert result_data == original_data
