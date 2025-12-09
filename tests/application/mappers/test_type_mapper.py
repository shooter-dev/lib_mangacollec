"""Tests pour le TypeSerieMapper.

This module contains unit tests for the TypeSerieMapper.
"""

from mangacollec.application.mappers import TypeSerieMapper
from mangacollec.domain.entities import TypeSerie


class TestTypeSerieMapper:
    """Tests pour le mapper TypeSerie."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en TypeSerie."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

        type = TypeSerieMapper.from_dict(data)

        assert isinstance(type, TypeSerie)
        assert type.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert type.title == "Manga"
        assert type.to_display is True

    def test_from_dict_not_displayed(self) -> None:
        """Test de conversion d'un type de série non affiché."""
        data = {
            "id": "test-id",
            "title": "Hidden TypeSerie",
            "to_display": False,
        }

        type = TypeSerieMapper.from_dict(data)

        assert type.id == "test-id"
        assert type.title == "Hidden TypeSerie"
        assert type.to_display is False

    def test_from_dict_manhwa(self) -> None:
        """Test de conversion d'un type Manhwa."""
        data = {
            "id": "test-id",
            "title": "Manhwa",
            "to_display": True,
        }

        type = TypeSerieMapper.from_dict(data)

        assert type.title == "Manhwa"
        assert type.to_display is True

    def test_to_dict(self) -> None:
        """Test de conversion d'un TypeSerie en dictionnaire."""
        type = TypeSerie(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Manga",
            to_display=True,
        )

        result = TypeSerieMapper.to_dict(type)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Manga",
            "to_display": True,
        }

    def test_to_dict_not_displayed(self) -> None:
        """Test de conversion d'un type non affiché en dictionnaire."""
        type = TypeSerie(
            id="test-id",
            title="Hidden TypeSerie",
            to_display=False,
        )

        result = TypeSerieMapper.to_dict(type)

        assert result == {
            "id": "test-id",
            "title": "Hidden TypeSerie",
            "to_display": False,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test TypeSerie",
            "to_display": True,
        }

        # dict -> entity -> dict
        type = TypeSerieMapper.from_dict(original_data)
        result_data = TypeSerieMapper.to_dict(type)

        assert result_data == original_data
