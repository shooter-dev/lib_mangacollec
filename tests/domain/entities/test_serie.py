"""Tests pour les entités Serie et SerieListItem.

This module contains unit tests for Serie and SerieListItem entities.
"""

import pytest

from mangacollec.domain.entities import Serie, SerieListItem


class TestSerie:
    """Tests pour l'entité Serie."""

    def test_create_serie_with_all_fields(self) -> None:
        """Test de création d'une série avec tous les champs."""
        serie = Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
            type_id="e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1", "kind-2"],
        )

        assert serie.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert serie.title == "Naruto"
        assert serie.type_id == "e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d"
        assert serie.adult_content is False
        assert serie.editions_count == 12
        assert serie.tasks_count == 5
        assert serie.kinds_ids == ["kind-1", "kind-2"]

    def test_create_serie_without_kinds_ids(self) -> None:
        """Test de création d'une série sans kinds_ids."""
        serie = Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="One Piece",
            type_id="e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            adult_content=False,
            editions_count=25,
            tasks_count=3,
            kinds_ids=None,
        )

        assert serie.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert serie.title == "One Piece"
        assert serie.type_id == "e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d"
        assert serie.adult_content is False
        assert serie.editions_count == 25
        assert serie.tasks_count == 3
        assert serie.kinds_ids is None

    def test_create_serie_with_adult_content(self) -> None:
        """Test de création d'une série avec contenu adulte."""
        serie = Serie(
            id="test-id",
            title="Test Adult Serie",
            type_id="type-id",
            adult_content=True,
            editions_count=5,
            tasks_count=2,
            kinds_ids=None,
        )

        assert serie.adult_content is True

    def test_serie_is_frozen(self) -> None:
        """Test que l'entité Serie est immuable."""
        serie = Serie(
            id="test-id",
            title="Test",
            type_id="type-id",
            adult_content=False,
            editions_count=1,
            tasks_count=1,
        )

        with pytest.raises(AttributeError):
            serie.title = "New Title"


class TestSerieListItem:
    """Tests pour l'entité SerieListItem."""

    def test_create_serie_list_item(self) -> None:
        """Test de création d'un SerieListItem."""
        item = SerieListItem(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
        )

        assert item.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert item.title == "Naruto"

    def test_serie_list_item_is_frozen(self) -> None:
        """Test que l'entité SerieListItem est immuable."""
        item = SerieListItem(
            id="test-id",
            title="Test Serie",
        )

        with pytest.raises(AttributeError):
            item.title = "New Title"
