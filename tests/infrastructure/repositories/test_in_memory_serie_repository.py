"""Tests pour InMemorySerieRepository."""

import pytest

from mangacollec.application.dto import (GetAllSeriesV2Response,
                                         GetSerieByIdV2Response)
from mangacollec.domain.entities import Serie, TypeSerie
from mangacollec.domain.exceptions import SerieNotFoundException
from mangacollec.infrastructure.repositories import InMemorySerieRepository


class TestInMemorySerieRepository:
    """Tests pour InMemorySerieRepository."""

    @pytest.fixture
    def repo(self) -> InMemorySerieRepository:
        """Fixture pour le repository."""
        return InMemorySerieRepository()

    @pytest.fixture
    def sample_serie(self) -> Serie:
        """Fixture pour une série de test."""
        return Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
            type_id="type-1",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1"],
        )

    @pytest.fixture
    def sample_type(self) -> TypeSerie:
        """Fixture pour un type de test."""
        return TypeSerie(id="type-1", title="Manga", to_display=True)

    def test_get_all_series_v2_empty(self, repo: InMemorySerieRepository) -> None:
        """Test get_all_series_v2 avec un repository vide."""
        result = repo.get_all_series_v2()

        assert isinstance(result, GetAllSeriesV2Response)
        assert len(result.series) == 0
        assert len(result.types) == 0

    def test_add_and_get_all_series_v2(self, repo: InMemorySerieRepository, sample_serie: Serie) -> None:
        """Test l'ajout et la récupération."""
        repo.add(sample_serie)
        result = repo.get_all_series_v2()

        assert len(result.series) == 1
        assert result.series[0] == sample_serie

    def test_add_and_get_all_series_v2_with_types(
        self,
        repo: InMemorySerieRepository,
        sample_serie: Serie,
        sample_type: TypeSerie,
    ) -> None:
        """Test l'ajout et la récupération avec types."""
        repo.add(sample_serie)
        repo.add_type(sample_type)
        result = repo.get_all_series_v2()

        assert len(result.series) == 1
        assert result.series[0] == sample_serie
        assert len(result.types) == 1
        assert result.types[0] == sample_type

    def test_add_multiple_series(self, repo: InMemorySerieRepository) -> None:
        """Test l'ajout de plusieurs séries."""
        serie1 = Serie(
            id="1",
            title="Naruto",
            type_id="type-1",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1"],
        )
        serie2 = Serie(
            id="2",
            title="One Piece",
            type_id="type-1",
            adult_content=False,
            editions_count=25,
            tasks_count=3,
            kinds_ids=None,
        )

        repo.add(serie1)
        repo.add(serie2)
        result = repo.get_all_series_v2()

        assert len(result.series) == 2

    def test_get_serie_by_id_v2(self, repo: InMemorySerieRepository, sample_serie: Serie) -> None:
        """Test la récupération d'une série par ID."""
        repo.add(sample_serie)
        result = repo.get_serie_by_id_v2("39c0f48b-c9f3-488d-9f01-bb9f21f30b0e")

        assert isinstance(result, GetSerieByIdV2Response)
        assert len(result.series) == 1
        assert result.series[0] == sample_serie
        # Vérifier que les relations sont vides (InMemory)
        assert result.types == []
        assert result.kinds == []
        assert result.tasks == []
        assert result.jobs == []
        assert result.authors == []
        assert result.editions == []
        assert result.publishers == []
        assert result.volumes == []
        assert result.box_editions == []
        assert result.boxes == []
        assert result.box_volumes == []

    def test_get_serie_by_id_v2_not_found(self, repo: InMemorySerieRepository) -> None:
        """Test la récupération d'une série inexistante."""
        with pytest.raises(SerieNotFoundException) as exc_info:
            repo.get_serie_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_clear(
        self,
        repo: InMemorySerieRepository,
        sample_serie: Serie,
        sample_type: TypeSerie,
    ) -> None:
        """Test la suppression de toutes les séries et types."""
        repo.add(sample_serie)
        repo.add_type(sample_type)
        repo.clear()
        result = repo.get_all_series_v2()

        assert len(result.series) == 0
        assert len(result.types) == 0

    def test_add_duplicate_serie(self, repo: InMemorySerieRepository, sample_serie: Serie) -> None:
        """Test l'ajout d'une série en double (devrait écraser l'existante)."""
        repo.add(sample_serie)

        # Modifier la série et l'ajouter à nouveau avec le même ID
        duplicate_serie = Serie(
            id=sample_serie.id,
            title="Modified Title",
            type_id=sample_serie.type_id,
            adult_content=True,
            editions_count=99,
            tasks_count=99,
            kinds_ids=["modified"],
        )
        repo.add(duplicate_serie)

        result = repo.get_all_series_v2()
        assert len(result.series) == 1
        assert result.series[0].title == "Modified Title"
        assert result.series[0].adult_content is True

    def test_add_duplicate_type(self, repo: InMemorySerieRepository, sample_type: TypeSerie) -> None:
        """Test l'ajout d'un type en double (devrait écraser l'existant)."""
        repo.add_type(sample_type)

        # Modifier le type et l'ajouter à nouveau avec le même ID
        duplicate_type = TypeSerie(
            id=sample_type.id,
            title="Modified Type",
            to_display=False,
        )
        repo.add_type(duplicate_type)

        result = repo.get_all_series_v2()
        assert len(result.types) == 1
        assert result.types[0].title == "Modified Type"
        assert result.types[0].to_display is False
