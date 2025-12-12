"""Tests for TypeSerie mapper."""

from mangacollec.application.mappers import TypeSerieMapper
from mangacollec.domain.entities import TypeSerie


def test_from_dict():
    """Test conversion d'un dictionnaire en TypeSerie."""
    data = {
        "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "title": "Manga",
        "to_display": True,
    }

    type_serie = TypeSerieMapper.from_dict(data)

    assert type_serie.id == "106f524e-7283-44b8-aa84-25e9a7fb1f7d"
    assert type_serie.title == "Manga"
    assert type_serie.to_display is True


def test_from_dict_with_default_to_display():
    """Test conversion avec to_display manquant (valeur par défaut)."""
    data = {
        "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "title": "Manga",
    }

    type_serie = TypeSerieMapper.from_dict(data)

    assert type_serie.to_display is False


def test_to_dict():
    """Test conversion d'un TypeSerie en dictionnaire."""
    type_serie = TypeSerie(
        id="106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        title="Manga",
        to_display=True,
    )

    data = TypeSerieMapper.to_dict(type_serie)

    assert data["id"] == "106f524e-7283-44b8-aa84-25e9a7fb1f7d"
    assert data["title"] == "Manga"
    assert data["to_display"] is True


def test_from_all_types_v1_response():
    """Test conversion de la réponse API V1 en GetAllTypesSerieV1Response."""
    api_response = [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": True,
        },
        {
            "id": "different-id",
            "title": "Manhwa",
            "to_display": False,
        },
    ]

    response = TypeSerieMapper.from_all_types_v1_response(api_response)

    assert len(response.types) == 2
    assert response.types[0].id == "106f524e-7283-44b8-aa84-25e9a7fb1f7d"
    assert response.types[0].title == "Manga"
    assert response.types[0].to_display is True
    assert response.types[1].id == "different-id"
    assert response.types[1].title == "Manhwa"
    assert response.types[1].to_display is False


def test_from_all_types_v1_response_empty():
    """Test conversion d'une réponse API V1 vide."""
    api_response = []

    response = TypeSerieMapper.from_all_types_v1_response(api_response)

    assert len(response.types) == 0
    assert response.types == []
