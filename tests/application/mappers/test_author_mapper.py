"""Tests pour le AuthorMapper.

This module contains unit tests for the AuthorMapper.
"""

import pytest

from src.application.mappers.author_mapper import AuthorMapper
from src.domain.entities import Author, AuthorListItem


class TestAuthorMapper:
    """Tests pour le mapper Author."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Author."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
        }

        author = AuthorMapper.from_dict(data)

        assert isinstance(author, Author)
        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

    def test_from_dict_without_first_name(self) -> None:
        """Test de conversion sans first_name."""
        data = {
            "id": "test-id",
            "name": "Boichi",
            "tasks_count": 14,
        }

        author = AuthorMapper.from_dict(data)

        assert author.id == "test-id"
        assert author.name == "Boichi"
        assert author.first_name is None
        assert author.tasks_count == 14

    def test_from_dict_without_tasks_count(self) -> None:
        """Test de conversion sans tasks_count (valeur par défaut)."""
        data = {
            "id": "test-id",
            "name": "Test",
            "first_name": "Author",
        }

        author = AuthorMapper.from_dict(data)

        assert author.tasks_count == 0

    def test_to_dict(self) -> None:
        """Test de conversion d'un Author en dictionnaire."""
        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

        result = AuthorMapper.to_dict(author)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
        }

    def test_to_list_item_with_first_name(self) -> None:
        """Test de conversion d'un Author en AuthorListItem avec prénom."""
        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

        item = AuthorMapper.to_list_item(author)

        assert isinstance(item, AuthorListItem)
        assert item.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert item.full_name == "Masashi Kishimoto"

    def test_to_list_item_without_first_name(self) -> None:
        """Test de conversion d'un Author en AuthorListItem sans prénom."""
        author = Author(
            id="test-id",
            name="Boichi",
            first_name=None,
            tasks_count=14,
        )

        item = AuthorMapper.to_list_item(author)

        assert item.id == "test-id"
        assert item.full_name == "Boichi"
