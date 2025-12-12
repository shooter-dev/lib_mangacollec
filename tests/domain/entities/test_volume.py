"""Tests pour l'entité Volume.

This module contains unit tests for the Volume entity.
"""

import pytest

from mangacollec.domain.entities import Volume


class TestVolume:
    """Tests pour l'entité Volume."""

    def test_volume_creation_with_all_fields(self) -> None:
        """Test de création d'un volume avec tous les champs."""
        volume = Volume(
            id="volume-123",
            title="Tome 1 : Le Début",
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=150,
            not_sold=False,
            image_url="https://example.com/image.jpg",
            nb_pages=192,
            content="Chapitres 1-3",
        )

        assert volume.id == "volume-123"
        assert volume.title == "Tome 1 : Le Début"
        assert volume.number == 1
        assert volume.release_date == "2023-01-15"
        assert volume.isbn == "9782012345678"
        assert volume.asin == "2012345678"
        assert volume.edition_id == "edition-456"
        assert volume.possessions_count == 150
        assert volume.not_sold is False
        assert volume.image_url == "https://example.com/image.jpg"
        assert volume.nb_pages == 192
        assert volume.content == "Chapitres 1-3"

    def test_volume_creation_with_minimum_fields(self) -> None:
        """Test de création d'un volume avec les champs minimum obligatoires."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=None,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.id == "volume-123"
        assert volume.title is None
        assert volume.number == 1
        assert volume.release_date is None
        assert volume.isbn is None
        assert volume.asin is None
        assert volume.edition_id == "edition-456"
        assert volume.possessions_count is None
        assert volume.not_sold is False
        assert volume.image_url is None
        assert volume.nb_pages is None
        assert volume.content is None

    def test_volume_creation_without_isbn(self) -> None:
        """Test de création d'un volume sans ISBN."""
        volume = Volume(
            id="volume-123",
            title="Volume Sans ISBN",
            number=1,
            release_date="2023-01-15",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=0,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.id == "volume-123"
        assert volume.title == "Volume Sans ISBN"
        assert volume.isbn is None
        assert volume.asin is None

    def test_volume_creation_not_sold(self) -> None:
        """Test de création d'un volume non vendu."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=0,
            not_sold=True,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.not_sold is True
        assert volume.possessions_count == 0

    def test_volume_is_frozen(self) -> None:
        """Test que l'entité Volume est immuable (frozen)."""
        volume = Volume(
            id="volume-123",
            title="Test Volume",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=10,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        with pytest.raises(AttributeError):
            volume.title = "Modified Title"  # type: ignore

        with pytest.raises(AttributeError):
            volume.number = 2  # type: ignore

        with pytest.raises(AttributeError):
            volume.not_sold = True  # type: ignore

    def test_volume_equality(self) -> None:
        """Test d'égalité entre deux volumes identiques."""
        volume1 = Volume(
            id="volume-123",
            title="Volume Test",
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url="https://example.com/image.jpg",
            nb_pages=192,
            content="Chapitres 1-3",
        )

        volume2 = Volume(
            id="volume-123",
            title="Volume Test",
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url="https://example.com/image.jpg",
            nb_pages=192,
            content="Chapitres 1-3",
        )

        assert volume1 == volume2

    def test_volume_inequality(self) -> None:
        """Test d'inégalité entre deux volumes différents."""
        volume1 = Volume(
            id="volume-123",
            title="Volume 1",
            number=1,
            release_date="2023-01-15",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        volume2 = Volume(
            id="volume-456",
            title="Volume 2",
            number=2,
            release_date="2023-02-15",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=40,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume1 != volume2

    def test_volume_with_zero_possessions(self) -> None:
        """Test d'un volume sans possesseurs."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=0,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.possessions_count == 0
        assert volume.not_sold is False

    def test_volume_with_high_number(self) -> None:
        """Test d'un volume avec un numéro élevé."""
        volume = Volume(
            id="volume-123",
            title="Tome 100",
            number=100,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=25,
            not_sold=False,
            image_url=None,
            nb_pages=300,
            content=None,
        )

        assert volume.number == 100
        assert volume.nb_pages == 300

    def test_volume_with_content_description(self) -> None:
        """Test d'un volume avec description du contenu."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=75,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content="Chapitres 1-5 + Extra",
        )

        assert volume.content == "Chapitres 1-5 + Extra"

    def test_volume_hash(self) -> None:
        """Test que le volume est hashable (car frozen)."""
        volume = Volume(
            id="volume-123",
            title="Test Volume",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        # Doit pouvoir être utilisé comme clé de dictionnaire
        volumes_dict = {volume: "test_value"}
        assert volumes_dict[volume] == "test_value"

    def test_volume_in_set(self) -> None:
        """Test qu'un volume peut être ajouté à un set (car hashable)."""
        volume1 = Volume(
            id="volume-123",
            title="Volume 1",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        volume2 = Volume(
            id="volume-456",
            title="Volume 2",
            number=2,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=40,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        volumes_set = {volume1, volume2}
        assert len(volumes_set) == 2
        assert volume1 in volumes_set
        assert volume2 in volumes_set

    def test_volume_repr_is_not_necessary(self) -> None:
        """Test que le __repr__ fonctionne (dataclass fournit un repr par défaut)."""
        volume = Volume(
            id="volume-123",
            title="Test Volume",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        repr_str = repr(volume)
        assert "volume-123" in repr_str
        assert "Test Volume" in repr_str

    def test_volume_with_asin_only(self) -> None:
        """Test d'un volume avec seulement ASIN (Amazon)."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date="2023-01-15",
            isbn=None,
            asin="B0BXYZ123",
            edition_id="edition-456",
            possessions_count=30,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.isbn is None
        assert volume.asin == "B0BXYZ123"

    def test_volume_with_both_isbn_and_asin(self) -> None:
        """Test d'un volume avec ISBN et ASIN."""
        volume = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=75,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        assert volume.isbn == "9782012345678"
        assert volume.asin == "2012345678"
