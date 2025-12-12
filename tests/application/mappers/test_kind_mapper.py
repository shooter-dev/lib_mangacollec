"""Tests pour le KindMapper."""

import pytest

from mangacollec.application.dto import GetAllKindsV1Response, GetAllKindsV2Response
from mangacollec.application.mappers import KindMapper
from mangacollec.domain.entities import Kind


class TestKindMapper:
    """Tests pour le KindMapper."""

    @pytest.fixture
    def kind_data(self) -> dict:
        """Fixture pour les données d'un kind."""
        return {
            "id": "1",
            "name": "Manga",
            "name_en": "Manga",
        }

    @pytest.fixture
    def kind_entity(self) -> Kind:
        """Fixture pour une entité Kind."""
        return Kind(
            id="1",
            name="Manga",
            name_en="Manga",
        )

    def test_from_dict(self, kind_data: dict) -> None:
        """Test la conversion d'un dictionnaire en entité Kind."""
        kind = KindMapper.from_dict(kind_data)

        assert isinstance(kind, Kind)
        assert kind.id == "1"
        assert kind.name == "Manga"
        assert kind.name_en == "Manga"

    def test_to_dict(self, kind_entity: Kind) -> None:
        """Test la conversion d'une entité Kind en dictionnaire."""
        result = KindMapper.to_dict(kind_entity)

        assert isinstance(result, dict)
        assert result["id"] == "1"
        assert result["name"] == "Manga"
        assert result["name_en"] == "Manga"

    def test_from_all_kinds_v2_response(self, kind_data: dict) -> None:
        """Test la conversion de la réponse API V2 en GetAllKindsV2Response."""
        response = {
            "kinds": [kind_data, kind_data],
        }

        result = KindMapper.from_all_kinds_v2_response(response)

        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 2
        assert all(isinstance(kind, Kind) for kind in result.kinds)
        assert result.kinds[0].id == "1"

    def test_from_all_kinds_v2_response_empty(self) -> None:
        """Test la conversion d'une réponse API V2 vide."""
        response: dict = {"kinds": []}

        result = KindMapper.from_all_kinds_v2_response(response)

        assert isinstance(result, GetAllKindsV2Response)
        assert len(result.kinds) == 0

    def test_from_all_kinds_v1_response(self, kind_data: dict) -> None:
        """Test la conversion de la réponse API V1 en GetAllKindsV1Response."""
        response = {
            "kinds": [kind_data, kind_data],
        }

        result = KindMapper.from_all_kinds_v1_response(response)

        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 2
        assert all(isinstance(kind, Kind) for kind in result.kinds)
        assert result.kinds[0].id == "1"

    def test_from_all_kinds_v1_response_empty(self) -> None:
        """Test la conversion d'une réponse API V1 vide."""
        response: dict = {"kinds": []}

        result = KindMapper.from_all_kinds_v1_response(response)

        assert isinstance(result, GetAllKindsV1Response)
        assert len(result.kinds) == 0

    def test_bidirectional_conversion(self, kind_data: dict) -> None:
        """Test la conversion bidirectionnelle dict -> entity -> dict."""
        kind = KindMapper.from_dict(kind_data)
        result = KindMapper.to_dict(kind)

        assert result == kind_data
