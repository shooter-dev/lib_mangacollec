"""Tests d'intégration pour les use cases Kind."""

import pytest

from mangacollec.application.dto import (GetAllKindsV1Response,
                                         GetAllKindsV2Response)
from mangacollec.application.use_cases import (GetAllKindsV1UseCase,
                                               GetAllKindsV2UseCase)
from mangacollec.domain.entities import Kind
from mangacollec.infrastructure.repositories.memory.in_memory_kind_repository import \
    InMemoryKindRepository


class TestGetAllKindsV1UseCase:
    """Tests pour GetAllKindsV1UseCase."""

    @pytest.fixture
    def repo(self):
        """Fixture pour le repository."""
        return InMemoryKindRepository()

    @pytest.fixture
    def use_case(self, repo):
        """Fixture pour le use case."""
        return GetAllKindsV1UseCase(repo)

    @pytest.fixture
    def sample_kinds(self):
        """Fixture pour des kinds de test."""
        return [
            Kind(id="1", name="Manga", name_en="Manga"),
            Kind(id="2", name="Comics", name_en="Comics"),
            Kind(id="3", name="BD", name_en="Comic Book"),
        ]

    def test_get_all_kinds_v1_empty(self, use_case):
        """Test get_all_kinds_v1 avec un repository vide."""
        result = use_case()

        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 0

    def test_get_all_kinds_v1_with_data(self, use_case, repo, sample_kinds):
        """Test get_all_kinds_v1 avec des données."""
        for kind in sample_kinds:
            repo.add(kind)

        result = use_case()

        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 3
        assert all(isinstance(kind, Kind) for kind in result.kinds)

    def test_get_all_kinds_v1_returns_all_kinds(self, use_case, repo, sample_kinds):
        """Test que get_all_kinds_v1 retourne tous les kinds."""
        for kind in sample_kinds:
            repo.add(kind)

        result = use_case()

        kind_ids = [kind.id for kind in result.kinds]
        assert "1" in kind_ids
        assert "2" in kind_ids
        assert "3" in kind_ids


class TestGetAllKindsV2UseCase:
    """Tests pour GetAllKindsV2UseCase."""

    @pytest.fixture
    def repo(self):
        """Fixture pour le repository."""
        return InMemoryKindRepository()

    @pytest.fixture
    def use_case(self, repo):
        """Fixture pour le use case."""
        return GetAllKindsV2UseCase(repo)

    @pytest.fixture
    def sample_kinds(self):
        """Fixture pour des kinds de test."""
        return [
            Kind(id="1", name="Manga", name_en="Manga"),
            Kind(id="2", name="Comics", name_en="Comics"),
            Kind(id="3", name="BD", name_en="Comic Book"),
        ]

    def test_get_all_kinds_v2_empty(self, use_case):
        """Test get_all_kinds_v2 avec un repository vide."""
        result = use_case()

        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 0

    def test_get_all_kinds_v2_with_data(self, use_case, repo, sample_kinds):
        """Test get_all_kinds_v2 avec des données."""
        for kind in sample_kinds:
            repo.add(kind)

        result = use_case()

        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 3
        assert all(isinstance(kind, Kind) for kind in result.kinds)

    def test_get_all_kinds_v2_returns_all_kinds(self, use_case, repo, sample_kinds):
        """Test que get_all_kinds_v2 retourne tous les kinds."""
        for kind in sample_kinds:
            repo.add(kind)

        result = use_case()

        kind_ids = [kind.id for kind in result.kinds]
        assert "1" in kind_ids
        assert "2" in kind_ids
        assert "3" in kind_ids

    def test_v1_and_v2_use_cases_return_same_data(self, repo, sample_kinds):
        """Test que V1 et V2 retournent les mêmes données."""
        for kind in sample_kinds:
            repo.add(kind)

        use_case_v1 = GetAllKindsV1UseCase(repo)
        use_case_v2 = GetAllKindsV2UseCase(repo)

        result_v1 = use_case_v1()
        result_v2 = use_case_v2()

        assert result_v1.kinds == result_v2.kinds
