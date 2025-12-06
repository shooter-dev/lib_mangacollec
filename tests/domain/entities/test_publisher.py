"""Tests pour l'entité Publisher.

This module contains unit tests for Publisher entity.
"""

import pytest

from src.domain.entities import Publisher


class TestPublisher:
    """Tests pour l'entité Publisher."""

    def test_create_publisher_with_all_fields(self) -> None:
        """Test de création d'un éditeur avec tous les champs."""
        publisher = Publisher(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

        assert publisher.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert publisher.title == "Kana"
        assert publisher.closed is False
        assert publisher.editions_count == 150
        assert publisher.no_amazon is False

    def test_create_publisher_closed(self) -> None:
        """Test de création d'un éditeur fermé."""
        publisher = Publisher(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            title="Defunct Publisher",
            closed=True,
            editions_count=50,
            no_amazon=True,
        )

        assert publisher.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
        assert publisher.title == "Defunct Publisher"
        assert publisher.closed is True
        assert publisher.editions_count == 50
        assert publisher.no_amazon is True

    def test_create_publisher_no_editions(self) -> None:
        """Test de création d'un éditeur sans éditions."""
        publisher = Publisher(
            id="test-id",
            title="New Publisher",
            closed=False,
            editions_count=0,
            no_amazon=False,
        )

        assert publisher.editions_count == 0

    def test_publisher_is_frozen(self) -> None:
        """Test que l'entité Publisher est immuable."""
        publisher = Publisher(
            id="test-id",
            title="Test Publisher",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )

        with pytest.raises(AttributeError):
            publisher.title = "New Title"

    def test_publisher_equality(self) -> None:
        """Test de l'égalité entre deux publishers identiques."""
        publisher1 = Publisher(
            id="test-id",
            title="Test",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )
        publisher2 = Publisher(
            id="test-id",
            title="Test",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )

        assert publisher1 == publisher2

    def test_publisher_inequality(self) -> None:
        """Test de l'inégalité entre deux publishers différents."""
        publisher1 = Publisher(
            id="id1",
            title="Test1",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )
        publisher2 = Publisher(
            id="id2",
            title="Test2",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )

        assert publisher1 != publisher2
