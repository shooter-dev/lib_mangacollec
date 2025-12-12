"""Tests pour les use cases Planning.

This module contains unit tests for Planning use cases.
"""

import pytest

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.application.use_cases import GetPlanningV2UseCase
from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         Serie, TypeSerie, Volume)
from mangacollec.infrastructure.repositories import InMemoryPlanningRepository


@pytest.fixture
def repository() -> InMemoryPlanningRepository:
    """Fixture pour créer un repository en mémoire."""
    return InMemoryPlanningRepository()


@pytest.fixture
def sample_volume() -> Volume:
    """Fixture pour créer un volume de test."""
    return Volume(
        id="vol-1",
        title="Volume 1",
        number=1,
        release_date="2022-09-01",
        isbn="9781234567890",
        asin="B001",
        edition_id="ed-1",
        possessions_count=100,
        not_sold=False,
        image_url="http://example.com/vol1.jpg",
        nb_pages=None,
        content=None,
    )


@pytest.fixture
def sample_edition() -> Edition:
    """Fixture pour créer une édition de test."""
    return Edition(
        id="ed-1",
        title="Edition 1",
        series_id="series-1",
        publisher_id="pub-1",
        parent_edition_id=None,
        volumes_count=10,
        last_volume_number=None,
        commercial_stop=False,
        not_finished=False,
        follow_editions_count=50,
    )


@pytest.fixture
def sample_serie() -> Serie:
    """Fixture pour créer une série de test."""
    return Serie(
        id="series-1",
        title="Serie 1",
        type_id="type-1",
        adult_content=False,
        editions_count=5,
        tasks_count=2,
    )


@pytest.fixture
def sample_type() -> TypeSerie:
    """Fixture pour créer un type de test."""
    return TypeSerie(id="type-1", title="Manga", to_display=True)


@pytest.fixture
def sample_box() -> Box:
    """Fixture pour créer une box de test."""
    return Box(
        id="box-1",
        title="Box 1",
        number=1,
        release_date="2022-10-01",
        isbn="9780987654321",
        asin="B002",
        commercial_stop=False,
        box_edition_id="be-1",
        box_possessions_count=50,
        image_url="http://example.com/box1.jpg",
    )


@pytest.fixture
def sample_box_edition() -> BoxEdition:
    """Fixture pour créer une box_edition de test."""
    return BoxEdition(
        id="be-1",
        title="Box Edition 1",
        publisher_id="pub-1",
        boxes_count=2,
        adult_content=False,
        box_follow_editions_count=10,
    )


@pytest.fixture
def sample_box_volume() -> BoxVolume:
    """Fixture pour créer une box_volume de test."""
    return BoxVolume(
        id="bv-1",
        title=None,
        number=1,
        release_date="2022-10-01",
        isbn="9781234567890",
        asin=None,
        edition_id="ed-1",
        possessions_count=100,
        not_sold=False,
        image_url="http://example.com/boxvol1.jpg",
    )


