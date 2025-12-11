"""Tests pour l'entité Kind."""

import pytest

from mangacollec.domain.entities import Kind


class TestKindEntity:
    """Tests pour l'entité Kind."""

    def test_kind_creation(self) -> None:
        """Test la création d'une entité Kind."""
        kind = Kind(
            id="1",
            name="Manga",
            name_en="Manga",
        )

        assert kind.id == "1"
        assert kind.name == "Manga"
        assert kind.name_en == "Manga"

    def test_kind_immutability(self) -> None:
        """Test que l'entité Kind est immuable."""
        kind = Kind(
            id="1",
            name="Manga",
            name_en="Manga",
        )

        with pytest.raises(AttributeError):
            kind.name = "Comics"  # type: ignore[misc]

    def test_kind_equality(self) -> None:
        """Test l'égalité entre deux entités Kind."""
        kind1 = Kind(id="1", name="Manga", name_en="Manga")
        kind2 = Kind(id="1", name="Manga", name_en="Manga")
        kind3 = Kind(id="2", name="Comics", name_en="Comics")

        assert kind1 == kind2
        assert kind1 != kind3
