"""Tests pour les DTOs de réponse Kind."""

import pytest

from mangacollec.application.dto import (GetAllKindsV1Response,
                                         GetAllKindsV2Response)
from mangacollec.domain.entities import Kind


class TestGetAllKindsV1Response:
    """Tests pour GetAllKindsV1Response."""

    @pytest.fixture
    def sample_kinds(self):
        """Fixture pour des kinds de test."""
        return [
            Kind(id="1", name="Manga", name_en="Manga"),
            Kind(id="2", name="Comics", name_en="Comics"),
        ]

    def test_creation(self, sample_kinds):
        """Test la création d'un GetAllKindsV1Response."""
        response = GetAllKindsV1Response(kinds=sample_kinds)

        assert isinstance(response, GetAllKindsV1Response)
        assert response.kinds == sample_kinds
        assert len(response.kinds) == 2

    def test_immutability(self, sample_kinds):
        """Test que GetAllKindsV1Response est immuable."""
        response = GetAllKindsV1Response(kinds=sample_kinds)

        with pytest.raises(AttributeError):
            response.kinds = []  # type: ignore[misc]

    def test_empty_kinds_list(self):
        """Test avec une liste vide."""
        response = GetAllKindsV1Response(kinds=[])

        assert isinstance(response, GetAllKindsV1Response)
        assert len(response.kinds) == 0


class TestGetAllKindsV2Response:
    """Tests pour GetAllKindsV2Response."""

    @pytest.fixture
    def sample_kinds(self):
        """Fixture pour des kinds de test."""
        return [
            Kind(id="1", name="Manga", name_en="Manga"),
            Kind(id="2", name="Comics", name_en="Comics"),
        ]

    def test_creation(self, sample_kinds):
        """Test la création d'un GetAllKindsV2Response."""
        response = GetAllKindsV2Response(kinds=sample_kinds)

        assert isinstance(response, GetAllKindsV2Response)
        assert response.kinds == sample_kinds
        assert len(response.kinds) == 2

    def test_immutability(self, sample_kinds):
        """Test que GetAllKindsV2Response est immuable."""
        response = GetAllKindsV2Response(kinds=sample_kinds)

        with pytest.raises(AttributeError):
            response.kinds = []  # type: ignore[misc]

    def test_empty_kinds_list(self):
        """Test avec une liste vide."""
        response = GetAllKindsV2Response(kinds=[])

        assert isinstance(response, GetAllKindsV2Response)
        assert len(response.kinds) == 0
