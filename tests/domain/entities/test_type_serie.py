"""Tests for TypeSerie entity."""

import pytest

from mangacollec.domain.entities import TypeSerie


def test_type_serie_creation():
    """Test création d'un TypeSerie."""
    type_serie = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )

    assert type_serie.id == "106f524e-7283-44b8-aa84-25e9a7fb1f7d"
    assert type_serie.title == "Manga"
    assert type_serie.to_display is True


def test_type_serie_immutability():
    """Test immutabilité de TypeSerie."""
    type_serie = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )

    with pytest.raises(AttributeError):
        type_serie.title = "Manhwa"


def test_type_serie_equality():
    """Test égalité entre deux TypeSerie."""
    type_serie1 = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )
    type_serie2 = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )

    assert type_serie1 == type_serie2


def test_type_serie_inequality():
    """Test inégalité entre deux TypeSerie différents."""
    type_serie1 = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )
    type_serie2 = TypeSerie(
        id="different-id",
        title="Manhwa",
        to_display=False,
    )

    assert type_serie1 != type_serie2


def test_type_serie_with_to_display_false():
    """Test création d'un TypeSerie avec to_display=False."""
    type_serie = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=False,
    )

    assert type_serie.to_display is False
