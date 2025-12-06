"""Tests pour le EditionMapper.

This module contains unit tests for the EditionMapper.
"""

import pytest

from src.application.mappers.edition_mapper import EditionMapper
from src.domain.entities import Edition


class TestEditionMapper:
    """Tests pour le mapper Edition."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Edition."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Edition Collector",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 1443,
        }

        edition = EditionMapper.from_dict(data)

        assert isinstance(edition, Edition)
        assert edition.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert edition.title == "Edition Collector"
        assert edition.series_id == "series-123"
        assert edition.publisher_id == "publisher-456"
        assert edition.parent_edition_id == "parent-789"
        assert edition.volumes_count == 72
        assert edition.last_volume_number == 72
        assert edition.commercial_stop is False
        assert edition.not_finished is False
        assert edition.follow_editions_count == 1443

    def test_from_dict_without_title(self) -> None:
        """Test de conversion sans titre."""
        data = {
            "id": "test-id",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.id == "test-id"
        assert edition.title is None
        assert edition.series_id == "series-123"
        assert edition.publisher_id == "publisher-456"

    def test_from_dict_without_parent_edition(self) -> None:
        """Test de conversion sans édition parente."""
        data = {
            "id": "test-id",
            "title": "Main Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.parent_edition_id is None

    def test_from_dict_without_last_volume_number(self) -> None:
        """Test de conversion sans numéro de dernier volume."""
        data = {
            "id": "test-id",
            "title": "Ongoing Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.last_volume_number is None

    def test_from_dict_commercial_stop(self) -> None:
        """Test de conversion avec arrêt commercial."""
        data = {
            "id": "test-id",
            "title": "Stopped Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 10,
            "last_volume_number": 10,
            "commercial_stop": True,
            "not_finished": False,
            "follow_editions_count": 50,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.commercial_stop is True
        assert edition.not_finished is False

    def test_from_dict_not_finished(self) -> None:
        """Test de conversion avec série non terminée."""
        data = {
            "id": "test-id",
            "title": "Ongoing Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "volumes_count": 50,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 500,
        }

        edition = EditionMapper.from_dict(data)

        assert edition.not_finished is True
        assert edition.commercial_stop is False

    def test_to_dict(self) -> None:
        """Test de conversion d'une Edition en dictionnaire."""
        edition = Edition(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            title="Edition Collector",
            series_id="series-123",
            publisher_id="publisher-456",
            parent_edition_id="parent-789",
            volumes_count=72,
            last_volume_number=72,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=1443,
        )

        result = EditionMapper.to_dict(edition)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "title": "Edition Collector",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 1443,
        }

    def test_to_dict_with_nulls(self) -> None:
        """Test de conversion avec valeurs nulles."""
        edition = Edition(
            id="test-id",
            title=None,
            series_id="series-123",
            publisher_id="publisher-456",
            parent_edition_id=None,
            volumes_count=50,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=100,
        )

        result = EditionMapper.to_dict(edition)

        assert result == {
            "id": "test-id",
            "title": None,
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": None,
            "volumes_count": 50,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

    def test_round_trip_conversion(self) -> None:
        """Test de conversion bidirectionnelle (dict -> entity -> dict)."""
        original_data = {
            "id": "test-id",
            "title": "Test Edition",
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": "parent-789",
            "volumes_count": 100,
            "last_volume_number": 100,
            "commercial_stop": False,
            "not_finished": False,
            "follow_editions_count": 200,
        }

        # dict -> entity -> dict
        edition = EditionMapper.from_dict(original_data)
        result_data = EditionMapper.to_dict(edition)

        assert result_data == original_data

    def test_round_trip_conversion_with_nulls(self) -> None:
        """Test de conversion bidirectionnelle avec valeurs nulles."""
        original_data = {
            "id": "test-id",
            "title": None,
            "series_id": "series-123",
            "publisher_id": "publisher-456",
            "parent_edition_id": None,
            "volumes_count": 50,
            "last_volume_number": None,
            "commercial_stop": False,
            "not_finished": True,
            "follow_editions_count": 100,
        }

        # dict -> entity -> dict
        edition = EditionMapper.from_dict(original_data)
        result_data = EditionMapper.to_dict(edition)

        assert result_data == original_data