class TestGetPlanningV2UseCase:
    """Tests pour GetPlanningV2UseCase."""

    def test_get_planning_v2_with_data(
        self,
        repository: InMemoryPlanningRepository,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box: Box,
        sample_box_edition: BoxEdition,
        sample_box_volume: BoxVolume,
    ) -> None:
        """Test de récupération du planning avec toutes les données."""
        # Arrange
        month = "2022-09-30"
        repository.add_planning(
            month=month,
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
            box_volumes=[sample_box_volume],
        )
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 1
        assert result.volumes[0] == sample_volume
        assert len(result.editions) == 1
        assert result.editions[0] == sample_edition
        assert len(result.series) == 1
        assert result.series[0] == sample_serie
        assert len(result.types) == 1
        assert result.types[0] == sample_type
        assert len(result.boxes) == 1
        assert result.boxes[0] == sample_box
        assert len(result.box_editions) == 1
        assert result.box_editions[0] == sample_box_edition
        assert len(result.box_volumes) == 1
        assert result.box_volumes[0] == sample_box_volume

    def test_get_planning_v2_empty(self, repository: InMemoryPlanningRepository) -> None:
        """Test de récupération du planning vide."""
        # Arrange
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase("2022-09-30")

        # Assert
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

    def test_get_planning_v2_multiple_volumes(
        self, repository: InMemoryPlanningRepository, sample_volume: Volume
    ) -> None:
        """Test de récupération du planning avec plusieurs volumes."""
        # Arrange
        month = "2022-09-30"
        volume2 = Volume(
            id="vol-2",
            title="Volume 2",
            number=2,
            release_date="2022-10-01",
            isbn="9781234567891",
            asin=None,
            edition_id="ed-1",
            possessions_count=95,
            not_sold=False,
            image_url="http://example.com/vol2.jpg",
            nb_pages=None,
            content=None,
        )
        repository.add_planning(month=month, volumes=[sample_volume, volume2])
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert len(result.volumes) == 2
        assert result.volumes[0].id == "vol-1"
        assert result.volumes[1].id == "vol-2"

    def test_get_planning_v2_different_months(
        self, repository: InMemoryPlanningRepository, sample_volume: Volume
    ) -> None:
        """Test de récupération du planning pour différents mois."""
        # Arrange
        month1 = "2022-09-30"
        month2 = "2022-10-31"
        volume2 = Volume(
            id="vol-2",
            title="Volume 2",
            number=2,
            release_date="2022-10-01",
            isbn="9781234567891",
            asin=None,
            edition_id="ed-1",
            possessions_count=95,
            not_sold=False,
            image_url="http://example.com/vol2.jpg",
            nb_pages=None,
            content=None,
        )
        repository.add_planning(month=month1, volumes=[sample_volume])
        repository.add_planning(month=month2, volumes=[volume2])
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result1 = usecase(month1)
        result2 = usecase(month2)

        # Assert
        assert len(result1.volumes) == 1
        assert result1.volumes[0].id == "vol-1"
        assert len(result2.volumes) == 1
        assert result2.volumes[0].id == "vol-2"

    def test_get_planning_v2_only_volumes(self, repository: InMemoryPlanningRepository, sample_volume: Volume) -> None:
        """Test de récupération du planning avec uniquement des volumes."""
        # Arrange
        month = "2022-09-30"
        repository.add_planning(month=month, volumes=[sample_volume])
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert len(result.volumes) == 1
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

    def test_get_planning_v2_only_boxes(
        self,
        repository: InMemoryPlanningRepository,
        sample_box: Box,
        sample_box_edition: BoxEdition,
        sample_box_volume: BoxVolume,
    ) -> None:
        """Test de récupération du planning avec uniquement des boxes."""
        # Arrange
        month = "2022-09-30"
        repository.add_planning(
            month=month, boxes=[sample_box], box_editions=[sample_box_edition], box_volumes=[sample_box_volume]
        )
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 1
        assert len(result.box_editions) == 1
        assert len(result.box_volumes) == 1
        assert result.boxes[0].id == "box-1"

    def test_get_planning_v2_complete_data(
        self,
        repository: InMemoryPlanningRepository,
        sample_volume: Volume,
        sample_edition: Edition,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_box: Box,
        sample_box_edition: BoxEdition,
        sample_box_volume: BoxVolume,
    ) -> None:
        """Test de récupération du planning avec toutes les entités."""
        # Arrange
        month = "2022-09-30"
        repository.add_planning(
            month=month,
            volumes=[sample_volume],
            editions=[sample_edition],
            series=[sample_serie],
            types=[sample_type],
            boxes=[sample_box],
            box_editions=[sample_box_edition],
            box_volumes=[sample_box_volume],
        )
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert - Vérifier toutes les entités
        assert isinstance(result.volumes[0], Volume)
        assert isinstance(result.editions[0], Edition)
        assert isinstance(result.series[0], Serie)
        assert isinstance(result.types[0], TypeSerie)
        assert isinstance(result.boxes[0], Box)
        assert isinstance(result.box_editions[0], BoxEdition)
        assert isinstance(result.box_volumes[0], BoxVolume)

        # Vérifier les IDs
        assert result.volumes[0].id == "vol-1"
        assert result.editions[0].id == "ed-1"
        assert result.series[0].id == "series-1"
        assert result.types[0].id == "type-1"
        assert result.boxes[0].id == "box-1"
        assert result.box_editions[0].id == "be-1"
        assert result.box_volumes[0].id == "bv-1"

    def test_get_planning_v2_multiple_editions(
        self, repository: InMemoryPlanningRepository, sample_edition: Edition
    ) -> None:
        """Test de récupération du planning avec plusieurs éditions."""
        # Arrange
        month = "2022-09-30"
        edition2 = Edition(
            id="ed-2",
            title="Edition 2",
            series_id="series-2",
            publisher_id="pub-2",
            parent_edition_id=None,
            volumes_count=5,
            last_volume_number=None,
            commercial_stop=False,
            not_finished=True,
            follow_editions_count=25,
        )
        repository.add_planning(month=month, editions=[sample_edition, edition2])
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert len(result.editions) == 2
        assert result.editions[0].id == "ed-1"
        assert result.editions[1].id == "ed-2"
        assert result.editions[0].title == "Edition 1"
        assert result.editions[1].title == "Edition 2"

    def test_get_planning_v2_preserves_order(
        self, repository: InMemoryPlanningRepository, sample_volume: Volume
    ) -> None:
        """Test que l'ordre des éléments est préservé."""
        # Arrange
        month = "2022-09-30"
        volume2 = Volume(
            id="vol-2",
            title="Volume 2",
            number=2,
            release_date="2022-10-01",
            isbn="9781234567891",
            asin=None,
            edition_id="ed-1",
            possessions_count=95,
            not_sold=False,
            image_url="http://example.com/vol2.jpg",
            nb_pages=None,
            content=None,
        )
        volume3 = Volume(
            id="vol-3",
            title="Volume 3",
            number=3,
            release_date="2022-11-01",
            isbn="9781234567892",
            asin=None,
            edition_id="ed-1",
            possessions_count=90,
            not_sold=False,
            image_url="http://example.com/vol3.jpg",
            nb_pages=None,
            content=None,
        )
        repository.add_planning(month=month, volumes=[sample_volume, volume2, volume3])
        usecase = GetPlanningV2UseCase(repository)

        # Act
        result = usecase(month)

        # Assert
        assert len(result.volumes) == 3
        assert result.volumes[0].id == "vol-1"
        assert result.volumes[1].id == "vol-2"
        assert result.volumes[2].id == "vol-3"
