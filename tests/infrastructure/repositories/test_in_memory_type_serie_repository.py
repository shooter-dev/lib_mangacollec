"""Tests for InMemory TypeSerie repository."""

from mangacollec.domain.entities import TypeSerie
from mangacollec.infrastructure.repositories import InMemoryTypeSerieRepository


def test_get_all_types_v1_empty():
    """Test récupération de tous les types avec un repository vide."""
    repo = InMemoryTypeSerieRepository()

    result = repo.get_all_types_v1()

    assert len(result.types) == 0


def test_get_all_types_v1_with_data():
    """Test récupération de tous les types avec des données."""
    repo = InMemoryTypeSerieRepository()
    type1 = TypeSerie(id="1", title="Manga", to_display=True)
    type2 = TypeSerie(id="2", title="Manhwa", to_display=False)

    repo.add(type1)
    repo.add(type2)

    result = repo.get_all_types_v1()

    assert len(result.types) == 2
    assert type1 in result.types
    assert type2 in result.types


def test_add_type_serie():
    """Test ajout d'un type de série."""
    repo = InMemoryTypeSerieRepository()
    type_serie = TypeSerie(id="1", title="Manga", to_display=True)

    repo.add(type_serie)

    result = repo.get_all_types_v1()
    assert len(result.types) == 1
    assert result.types[0] == type_serie


def test_clear():
    """Test vidage du repository."""
    repo = InMemoryTypeSerieRepository()
    type1 = TypeSerie(id="1", title="Manga", to_display=True)
    type2 = TypeSerie(id="2", title="Manhwa", to_display=False)

    repo.add(type1)
    repo.add(type2)
    repo.clear()

    result = repo.get_all_types_v1()
    assert len(result.types) == 0
