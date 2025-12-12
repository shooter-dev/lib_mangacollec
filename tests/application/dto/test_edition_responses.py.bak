"""Tests pour les DTOs de réponse Edition.

This module contains unit tests for Edition response DTOs.
"""

import pytest

from mangacollec.application.dto import GetEditionByIdV2Response
from mangacollec.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume


class TestGetEditionByIdV2Response:
    """Tests pour GetEditionByIdV2Response."""

    @pytest.fixture
    def sample_edition(self) -> Edition:
        """Fixture pour créer une édition de test."""
        return Edition(
            id="edition-123",
            title="Edition Collector",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=72,
            last_volume_number=72,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=1443,
        )

    @pytest.fixture
    def sample_publisher(self) -> Publisher:
        """Fixture pour créer un publisher de test."""
        return Publisher(
            id="publisher-789",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

    @pytest.fixture
    def sample_serie(self) -> Serie:
        """Fixture pour créer une série de test."""
        return Serie(
            id="series-456",
            title="Naruto",
            type_id="type-001",
            adult_content=False,
            editions_count=7,
            tasks_count=1,
        )

    @pytest.fixture
    def sample_type(self) -> TypeSerie:
        """Fixture pour créer un type de test."""
        return TypeSerie(
            id="type-001",
            title="Manga",
            to_display=True,
        )

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="volume-001",
            title=None,
            number=1,
            release_date="2002-03-01",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-123",
            possessions_count=100,
            not_sold=False,
            image_url="https://example.com/image.jpg",
        )

    def test_response_creation_with_all_entities(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_volume: Volume,
    ) -> None:
        """Test de création d'une réponse avec toutes les entités."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[sample_type],
            volumes=[sample_volume],
        )

        assert len(response.editions) == 1
        assert response.editions[0] == sample_edition
        assert len(response.publishers) == 1
        assert response.publishers[0] == sample_publisher
        assert len(response.series) == 1
        assert response.series[0] == sample_serie
        assert len(response.types) == 1
        assert response.types[0] == sample_type
        assert len(response.volumes) == 1
        assert response.volumes[0] == sample_volume

    def test_response_creation_with_empty_lists(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de création d'une réponse avec listes vides."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        assert len(response.editions) == 1
        assert len(response.publishers) == 1
        assert response.series == []
        assert response.types == []
        assert response.volumes == []

    def test_response_creation_with_multiple_editions(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de création d'une réponse avec plusieurs éditions."""
        child_edition = Edition(
            id="edition-child",
            title="Edition Deluxe",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id="edition-123",
            volumes_count=50,
            last_volume_number=50,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=500,
        )

        response = GetEditionByIdV2Response(
            editions=[sample_edition, child_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        assert len(response.editions) == 2
        assert response.editions[0].id == "edition-123"
        assert response.editions[1].id == "edition-child"
        assert response.editions[1].parent_edition_id == "edition-123"

    def test_response_creation_with_multiple_volumes(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_volume: Volume,
    ) -> None:
        """Test de création d'une réponse avec plusieurs volumes."""
        volume2 = Volume(
            id="volume-002",
            title=None,
            number=2,
            release_date="2002-04-01",
            isbn="9782012345679",
            asin="2012345679",
            edition_id="edition-123",
            possessions_count=90,
            not_sold=False,
            image_url="https://example.com/image2.jpg",
        )

        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[sample_volume, volume2],
        )

        assert len(response.volumes) == 2
        assert response.volumes[0].number == 1
        assert response.volumes[1].number == 2

    def test_response_is_frozen(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test que le DTO de réponse est immuable (frozen)."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        with pytest.raises(AttributeError):
            response.editions = []  # type: ignore

    def test_response_editions_is_list(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test que editions est bien une liste."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        assert isinstance(response.editions, list)
        assert all(isinstance(e, Edition) for e in response.editions)

    def test_response_publishers_is_list(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test que publishers est bien une liste."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        assert isinstance(response.publishers, list)
        assert all(isinstance(p, Publisher) for p in response.publishers)

    def test_response_series_is_list(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
    ) -> None:
        """Test que series est bien une liste."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[],
            volumes=[],
        )

        assert isinstance(response.series, list)
        assert all(isinstance(s, Serie) for s in response.series)

    def test_response_types_is_list(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_type: TypeSerie,
    ) -> None:
        """Test que types est bien une liste."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[sample_type],
            volumes=[],
        )

        assert isinstance(response.types, list)
        assert all(isinstance(t, TypeSerie) for t in response.types)

    def test_response_volumes_is_list(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_volume: Volume,
    ) -> None:
        """Test que volumes est bien une liste."""
        response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[sample_volume],
        )

        assert isinstance(response.volumes, list)
        assert all(isinstance(v, Volume) for v in response.volumes)

    def test_response_equality(
        self,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test d'égalité entre deux réponses identiques."""
        response1 = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        response2 = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )

        assert response1 == response2
