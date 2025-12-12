"""Tests pour les use cases Serie.

This module contains unit tests for Serie use cases.
"""

import pytest

from mangacollec.application.use_cases import (GetAllSeriesV2UseCase,
                                               GetListSeriesUseCase,
                                               GetSerieByIdV2UseCase)
from mangacollec.domain.entities import Serie, SerieListItem, TypeSerie
from mangacollec.domain.exceptions import SerieNotFoundException
from mangacollec.infrastructure.repositories import InMemorySerieRepository


@pytest.fixture
def repository() -> InMemorySerieRepository:
    """Fixture pour créer un repository en mémoire."""
    return InMemorySerieRepository()


@pytest.fixture
def sample_series(repository: InMemorySerieRepository) -> list[Serie]:
    """Fixture pour créer des séries de test."""
    series = [
        Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
            type_id="type-1",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1"],
        ),
        Serie(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            title="One Piece",
            type_id="type-1",
            adult_content=False,
            editions_count=25,
            tasks_count=3,
            kinds_ids=None,
        ),
        Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Adult Serie",
            type_id="type-2",
            adult_content=True,
            editions_count=5,
            tasks_count=2,
            kinds_ids=["kind-2", "kind-3"],
        ),
    ]

    for serie in series:
        repository.add(serie)

    return series


@pytest.fixture
def sample_types(repository: InMemorySerieRepository) -> list[TypeSerie]:
    """Fixture pour créer des types de test."""
    types = [
        TypeSerie(id="type-1", title="Manga", to_display=True),
        TypeSerie(id="type-2", title="Seinen", to_display=True),
    ]

    for type_serie in types:
        repository.add_type(type_serie)

    return types


class TestGetSerieByIdV2UseCase:
    """Tests pour GetSerieByIdV2UseCase."""

    def test_get_existing_serie(
        self,
        repository: InMemorySerieRepository,
        sample_series: list[Serie],
        sample_types: list[TypeSerie],
    ) -> None:
        """Test de récupération d'une série existante avec toutes ses relations."""
        usecase = GetSerieByIdV2UseCase(repository)

        (
            serie,
            types,
            kinds,
            tasks,
            jobs,
            authors,
            editions,
            publishers,
            volumes,
            box_editions,
            boxes,
            box_volumes,
        ) = usecase("39c0f48b-c9f3-488d-9f01-bb9f21f30b0e")

        assert isinstance(serie, Serie)
        assert serie.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert serie.title == "Naruto"
        assert serie.kinds_ids == ["kind-1"]
        # Vérifier que les listes sont vides (InMemory repository)
        assert types == []
        assert kinds == []
        assert tasks == []
        assert jobs == []
        assert authors == []
        assert editions == []
        assert publishers == []
        assert volumes == []
        assert box_editions == []
        assert boxes == []
        assert box_volumes == []

    def test_get_nonexistent_serie(self, repository: InMemorySerieRepository) -> None:
        """Test de récupération d'une série inexistante."""
        usecase = GetSerieByIdV2UseCase(repository)

        with pytest.raises(SerieNotFoundException) as exc_info:
            usecase("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_serie_with_empty_id(self, repository: InMemorySerieRepository) -> None:
        """Test de récupération d'une série avec un ID vide."""
        usecase = GetSerieByIdV2UseCase(repository)

        with pytest.raises(SerieNotFoundException) as exc_info:
            usecase("")

        assert "" in str(exc_info.value)

    def test_get_serie_with_none_id(self, repository: InMemorySerieRepository) -> None:
        """Test de récupération d'une série avec un ID None."""
        usecase = GetSerieByIdV2UseCase(repository)

        with pytest.raises(SerieNotFoundException):
            usecase(None)  # type: ignore[arg-type]


class TestGetAllSeriesV2UseCase:
    """Tests pour GetAllSeriesV2UseCase."""

    def test_get_all_series(
        self,
        repository: InMemorySerieRepository,
        sample_series: list[Serie],
        sample_types: list[TypeSerie],
    ) -> None:
        """Test de récupération de toutes les séries avec leurs types."""
        usecase = GetAllSeriesV2UseCase(repository)

        series, types = usecase()

        assert len(series) == 3
        assert all(isinstance(serie, Serie) for serie in series)
        assert len(types) == 2
        assert all(isinstance(type_serie, TypeSerie) for type_serie in types)

    def test_get_all_series_empty(self, repository: InMemorySerieRepository) -> None:
        """Test de récupération avec repository vide."""
        usecase = GetAllSeriesV2UseCase(repository)

        series, types = usecase()

        assert series == []
        assert types == []


class TestGetListSeriesUseCase:
    """Tests pour GetListSeriesUseCase."""

    def test_get_list_series(
        self,
        repository: InMemorySerieRepository,
        sample_series: list[Serie],
        sample_types: list[TypeSerie],
    ) -> None:
        """Test de récupération de la liste simplifiée des séries."""
        usecase = GetListSeriesUseCase(repository)

        result = usecase()

        assert len(result) == 3
        assert all(isinstance(item, SerieListItem) for item in result)
        assert result[0].id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert result[0].title == "Naruto"

    def test_get_list_series_empty(self, repository: InMemorySerieRepository) -> None:
        """Test de récupération avec repository vide."""
        usecase = GetListSeriesUseCase(repository)

        result = usecase()

        assert result == []
