"""Tests pour les DTOs de réponse Volume.

This module contains unit tests for Volume response DTOs.
"""

import pytest

from mangacollec.application.dto import (GetVolumeByIdV2Response,
                                         GetVolumesNewsV2Response)
from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         NativeAdVolumeHomeFirst, Publisher,
                                         Serie, TypeSerie, Volume)


class TestGetVolumeByIdV2Response:
    """Tests pour GetVolumeByIdV2Response."""

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="volume-123",
            title="Tome 1",
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
            editions_count=50,
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
            editions_count=3,
            tasks_count=5,
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

    def test_create_response_with_all_entities(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box_volume: BoxVolume,
        sample_box: Box,
        sample_box_edition: BoxEdition,
    ) -> None:
        """Test de création avec toutes les entités."""
        response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[sample_box_volume],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
        )

        assert len(response.volumes) == 1
        assert response.volumes[0] == sample_volume

        assert len(response.editions) == 1
        assert response.editions[0] == sample_edition

        assert len(response.publishers) == 1
        assert response.publishers[0] == sample_publisher

        assert len(response.series) == 1
        assert response.series[0] == sample_serie

        assert len(response.types) == 1
        assert response.types[0] == sample_type

        assert len(response.box_volumes) == 1
        assert response.box_volumes[0] == sample_box_volume

        assert len(response.boxes) == 1
        assert response.boxes[0] == sample_box

        assert len(response.box_editions) == 1
        assert response.box_editions[0] == sample_box_edition

    def test_create_response_with_empty_lists(self) -> None:
        """Test de création avec listes vides."""
        response = GetVolumeByIdV2Response(
            volumes=[],
            editions=[],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        assert response.volumes == []
        assert response.editions == []
        assert response.publishers == []
        assert response.series == []
        assert response.types == []
        assert response.box_volumes == []
        assert response.boxes == []
        assert response.box_editions == []

    def test_create_response_with_multiple_volumes(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de création avec plusieurs volumes."""
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

        response = GetVolumeByIdV2Response(
            volumes=[sample_volume, volume2],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        assert len(response.volumes) == 2
        assert response.volumes[0].id == "volume-123"
        assert response.volumes[1].id == "volume-124"
        assert response.volumes[0].number == 1
        assert response.volumes[1].number == 2

    def test_response_is_frozen(self, sample_volume: Volume) -> None:
        """Test que le DTO est immuable (frozen)."""
        response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        with pytest.raises(AttributeError):
            response.volumes = []  # type: ignore

        with pytest.raises(AttributeError):
            response.editions = []  # type: ignore

    def test_response_equality(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test d'égalité entre deux réponses identiques."""
        response1 = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        response2 = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        assert response1 == response2

    def test_response_is_frozen_dataclass(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test que la réponse est une dataclass frozen."""
        response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        # Le dataclass est frozen
        assert hasattr(response, "__dataclass_fields__")

        # On ne peut pas modifier les attributs d'un dataclass frozen
        with pytest.raises(AttributeError):
            response.volumes = []  # type: ignore

    def test_response_with_only_volume(self, sample_volume: Volume) -> None:
        """Test de création avec seulement un volume."""
        response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        assert len(response.volumes) == 1
        assert len(response.editions) == 0
        assert len(response.publishers) == 0
        assert len(response.series) == 0
        assert len(response.types) == 0
        assert len(response.box_volumes) == 0
        assert len(response.boxes) == 0
        assert len(response.box_editions) == 0


class TestGetVolumesNewsV2Response:
    """Tests pour GetVolumesNewsV2Response."""

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="volume-123",
            title="Nouveauté Tome 1",
            number=1,
            release_date="2023-12-01",
            isbn="9782012345678",
            asin=None,
            edition_id="edition-456",
            possessions_count=50,
            not_sold=False,
            image_url="https://example.com/new.jpg",
            nb_pages=192,
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

    def test_create_news_response_with_all_entities(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box_volume: BoxVolume,
        sample_box: Box,
        sample_box_edition: BoxEdition,
        sample_native_ad: NativeAdVolumeHomeFirst,
    ) -> None:
        """Test de création avec toutes les entités et la publicité."""
        response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[sample_box_volume],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
            native_ad_volume_home_first=sample_native_ad,
        )

        assert len(response.volumes) == 1
        assert response.volumes[0] == sample_volume

        assert len(response.editions) == 1
        assert response.editions[0] == sample_edition

        assert len(response.series) == 1
        assert response.series[0] == sample_serie

        assert len(response.types) == 1
        assert response.types[0] == sample_type

        assert len(response.box_volumes) == 1
        assert response.box_volumes[0] == sample_box_volume

        assert len(response.boxes) == 1
        assert response.boxes[0] == sample_box

        assert len(response.box_editions) == 1
        assert response.box_editions[0] == sample_box_edition

        assert response.native_ad_volume_home_first is not None
        assert response.native_ad_volume_home_first == sample_native_ad

    def test_create_news_response_without_native_ad(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de création sans publicité native."""
        response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        assert len(response.volumes) == 1
        assert len(response.editions) == 1
        assert response.native_ad_volume_home_first is None

    def test_create_news_response_with_empty_lists(self) -> None:
        """Test de création avec listes vides et sans publicité."""
        response = GetVolumesNewsV2Response(
            volumes=[],
            editions=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        assert response.volumes == []
        assert response.editions == []
        assert response.series == []
        assert response.types == []
        assert response.box_volumes == []
        assert response.boxes == []
        assert response.box_editions == []
        assert response.native_ad_volume_home_first is None

    def test_create_news_response_with_multiple_new_volumes(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test de création avec plusieurs nouveautés."""
        volume2 = Volume(
            id="volume-124",
            title="Nouveauté Tome 2",
            number=2,
            release_date="2023-12-15",
            isbn="9782012345679",
            asin=None,
            edition_id="edition-456",
            possessions_count=30,
            not_sold=False,
            image_url="https://example.com/new2.jpg",
            nb_pages=200,
            content=None,
        )

        response = GetVolumesNewsV2Response(
            volumes=[sample_volume, volume2],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        assert len(response.volumes) == 2
        assert response.volumes[0].title == "Nouveauté Tome 1"
        assert response.volumes[1].title == "Nouveauté Tome 2"

    def test_news_response_is_frozen(self, sample_volume: Volume) -> None:
        """Test que le DTO news est immuable (frozen)."""
        response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        with pytest.raises(AttributeError):
            response.volumes = []  # type: ignore

        with pytest.raises(AttributeError):
            response.native_ad_volume_home_first = None  # type: ignore

    def test_news_response_equality(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test d'égalité entre deux réponses news identiques."""
        response1 = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        response2 = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        assert response1 == response2

    def test_news_response_inequality_due_to_ad(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_native_ad: NativeAdVolumeHomeFirst,
    ) -> None:
        """Test d'inégalité due à la publicité native."""
        response1 = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        response2 = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=sample_native_ad,
        )

        assert response1 != response2

    def test_news_response_is_frozen_dataclass(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test que la réponse news est une dataclass frozen."""
        response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        # Le dataclass est frozen
        assert hasattr(response, "__dataclass_fields__")

        # On ne peut pas modifier les attributs d'un dataclass frozen
        with pytest.raises(AttributeError):
            response.volumes = []  # type: ignore
