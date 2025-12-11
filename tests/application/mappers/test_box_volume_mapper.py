"""Tests unitaires pour BoxVolumeMapper."""

import pytest

from mangacollec.application.mappers import BoxVolumeMapper
from mangacollec.domain.entities import BoxVolume


class TestBoxVolumeMapperFromDict:
    """Tests pour la méthode from_dict."""

    def test_from_dict_with_all_fields(self):
        """Test la conversion d'un dict complet en BoxVolume."""
        # Arrange
        data = {
            "id": "box-volume-123",
            "title": "One Piece - Édition Coffret",
            "number": 1,
            "release_date": "2022-09-30",
            "isbn": "978-2-7234-5678-9",
            "asin": "B07XYZ1234",
            "edition_id": "edition-456",
            "possessions_count": 150,
            "not_sold": False,
            "image_url": "https://example.com/box-volume.jpg",
        }

        # Act
        box_volume = BoxVolumeMapper.from_dict(data)

        # Assert
        assert isinstance(box_volume, BoxVolume)
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

    def test_from_dict_without_optional_fields(self):
        """Test la conversion sans champs optionnels."""
        # Arrange
        data = {
            "id": "box-volume-123",
            "number": 2,
            "edition_id": "edition-456",
            "not_sold": False,
        }

        # Act
        box_volume = BoxVolumeMapper.from_dict(data)

        # Assert
        assert isinstance(box_volume, BoxVolume)
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

    def test_from_dict_with_not_sold_true(self):
        """Test la conversion avec not_sold=True."""
        # Arrange
        data = {
            "id": "box-volume-123",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": True,
        }

        # Act
        box_volume = BoxVolumeMapper.from_dict(data)

        # Assert
        assert box_volume.not_sold is True

    def test_from_dict_immutability(self):
        """Test que l'entité BoxVolume créée est immuable."""
        # Arrange
        data = {
            "id": "box-volume-123",
            "number": 1,
            "edition_id": "edition-456",
            "not_sold": False,
        }

        # Act
        box_volume = BoxVolumeMapper.from_dict(data)

        # Assert
        with pytest.raises(Exception):  # FrozenInstanceError
            box_volume.title = "Modified Title"  # type: ignore


class TestBoxVolumeMapperToDict:
    """Tests pour la méthode to_dict."""

    def test_to_dict_with_all_fields(self):
        """Test la conversion d'un BoxVolume complet en dictionnaire."""
        # Arrange
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

        # Act
        result = BoxVolumeMapper.to_dict(box_volume)

        # Assert
        assert isinstance(result, dict)
        assert result["id"] == "box-volume-123"
        assert result["title"] == "One Piece - Édition Coffret"
        assert result["number"] == 1
        assert result["release_date"] == "2022-09-30"
        assert result["isbn"] == "978-2-7234-5678-9"
        assert result["asin"] == "B07XYZ1234"
        assert result["edition_id"] == "edition-456"
        assert result["possessions_count"] == 150
        assert result["not_sold"] is False
        assert result["image_url"] == "https://example.com/box-volume.jpg"

    def test_to_dict_without_optional_fields(self):
        """Test la conversion d'un BoxVolume sans champs optionnels."""
        # Arrange
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

        # Act
        result = BoxVolumeMapper.to_dict(box_volume)

        # Assert
        assert isinstance(result, dict)
        assert result["id"] == "box-volume-123"
        assert result["title"] is None
        assert result["number"] == 2
        assert result["release_date"] is None
        assert result["isbn"] is None
        assert result["asin"] is None
        assert result["edition_id"] == "edition-456"
        assert result["possessions_count"] is None
        assert result["not_sold"] is False
        assert result["image_url"] is None

    def test_to_dict_contains_all_fields(self):
        """Test que to_dict retourne tous les champs."""
        # Arrange
        box_volume = BoxVolume(
            id="box-volume-123",
            title="Test",
            number=1,
            release_date="2022-09-30",
            isbn="978-2-7234-5678-9",
            asin="B07XYZ1234",
            edition_id="edition-456",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

        # Act
        result = BoxVolumeMapper.to_dict(box_volume)

        # Assert
        assert len(result) == 10
        assert "id" in result
        assert "title" in result
        assert "number" in result
        assert "release_date" in result
        assert "isbn" in result
        assert "asin" in result
        assert "edition_id" in result
        assert "possessions_count" in result
        assert "not_sold" in result
        assert "image_url" in result

    def test_to_dict_roundtrip_conversion(self):
        """Test que from_dict(to_dict(box_volume)) == box_volume."""
        # Arrange
        original = BoxVolume(
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

        # Act
        dict_data = BoxVolumeMapper.to_dict(original)
        reconstructed = BoxVolumeMapper.from_dict(dict_data)

        # Assert
        assert original == reconstructed
