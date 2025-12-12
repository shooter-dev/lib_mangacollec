"""Tests pour les use cases Edition.

This module contains unit tests for Edition use cases.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import GetEditionByIdV2Response
from mangacollec.application.use_cases import GetEditionByIdV2UseCase
from mangacollec.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume
from mangacollec.domain.exceptions import EditionNotFoundException
from mangacollec.domain.repositories import IEditionRepository


class TestGetEditionByIdV2UseCase:
    """Tests pour GetEditionByIdV2UseCase."""

    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Fixture pour créer un mock du repository."""
        return Mock(spec=IEditionRepository)

    @pytest.fixture
    def use_case(self, mock_repository: Mock) -> GetEditionByIdV2UseCase:
        """Fixture pour créer le use case avec un mock repository."""
        return GetEditionByIdV2UseCase(mock_repository)

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
            nb_pages=None,
            content=None,
        )

    def test_get_edition_by_id_success(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_volume: Volume,
    ) -> None:
        """Test de récupération réussie d'une édition par ID."""
        # Préparation du mock - Le repository retourne un DTO
        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[sample_type],
            volumes=[sample_volume],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        # Exécution - Le use case retourne un tuple
        result = use_case("edition-123")

        # Vérifications - Le résultat doit être un tuple
        assert isinstance(result, tuple)
        assert len(result) == 5

        editions, publishers, series, types, volumes = result
        assert len(editions) == 1
        assert editions[0] == sample_edition
        assert len(publishers) == 1
        assert publishers[0] == sample_publisher
        assert len(series) == 1
        assert series[0] == sample_serie
        assert len(types) == 1
        assert types[0] == sample_type
        assert len(volumes) == 1
        assert volumes[0] == sample_volume

        mock_repository.get_edition_by_id_v2.assert_called_once_with("edition-123")

    def test_get_edition_by_id_not_found(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
    ) -> None:
        """Test de récupération d'une édition inexistante."""
        mock_repository.get_edition_by_id_v2.side_effect = EditionNotFoundException("nonexistent-id")

        with pytest.raises(EditionNotFoundException) as exc_info:
            use_case("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        mock_repository.get_edition_by_id_v2.assert_called_once_with("nonexistent-id")

    def test_get_edition_by_id_with_empty_lists(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération avec listes vides pour series, types et volumes."""
        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        result = use_case("edition-123")

        assert isinstance(result, tuple)
        editions, publishers, series, types, volumes = result
        assert len(editions) == 1
        assert len(publishers) == 1
        assert publishers[0] == sample_publisher
        assert series == []
        assert types == []
        assert volumes == []

    def test_get_edition_by_id_multiple_editions(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération avec plusieurs éditions (parent et enfants)."""
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

        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition, child_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        result = use_case("edition-123")

        assert isinstance(result, tuple)
        editions, publishers, series, types, volumes = result
        assert len(editions) == 2
        assert editions[0].id == "edition-123"
        assert editions[1].id == "edition-child"
        assert editions[1].parent_edition_id == "edition-123"

    def test_get_edition_by_id_multiple_volumes(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération avec plusieurs volumes."""
        volume1 = Volume(
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
            nb_pages=None,
            content=None,
        )
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
            nb_pages=None,
            content=None,
        )

        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[volume1, volume2],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        result = use_case("edition-123")

        assert isinstance(result, tuple)
        editions, publishers, series, types, volumes = result
        assert len(volumes) == 2
        assert volumes[0].number == 1
        assert volumes[1].number == 2

    def test_get_edition_by_id_commercial_stop(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération d'une édition avec arrêt commercial."""
        stopped_edition = Edition(
            id="edition-stopped",
            title="Stopped Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=True,
            not_finished=False,
            follow_editions_count=50,
        )

        mock_response = GetEditionByIdV2Response(
            editions=[stopped_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        result = use_case("edition-stopped")

        assert isinstance(result, tuple)
        editions, publishers, series, types, volumes = result
        assert editions[0].commercial_stop is True
        assert editions[0].not_finished is False

    def test_get_edition_by_id_not_finished(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération d'une édition non terminée."""
        ongoing_edition = Edition(
            id="edition-ongoing",
            title="Ongoing Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=50,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=500,
        )

        mock_response = GetEditionByIdV2Response(
            editions=[ongoing_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        result = use_case("edition-ongoing")

        assert isinstance(result, tuple)
        editions, publishers, series, types, volumes = result
        assert editions[0].not_finished is True
        assert editions[0].commercial_stop is False
        assert editions[0].last_volume_number is None

    def test_get_edition_by_id_repository_called_once(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test que le repository est appelé exactement une fois."""
        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        use_case("edition-123")

        mock_repository.get_edition_by_id_v2.assert_called_once()

    def test_use_case_call_syntax(
        self,
        use_case: GetEditionByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de la syntaxe d'appel du use case avec __call__."""
        mock_response = GetEditionByIdV2Response(
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[],
            types=[],
            volumes=[],
        )
        mock_repository.get_edition_by_id_v2.return_value = mock_response

        # Test avec __call__ (syntaxe fonctionnelle)
        result = use_case("edition-123")

        assert isinstance(result, tuple)
        assert len(result) == 5
        assert result[0] == [sample_edition]
        assert result[1] == [sample_publisher]
        assert result[2] == []
        assert result[3] == []
        assert result[4] == []
