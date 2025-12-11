"""Tests pour InMemoryKindRepository."""

import pytest

from mangacollec.application.dto import (GetAllKindsV1Response,
                                         GetAllKindsV2Response)
from mangacollec.domain.entities import Kind
from mangacollec.infrastructure.repositories.memory.in_memory_kind_repository import \
    InMemoryKindRepository


class TestInMemoryKindRepository:
    """Tests pour InMemoryKindRepository."""

    @pytest.fixture
    def repo(self) -> InMemoryKindRepository:
        """Fixture pour le repository."""
        return InMemoryKindRepository()

    @pytest.fixture
    def sample_kind(self) -> Kind:
        """Fixture pour un kind de test."""
        return Kind(
            id="1",
            name="Manga",
            name_en="Manga",
        )

    def test_get_all_kinds_v1_empty(self, repo: InMemoryKindRepository) -> None:
        """Test get_all_kinds_v1 avec un repository vide."""
        result = repo.get_all_kinds_v1()

        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 0

    def test_get_all_kinds_v2_empty(self, repo: InMemoryKindRepository) -> None:
        """Test get_all_kinds_v2 avec un repository vide."""
        result = repo.get_all_kinds_v2()

        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 0

    def test_add_and_get_all_kinds_v1(self, repo: InMemoryKindRepository, sample_kind: Kind) -> None:
        """Test l'ajout et la récupération via V1."""
        repo.add(sample_kind)
        result = repo.get_all_kinds_v1()

        assert len(result.kinds) == 1
        assert result.kinds[0] == sample_kind

    def test_add_and_get_all_kinds_v2(self, repo: InMemoryKindRepository, sample_kind: Kind) -> None:
        """Test l'ajout et la récupération via V2."""
        repo.add(sample_kind)
        result = repo.get_all_kinds_v2()

        assert len(result.kinds) == 1
        assert result.kinds[0] == sample_kind

    def test_add_multiple_kinds(self, repo: InMemoryKindRepository) -> None:
        """Test l'ajout de plusieurs kinds."""
        kind1 = Kind(id="1", name="Manga", name_en="Manga")
        kind2 = Kind(id="2", name="Comics", name_en="Comics")

        repo.add(kind1)
        repo.add(kind2)
        result = repo.get_all_kinds_v2()

        assert len(result.kinds) == 2

    def test_clear(self, repo: InMemoryKindRepository, sample_kind: Kind) -> None:
        """Test la suppression de tous les kinds."""
        repo.add(sample_kind)
        repo.clear()
        result = repo.get_all_kinds_v2()

        assert len(result.kinds) == 0

    def test_v1_and_v2_return_same_data(self, repo: InMemoryKindRepository, sample_kind: Kind) -> None:
        """Test que V1 et V2 retournent les mêmes données."""
        repo.add(sample_kind)
        result_v1 = repo.get_all_kinds_v1()
        result_v2 = repo.get_all_kinds_v2()

        assert result_v1.kinds == result_v2.kinds
