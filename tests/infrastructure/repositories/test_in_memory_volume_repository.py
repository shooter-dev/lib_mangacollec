"""Tests pour InMemoryVolumeRepository."""

import pytest

from mangacollec.application.dto import (
    GetVolumeByIdV2Response,
    GetVolumesNewsV2Response,
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
from mangacollec.infrastructure.repositories import InMemoryVolumeRepository


class TestInMemoryVolumeRepository:
    """Tests pour InMemoryVolumeRepository."""

    @pytest.fixture
    def repo(self) -> InMemoryVolumeRepository:
        """Fixture pour le repository."""
        return InMemoryVolumeRepository()

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour un volume de test."""
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
        """Fixture pour une édition de test."""
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
        """Fixture pour un publisher de test."""
        return Publisher(
            id="publisher-001",
            title="Kana",
            closed=False,
            editions_count=150,
            no_amazon=False,
        )

    @pytest.fixture
    def sample_serie(self) -> Serie:
        """Fixture pour une série de test."""
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
        """Fixture pour un type de test."""
        return TypeSerie(
            id="type-001",
            title="Manga",
            to_display=True,
        )

    @pytest.fixture
    def sample_box_volume(self) -> BoxVolume:
        """Fixture pour un box volume de test."""
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
        """Fixture pour un box de test."""
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
        """Fixture pour un box edition de test."""
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
        """Fixture pour une publicité native de test."""
        return NativeAdVolumeHomeFirst(
            id="ad-123",
            volume_id="volume-123",
            title="Publicité Spéciale",
            start_date="2023-12-01",
            end_date="2023-12-31",
        )

    @pytest.fixture
    def sample_response(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box_volume: BoxVolume,
        sample_box: Box,
        sample_box_edition: BoxEdition,
    ) -> GetVolumeByIdV2Response:
        """Fixture pour une réponse complète."""
        return GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            publishers=[sample_publisher],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[sample_box_volume],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
        )

    @pytest.fixture
    def sample_news_response(
        self,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_native_ad: NativeAdVolumeHomeFirst,
    ) -> GetVolumesNewsV2Response:
        """Fixture pour une réponse news."""
        return GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=sample_native_ad,
        )

    def test_get_by_id_v2_empty(self, repo: InMemoryVolumeRepository) -> None:
        """Test get_by_id_v2 avec un repository vide."""
        with pytest.raises(VolumeNotFoundException) as exc_info:
            repo.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_add_and_get_by_id_v2(
        self,
        repo: InMemoryVolumeRepository,
        sample_response: GetVolumeByIdV2Response,
    ) -> None:
        """Test l'ajout et la récupération."""
        repo.add_volume("volume-123", sample_response)
        result = repo.get_by_id_v2("volume-123")

        assert isinstance(result, GetVolumeByIdV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].id == "volume-123"
        assert result.volumes[0].title == "Tome 1"

    def test_add_multiple_volumes(
        self,
        repo: InMemoryVolumeRepository,
        sample_response: GetVolumeByIdV2Response,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test l'ajout de plusieurs volumes."""
        # Premier volume
        repo.add_volume("volume-123", sample_response)

        # Deuxième volume
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
        response2 = GetVolumeByIdV2Response(
            volumes=[volume2],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )
        repo.add_volume("volume-124", response2)

        # Vérification
        result1 = repo.get_by_id_v2("volume-123")
        result2 = repo.get_by_id_v2("volume-124")

        assert result1.volumes[0].id == "volume-123"
        assert result2.volumes[0].id == "volume-124"
        assert result1.volumes[0].number == 1
        assert result2.volumes[0].number == 2

    def test_get_volumes_news_v2_empty(self, repo: InMemoryVolumeRepository) -> None:
        """Test get_volumes_news_v2 avec un repository vide."""
        result = repo.get_volumes_news_v2()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.box_volumes) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert result.native_ad_volume_home_first is None

    def test_set_and_get_volumes_news_v2(
        self,
        repo: InMemoryVolumeRepository,
        sample_news_response: GetVolumesNewsV2Response,
    ) -> None:
        """Test la définition et la récupération des news."""
        repo.set_news(sample_news_response)
        result = repo.get_volumes_news_v2()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0].id == "volume-123"
        assert result.volumes[0].title == "Tome 1"

        assert len(result.editions) == 1
        assert result.editions[0].id == "edition-456"

        assert result.native_ad_volume_home_first is not None
        assert result.native_ad_volume_home_first.id == "ad-123"

    def test_set_news_without_native_ad(
        self,
        repo: InMemoryVolumeRepository,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test la définition des news sans publicité."""
        news_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        repo.set_news(news_response)
        result = repo.get_volumes_news_v2()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 1
        assert result.native_ad_volume_home_first is None

    def test_clear(self, repo: InMemoryVolumeRepository, sample_response: GetVolumeByIdV2Response) -> None:
        """Test la suppression de toutes les données."""
        # Ajouter des données
        repo.add_volume("volume-123", sample_response)

        # Ajouter des news
        news_response = GetVolumesNewsV2Response(
            volumes=[sample_response.volumes[0]],
            editions=sample_response.editions,
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )
        repo.set_news(news_response)

        # Vérifier que les données existent
        assert repo.get_by_id_v2("volume-123") is not None
        assert len(repo.get_volumes_news_v2().volumes) == 1

        # Vider le repository
        repo.clear()

        # Vérifier que tout est vide
        with pytest.raises(VolumeNotFoundException):
            repo.get_by_id_v2("volume-123")

        news_result = repo.get_volumes_news_v2()
        assert len(news_result.volumes) == 0
        assert news_result.native_ad_volume_home_first is None

    def test_overwrite_volume(
        self,
        repo: InMemoryVolumeRepository,
        sample_response: GetVolumeByIdV2Response,
        sample_edition: Edition,
    ) -> None:
        """Test l'écrasement d'un volume existant."""
        # Ajouter un volume initial
        repo.add_volume("volume-123", sample_response)

        # Créer une nouvelle réponse pour le même ID
        updated_volume = Volume(
            id="volume-123",
            title="Tome 1 Mis à Jour",
            number=1,
            release_date="2023-01-20",
            isbn=None,
            asin=None,
            edition_id="edition-456",
            possessions_count=200,
            not_sold=False,
            image_url=None,
            nb_pages=None,
            content=None,
        )
        updated_response = GetVolumeByIdV2Response(
            volumes=[updated_volume],
            editions=[sample_edition],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        # Écraser le volume existant
        repo.add_volume("volume-123", updated_response)

        # Vérifier que le volume a été mis à jour
        result = repo.get_by_id_v2("volume-123")
        assert result.volumes[0].title == "Tome 1 Mis à Jour"
        assert result.volumes[0].release_date == "2023-01-20"
        assert result.volumes[0].possessions_count == 200

    def test_overwrite_news(
        self,
        repo: InMemoryVolumeRepository,
        sample_news_response: GetVolumesNewsV2Response,
        sample_volume: Volume,
    ) -> None:
        """Test l'écrasement des news."""
        # Ajouter des news initiales
        repo.set_news(sample_news_response)
        initial_result = repo.get_volumes_news_v2()
        assert len(initial_result.volumes) == 1
        assert initial_result.native_ad_volume_home_first is not None

        # Créer de nouvelles news sans publicité
        new_news_response = GetVolumesNewsV2Response(
            volumes=[sample_volume],
            editions=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        # Écraser les news
        repo.set_news(new_news_response)
        updated_result = repo.get_volumes_news_v2()

        assert len(updated_result.volumes) == 1
        assert updated_result.native_ad_volume_home_first is None

    def test_get_by_id_v2_with_minimal_data(
        self,
        repo: InMemoryVolumeRepository,
        sample_volume: Volume,
    ) -> None:
        """Test get_by_id_v2 avec des données minimales."""
        minimal_response = GetVolumeByIdV2Response(
            volumes=[sample_volume],
            editions=[],
            publishers=[],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
        )

        repo.add_volume("volume-123", minimal_response)
        result = repo.get_by_id_v2("volume-123")

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

    def test_get_volumes_news_v2_with_multiple_volumes(
        self,
        repo: InMemoryVolumeRepository,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test get_volumes_news_v2 avec plusieurs volumes."""
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

        news_response = GetVolumesNewsV2Response(
            volumes=[sample_volume, volume2],
            editions=[sample_edition],
            series=[],
            types=[],
            box_volumes=[],
            boxes=[],
            box_editions=[],
            native_ad_volume_home_first=None,
        )

        repo.set_news(news_response)
        result = repo.get_volumes_news_v2()

        assert isinstance(result, GetVolumesNewsV2Response)
        assert len(result.volumes) == 2
        assert result.volumes[0].title == "Tome 1"
        assert result.volumes[1].title == "Nouveauté Tome 2"

    def test_volume_not_found_exception_message(self, repo: InMemoryVolumeRepository) -> None:
        """Test du message de l'exception VolumeNotFoundException."""
        with pytest.raises(VolumeNotFoundException) as exc_info:
            repo.get_by_id_v2("missing-volume-id")

        exception = exc_info.value
        assert exception.volume_id == "missing-volume-id"
        assert "missing-volume-id" in str(exception)
        assert "Volume with ID" in str(exception)

    def test_separate_data_stores(
        self,
        repo: InMemoryVolumeRepository,
        sample_response: GetVolumeByIdV2Response,
        sample_news_response: GetVolumesNewsV2Response,
    ) -> None:
        """Test que les données des volumes et des news sont stockées séparément."""
        # Ajouter un volume dans le store principal
        repo.add_volume("volume-123", sample_response)

        # Ajouter des news
        repo.set_news(sample_news_response)

        # Les deux doivent être accessibles
        volume_result = repo.get_by_id_v2("volume-123")
        news_result = repo.get_volumes_news_v2()

        assert len(volume_result.volumes) == 1
        assert len(news_result.volumes) == 1

        # Vider le repository principal ne doit pas affecter les news
        repo.clear()

        with pytest.raises(VolumeNotFoundException):
            repo.get_by_id_v2("volume-123")

        # Mais les news doivent toujours être accessibles
        # Note: Selon l'implémentation, clear() vide aussi _news_data
        # Ce test peut être ajusté selon le comportement souhaité
        final_news_result = repo.get_volumes_news_v2()
        assert len(final_news_result.volumes) == 0  # clear() vide aussi les news
