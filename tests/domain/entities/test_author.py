"""Tests pour les entités Author et AuthorListItem.

This module contains unit tests for Author and AuthorListItem entities.
"""

import pytest

from src.domain.entities import Author, AuthorListItem


class TestAuthor:
    """Tests pour l'entité Author."""

    def test_create_author_with_all_fields(self) -> None:
        """Test de création d'un auteur avec tous les champs."""
        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

    def test_create_author_without_first_name(self) -> None:
        """Test de création d'un auteur sans prénom."""
        author = Author(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            name="Boichi",
            first_name=None,
            tasks_count=14,
        )

        assert author.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
        assert author.name == "Boichi"
        assert author.first_name is None
        assert author.tasks_count == 14

    def test_author_is_frozen(self) -> None:
        """Test que l'entité Author est immuable."""
        author = Author(
            id="test-id",
            name="Test",
            first_name="Author",
            tasks_count=1,
        )

        with pytest.raises(AttributeError):
            author.name = "NewName"


class TestAuthorListItem:
    """Tests pour l'entité AuthorListItem."""

    def test_create_author_list_item(self) -> None:
        """Test de création d'un AuthorListItem."""
        item = AuthorListItem(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            full_name="Masashi Kishimoto",
        )

        assert item.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert item.full_name == "Masashi Kishimoto"

    def test_author_list_item_is_frozen(self) -> None:
        """Test que l'entité AuthorListItem est immuable."""
        item = AuthorListItem(
            id="test-id",
            full_name="Test Author",
        )

        with pytest.raises(AttributeError):
            item.full_name = "New Name"
