"""Tests pour l'entité BoxVolume.

This module contains unit tests for the BoxVolume entity.
"""

import pytest

from mangacollec.domain.entities import BoxVolume


class TestBoxVolume:
    """Tests pour l'entité BoxVolume."""

    def test_box_volume_creation_with_all_fields(self) -> None:
        """Test de création d'un BoxVolume avec tous les champs."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title="One Piece - Édition Coffret",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=150,
            not_sold=False,
            image_url="https://example.com/box-volume.jpg",
        )

        assert box_volume.id == "box-volume-123"
        assert box_volume.title == "One Piece - Édition Coffret"
        assert box_volume.number == 1
        assert box_volume.release_date == "2022-09-30"
        assert box_volume.isbn == "978-2-7234-5678-9"
        assert box_volume.asin == "B07XYZ1234"
        assert box_volume.edition_id == "edition-456"
        assert box_volume.possessions_count == 150
        assert box_volume.not_sold is False
        assert box_volume.image_url == "https://example.com/box-volume.jpg"

    def test_box_volume_creation_without_optional_fields(self) -> None:
        """Test de création d'un BoxVolume sans champs optionnels."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title=None,
            number=2,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=None,
            not_sold=False,
            image_url=None,
        )

        assert box_volume.id == "box-volume-123"
        assert box_volume.title is None
        assert box_volume.number == 2
        assert box_volume.release_date is None
        assert box_volume.isbn is None
        assert box_volume.asin is None
        assert box_volume.edition_id == "edition-456"
        assert box_volume.possessions_count is None
        assert box_volume.not_sold is False
        assert box_volume.image_url is None

    def test_box_volume_is_frozen(self) -> None:
        """Test que l'entité BoxVolume est immuable (frozen)."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title="Test Box Volume",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        with pytest.raises(AttributeError):
            box_volume.title = "Modified Title"  # type: ignore

    def test_box_volume_equality(self) -> None:
        """Test d'égalité entre deux BoxVolumes identiques."""
        box_volume1 = BoxVolume(
            id="box-volume-123",
            title="Box Volume Test",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        box_volume2 = BoxVolume(
            id="box-volume-123",
            title="Box Volume Test",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        assert box_volume1 == box_volume2

    def test_box_volume_inequality(self) -> None:
        """Test d'inégalité entre deux BoxVolumes différents."""
        box_volume1 = BoxVolume(
            id="box-volume-123",
            title="Box Volume Test",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        box_volume2 = BoxVolume(
            id="box-volume-456",
            title="Box Volume Test 2",
            number=2,
            release_date="2022-10-30",
            isbn="978-2-7234-9999-9",
            asin="B07XYZ9999",
            edition_id="edition-789",
            possessions_count=200,
            not_sold=True,
            image_url="https://example.com/image2.jpg",
        )

        assert box_volume1 != box_volume2

    def test_box_volume_with_not_sold(self) -> None:
        """Test d'un BoxVolume marqué comme non vendu."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title="Discontinued Box Volume",
            number=1,
            release_date="2020-01-15",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=50,
            not_sold=True,
            image_url="https://example.com/image.jpg",
        )

        assert box_volume.not_sold is True

    def test_box_volume_hash(self) -> None:
        """Test que le BoxVolume est hashable (car frozen)."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title="Test Box Volume",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        # Doit pouvoir être utilisé comme clé de dictionnaire
        box_volumes_dict = {box_volume: "test_value"}
        assert box_volumes_dict[box_volume] == "test_value"

    def test_box_volume_in_set(self) -> None:
        """Test qu'un BoxVolume peut être ajouté à un set (car hashable)."""
        box_volume1 = BoxVolume(
            id="box-volume-123",
            title="Box Volume Test",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        box_volume2 = BoxVolume(
            id="box-volume-456",
            title="Box Volume Test 2",
            number=2,
            release_date="2022-10-30",
            isbn="978-2-7234-9999-9",
            asin="B07XYZ9999",
            edition_id="edition-789",
            possessions_count=200,
            not_sold=True,
            image_url="https://example.com/image2.jpg",
        )

        box_volumes_set = {box_volume1, box_volume2}
        assert len(box_volumes_set) == 2
        assert box_volume1 in box_volumes_set
        assert box_volume2 in box_volumes_set
