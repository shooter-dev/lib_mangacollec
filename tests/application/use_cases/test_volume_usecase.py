"""Tests pour les use cases Volume.

This module contains unit tests for Volume use cases.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
)
from mangacollec.application.use_cases import (
    GetVolumeByIdV2UseCase,
    GetVolumesNewsV2UseCase,
)
from mangacollec.domain.entities import (
    Box,
    BoxEdition,
    BoxVolume,
    Edition,
    NativeAdVolumeHomeFirst,
    Publisher,
    Serie,
    TypeSerie,
    Volume,
)
from mangacollec.domain.exceptions import VolumeNotFoundException
from mangacollec.domain.repositories import IVolumeRepository


class TestGetVolumeByIdV2UseCase:
    """Tests pour GetVolumeByIdV2UseCase."""

    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Fixture pour créer un mock du repository."""
        return Mock(spec=IVolumeRepository)

    @pytest.fixture
    def use_case(self, mock_repository: Mock) -> GetVolumeByIdV2UseCase:
        """Fixture pour créer le use case avec un mock repository."""
        return GetVolumeByIdV2UseCase(mock_repository)

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="volume-123",
            title="Tome 1 : Le Début",
            number=1,
            release_date="2023-01-15",
            isbn="9782012345678",
            asin="2012345678",
            edition_id="edition-456",
            possessions_count=150,
            not_sold=False,
            image_url="https://example.com/image.jpg",
            nb_pages=192,
            content="Chapitres 1-3",
        )

    @pytest.fixture
    def sample_edition(self) -> Edition:
        """Fixture pour créer une édition de test."""
        return Edition(
            id="edition-456",
            title="Edition Collector",
            series_id="series-789",
            publisher_id="publisher-001",
            parent_edition_id=None,
            volumes_count=12,
            last_volume_number=12,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=300,
        )

    @pytest.fixture
    def sample_publisher(self) -> Publisher:
        """Fixture pour créer un publisher de test."""
        return Publisher(
            id="publisher-001",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

    @pytest.fixture
    def sample_serie(self) -> Serie:
        """Fixture pour créer une série de test."""
        return Serie(
            id="series-789",
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
    def sample_box_volume(self) -> BoxVolume:
        """Fixture pour créer un box volume de test."""
        return BoxVolume(
            id="box-volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=None,
            not_sold=False,
            image_url=None,
        )

    @pytest.fixture
    def sample_box(self) -> Box:
        """Fixture pour créer un box de test."""
        return Box(
            id="box-456",
            title="Intégrale Saison 1",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            commercial_stop=False,
            box_edition_id="box-edition-123",
            box_possessions_count=None,
            image_url=None,
        )

    @pytest.fixture
    def sample_box_edition(self) -> BoxEdition:
        """Fixture pour créer un box edition de test."""
        return BoxEdition(
            id="box-edition-123",
            title=None,
            publisher_id="publisher-001",
            boxes_count=1,
            adult_content=False,
            box_follow_editions_count=10,
        )

    def test_get_volume_by_id_success(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box_volume: BoxVolume,
        sample_box: Box,
        sample_box_edition: BoxEdition,
    ) -> None:
        """Test de récupération réussie d'un volume par ID."""
        # Préparation du mock
        mock_response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[sample_box_volume],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        # Exécution
        result = use_case("volume-123")

        # Vérifications
        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume

        assert len(result.editions) == 1
        assert result.editions[0] == sample_edition

        assert len(result.publishers) == 1
        assert result.publishers[0] == sample_publisher

        assert len(result.series) == 1
        assert result.series[0] == sample_serie

        assert len(result.types) == 1
        assert result.types[0] == sample_type

        assert len(result.box_volumes) == 1
        assert result.box_volumes[0] == sample_box_volume

        assert len(result.boxes) == 1
        assert result.boxes[0] == sample_box

        assert len(result.box_editions) == 1
        assert result.box_editions[0] == sample_box_edition

        mock_repository.get_by_id_v2.assert_called_once_with("volume-123")

    def test_get_volume_by_id_not_found(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
    ) -> None:
        """Test de récupération d'un volume inexistant."""
        mock_repository.get_by_id_v2.side_effect = VolumeNotFoundException("nonexistent-id")

        with pytest.raises(VolumeNotFoundException) as exc_info:
            use_case("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)
        mock_repository.get_by_id_v2.assert_called_once_with("nonexistent-id")

    def test_get_volume_by_id_with_minimal_data(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
    ) -> None:
        """Test de récupération avec données minimales."""
        mock_response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        result = use_case("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume
        assert result.editions == []
        assert result.publishers == []
        assert result.series == []
        assert result.types == []
        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []

    def test_get_volume_by_id_with_multiple_volumes(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération avec plusieurs volumes."""
        volume2 = Volume(
            id="volume-124",
            title="Tome 2",
            number=2,
            release_date="2023-02-15",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=120,
            not_sold=False,
            image_url=None,
            nb_pages=200,
            content=None,
        )

        mock_response = GetVolumeByIdV2Response(
            volumes=[sample_volume, volume2],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        result = use_case("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 2
        assert result.volumes[0].id == "volume-123"
        assert result.volumes[1].id == "volume-124"
        assert result.volumes[0].number == 1
        assert result.volumes[1].number == 2

    def test_get_volume_by_id_without_isbn(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération d'un volume sans ISBN."""
        volume_without_isbn = Volume(
            id="volume-123",
            title="Volume Sans ISBN",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=0,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        mock_response = GetVolumeByIdV2Response(
            volumes=[volume_without_isbn],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        result = use_case("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].isbn is None
        assert result.volumes[0].asin is None

    def test_get_volume_by_id_not_sold(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération d'un volume non vendu."""
        volume_not_sold = Volume(
            id="volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=0,
            not_sold=True,
            image_url=None,
            nb_pages=None,
            content=None,
        )

        mock_response = GetVolumeByIdV2Response(
            volumes=[volume_not_sold],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        result = use_case("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].not_sold is True
        assert result.volumes[0].possessions_count == 0

    def test_get_volume_by_id_repository_called_once(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test que le repository est appelé exactement une fois."""
        mock_response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        use_case("volume-123")

        mock_repository.get_by_id_v2.assert_called_once_with("volume-123")

    def test_use_case_call_syntax(
        self,
        use_case: GetVolumeByIdV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de la syntaxe d'appel du use case avec __call__."""
        mock_response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        mock_repository.get_by_id_v2.return_value = mock_response

        # Test avec __call__ (syntaxe fonctionnelle)
        result = use_case("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume


class TestGetVolumesNewsV2UseCase:
    """Tests pour GetVolumesNewsV2UseCase."""

    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Fixture pour créer un mock du repository."""
        return Mock(spec=IVolumeRepository)

    @pytest.fixture
    def use_case(self, mock_repository: Mock) -> GetVolumesNewsV2UseCase:
        """Fixture pour créer le use case avec un mock repository."""
        return GetVolumesNewsV2UseCase(mock_repository)

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="volume-123",
            title="Nouveauté Tome 1",
            number=1,
            release_date="2023-12-01",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url="https://example.com/new.jpg",
            nb_pages=None,
            content=None,
        )

    @pytest.fixture
    def sample_edition(self) -> Edition:
        """Fixture pour créer une édition de test."""
        return Edition(
            id="edition-456",
            title="Nouvelle Édition",
            series_id="series-789",
            publisher_id=None,
            parent_edition_id=None,
            volumes_count=5,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=100,
        )

    @pytest.fixture
    def sample_serie(self) -> Serie:
        """Fixture pour créer une série de test."""
        return Serie(
            id="series-789",
            title="Nouvelle Série",
            type_id="type-001",
            adult_content=False,
            editions_count=2,
            tasks_count=3,
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
    def sample_native_ad(self) -> NativeAdVolumeHomeFirst:
        """Fixture pour créer une publicité native de test."""
        return NativeAdVolumeHomeFirst(
            id="ad-123",
            volume_id="volume-123",
            title="Publicité Spéciale",
            start_date="2023-12-01",
            end_date="2023-12-31",
        )

    def test_get_volumes_news_success(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_native_ad: NativeAdVolumeHomeFirst,
    ) -> None:
        """Test de récupération réussie des volumes récents."""
        # Préparation du mock
        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=sample_native_ad,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        # Exécution
        result = use_case()

        # Vérifications
        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume

        assert len(result.editions) == 1
        assert result.editions[0] == sample_edition

        assert len(result.series) == 1
        assert result.series[0] == sample_serie

        assert len(result.types) == 1
        assert result.types[0] == sample_type

        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []

        assert result.native_ad_volume_home_first is not None
        assert result.native_ad_volume_home_first == sample_native_ad

        mock_repository.get_volumes_news_v2.assert_called_once()

    def test_get_volumes_news_without_native_ad(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération sans publicité native."""
        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        result = use_case()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert len(result.editions) == 1
        assert result.native_ad_volume_home_first is None

        mock_repository.get_volumes_news_v2.assert_called_once()

    def test_get_volumes_news_empty_response(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
    ) -> None:
        """Test de récupération avec réponse vide."""
        mock_response = GetVolumesNewsV2Response(
            volumes=[],
            editions=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        result = use_case()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert result.volumes == []
        assert result.editions == []
        assert result.series == []
        assert result.types == []
        assert result.box_volumes == []
        assert result.boxes == []
        assert result.box_editions == []
        assert result.native_ad_volume_home_first is None

        mock_repository.get_volumes_news_v2.assert_called_once()

    def test_get_volumes_news_multiple_volumes(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération avec plusieurs nouveautés."""
        volume2 = Volume(
            id="volume-124",
            title="Nouveauté Tome 2",
            number=2,
            release_date="2023-12-15",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=30,
            not_sold=False,
            image_url="https://example.com/new2.jpg",
            nb_pages=None,
            content=None,
        )

        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume, volume2],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        result = use_case()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 2
        assert result.volumes[0].title == "Nouveauté Tome 1"
        assert result.volumes[1].title == "Nouveauté Tome 2"

    def test_get_volumes_news_runtime_error(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
    ) -> None:
        """Test de gestion d'erreur runtime."""
        mock_repository.get_volumes_news_v2.side_effect = RuntimeError("API Error")

        with pytest.raises(RuntimeError) as exc_info:
            use_case()

        assert "API Error" in str(exc_info.value)
        mock_repository.get_volumes_news_v2.assert_called_once()

    def test_get_volumes_news_repository_called_once(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test que le repository est appelé exactement une fois."""
        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        use_case()

        mock_repository.get_volumes_news_v2.assert_called_once()

    def test_get_volumes_news_call_syntax(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de la syntaxe d'appel du use case avec __call__."""
        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        # Test avec __call__ (syntaxe fonctionnelle)
        result = use_case()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume

    def test_get_volumes_news_with_boxes(
        self,
        use_case: GetVolumesNewsV2UseCase,
        mock_repository: Mock,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
    ) -> None:
        """Test de récupération avec coffrets dans les nouveautés."""
        box_volume = BoxVolume(
            id="box-volume-123",
            title=None,
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=None,
            not_sold=False,
            image_url=None,
        )
        box = Box(
            id="box-456",
            title="Box Set Nouveauté",
            number=1,
            release_date=None,
            isbn=None,
            asin=None,
            commercial_stop=False,
            box_edition_id="box-edition-123",
            box_possessions_count=None,
            image_url=None,
        )
        box_edition = BoxEdition(
            id="box-edition-123",
            title=None,
            publisher_id="publisher-001",
            boxes_count=1,
            adult_content=False,
            box_follow_editions_count=10,
        )

        mock_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[box_volume],
            boxes=[box],
            box_editions=[box_edition],
            native_ad_volume_home_first=None,
        )
        mock_repository.get_volumes_news_v2.return_value = mock_response

        result = use_case()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert len(result.editions) == 1
        assert len(result.series) == 1
        assert len(result.types) == 1
        assert len(result.box_volumes) == 1
        assert len(result.boxes) == 1
        assert len(result.box_editions) == 1
        assert result.native_ad_volume_home_first is None
