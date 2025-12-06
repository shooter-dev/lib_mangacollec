"""Tests pour le PublisherMapper.

This module contains unit tests for the PublisherMapper.
"""

import pytest

from src.application.mappers.publisher_mapper import PublisherMapper
from src.domain.entities import Publisher


class TestPublisherMapper:
    """Tests pour le mapper Publisher."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Publisher."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Kana",
            "closed": False,
            "editions_count": 150,
            "no_amazon": False,
        }

        publisher = PublisherMapper.from_dict(data)

        assert isinstance(publisher, Publisher)
        assert publisher.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert publisher.title == "Kana"
        assert publisher.closed is False
        assert publisher.editions_count == 150
        assert publisher.no_amazon is False

    def test_from_dict_closed_publisher(self) -> None:
        """Test de conversion d'un éditeur fermé."""
        data = {
            "id": "test-id",
            "title": "Defunct Publisher",
            "closed": True,
            "editions_count": 50,
            "no_amazon": True,
        }

        publisher = PublisherMapper.from_dict(data)

        assert publisher.id == "test-id"
        assert publisher.title == "Defunct Publisher"
        assert publisher.closed is True
        assert publisher.editions_count == 50
        assert publisher.no_amazon is True

    def test_from_dict_zero_editions(self) -> None:
        """Test de conversion d'un éditeur sans éditions."""
        data = {
            "id": "test-id",
            "title": "New Publisher",
            "closed": False,
            "editions_count": 0,
            "no_amazon": False,
        }

        publisher = PublisherMapper.from_dict(data)

        assert publisher.editions_count == 0

    def test_to_dict(self) -> None:
        """Test de conversion d'un Publisher en dictionnaire."""
        publisher = Publisher(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

        result = PublisherMapper.to_dict(publisher)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Kana",
            "closed": False,
            "editions_count": 150,
            "no_amazon": False,
        }

    def test_to_dict_closed_publisher(self) -> None:
        """Test de conversion d'un éditeur fermé en dictionnaire."""
        publisher = Publisher(
            id="test-id",
            title="Defunct Publisher",
            closed=True,
            editions_count=50,
            no_amazon=True,
        )

        result = PublisherMapper.to_dict(publisher)

        assert result == {
            "id": "test-id",
            "title": "Defunct Publisher",
            "closed": True,
            "editions_count": 50,
            "no_amazon": True,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test Publisher",
            "closed": False,
            "editions_count": 100,
            "no_amazon": False,
        }

        # dict -> entity -> dict
        publisher = PublisherMapper.from_dict(original_data)
        result_data = PublisherMapper.to_dict(publisher)

        assert result_data == original_data
