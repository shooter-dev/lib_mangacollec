"""Tests pour l'entité Type.

This module contains unit tests for Type entity.
"""

import pytest

from mangacollec.domain.entities import TypeSerie


class TestType:
    """Tests pour l'entité Type."""

    def test_create_type_serie_with_all_fields(self) -> None:
        """Test de création d'un type de série avec tous les champs."""
        type_serie = TypeSerie(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Manga",
            to_display=True,
        )

        assert type_serie.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert type_serie.title == "Manga"
        assert type_serie.to_display is True

    def test_create_type_serie_not_displayed(self) -> None:
        """Test de création d'un type de série non affiché."""
        type_serie = TypeSerie(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            title="Hidden Type",
            to_display=False,
        )

        assert type_serie.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
        assert type_serie.title == "Hidden Type"
        assert type_serie.to_display is False

    def test_create_type_serie_manhwa(self) -> None:
        """Test de création d'un type de série Manhwa."""
        type_serie = TypeSerie(
            id="test-id",
            title="Manhwa",
            to_display=True,
        )

        assert type_serie.title == "Manhwa"
        assert type_serie.to_display is True

    def test_type_serie_is_frozen(self) -> None:
        """Test que l'entité Type est immuable."""
        type_serie = TypeSerie(
            id="test-id",
            title="Test Type",
            to_display=True,
        )

        with pytest.raises(AttributeError):
            type_serie.title = "New Title"

    def test_type_serie_equality(self) -> None:
        """Test de l'égalité entre deux types de série identiques."""
        type1 = TypeSerie(
            id="test-id",
            title="Test",
            to_display=True,
        )
        type2 = TypeSerie(
            id="test-id",
            title="Test",
            to_display=True,
        )

        assert type1 == type2

    def test_type_serie_inequality(self) -> None:
        """Test de l'inégalité entre deux types de série différents."""
        type1 = TypeSerie(
            id="id1",
            title="Manga",
            to_display=True,
        )
        type2 = TypeSerie(
            id="id2",
            title="Manhwa",
            to_display=True,
        )

        assert type1 != type2
