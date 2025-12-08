"""Tests pour l'entité Edition.

This module contains unit tests for the Edition entity.
"""

import pytest

from src.domain.entities import Edition


class TestEdition:
    """Tests pour l'entité Edition."""

    def test_edition_creation_with_all_fields(self) -> None:
        """Test de création d'une édition avec tous les champs."""
        edition = Edition(
            id="edition-123",
            title="Edition Collector",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id="parent-101",
            volumes_count=72,
            last_volume_number=72,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=1443,
        )

        assert edition.id == "edition-123"
        assert edition.title == "Edition Collector"
        assert edition.series_id == "series-456"
        assert edition.publisher_id == "publisher-789"
        assert edition.parent_edition_id == "parent-101"
        assert edition.volumes_count == 72
        assert edition.last_volume_number == 72
        assert edition.commercial_stop is False
        assert edition.not_finished is False
        assert edition.follow_editions_count == 1443

    def test_edition_creation_without_optional_fields(self) -> None:
        """Test de création d'une édition sans champs optionnels."""
        edition = Edition(
            id="edition-123",
            title=None,
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=50,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=100,
        )

        assert edition.id == "edition-123"
        assert edition.title is None
        assert edition.parent_edition_id is None
        assert edition.last_volume_number is None
        assert edition.not_finished is True

    def test_edition_is_frozen(self) -> None:
        """Test que l'entité Edition est immuable (frozen)."""
        edition = Edition(
            id="edition-123",
            title="Test Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        with pytest.raises(AttributeError):
            edition.title = "Modified Title"  # type: ignore

    def test_edition_equality(self) -> None:
        """Test d'égalité entre deux éditions identiques."""
        edition1 = Edition(
            id="edition-123",
            title="Edition Test",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        edition2 = Edition(
            id="edition-123",
            title="Edition Test",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        assert edition1 == edition2

    def test_edition_inequality(self) -> None:
        """Test d'inégalité entre deux éditions différentes."""
        edition1 = Edition(
            id="edition-123",
            title="Edition Test",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        edition2 = Edition(
            id="edition-456",
            title="Edition Test 2",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=20,
            last_volume_number=20,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=100,
        )

        assert edition1 != edition2

    def test_edition_with_commercial_stop(self) -> None:
        """Test d'une édition avec arrêt commercial."""
        edition = Edition(
            id="edition-123",
            title="Stopped Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=True,
            not_finished=False,
            follow_editions_count=50,
        )

        assert edition.commercial_stop is True
        assert edition.not_finished is False

    def test_edition_not_finished(self) -> None:
        """Test d'une édition non terminée."""
        edition = Edition(
            id="edition-123",
            title="Ongoing Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=50,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=500,
        )

        assert edition.not_finished is True
        assert edition.last_volume_number is None

    def test_edition_with_parent(self) -> None:
        """Test d'une édition avec une édition parente."""
        edition = Edition(
            id="edition-child",
            title="Edition Deluxe",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id="edition-parent",
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=100,
        )

        assert edition.parent_edition_id == "edition-parent"

    def test_edition_hash(self) -> None:
        """Test que l'édition est hashable (car frozen)."""
        edition = Edition(
            id="edition-123",
            title="Test Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        # Doit pouvoir être utilisé comme clé de dictionnaire
        editions_dict = {edition: "test_value"}
        assert editions_dict[edition] == "test_value"

    def test_edition_in_set(self) -> None:
        """Test qu'une édition peut être ajoutée à un set (car hashable)."""
        edition1 = Edition(
            id="edition-123",
            title="Test Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        edition2 = Edition(
            id="edition-456",
            title="Test Edition 2",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=20,
            last_volume_number=20,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=100,
        )

        editions_set = {edition1, edition2}
        assert len(editions_set) == 2
        assert edition1 in editions_set
        assert edition2 in editions_set
