"""Tests unitaires pour InMemoryPlanningRepository.

This module contains unit tests for the InMemoryPlanningRepository.
"""

import pytest

from mangacollec.application.dto import GetPlanningV2Response
from mangacollec.domain.entities import (Box, BoxEdition, BoxVolume, Edition,
                                         Serie, TypeSerie, Volume)
from mangacollec.infrastructure.repositories import InMemoryPlanningRepository


class TestInMemoryPlanningRepository:
    """Tests pour InMemoryPlanningRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryPlanningRepository:
        """Fixture pour créer un repository."""
        return InMemoryPlanningRepository()

    @pytest.fixture
    def sample_volume(self) -> Volume:
        """Fixture pour créer un volume de test."""
        return Volume(
            id="vol-1",
            title="Volume 1",
            number=1,
            release_date="2022-09-01",
            isbn="9781234567890",
            asin=None,
            edition_id="ed-1",
            possessions_count=100,
            not_sold=False,
            image_url="http://example.com/vol1.jpg",
            nb_pages=None,
            content=None,
        )

    @pytest.fixture
    def sample_edition(self) -> Edition:
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
    def sample_serie(self) -> Serie:
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
    def sample_type(self) -> TypeSerie:
        """Fixture pour créer un type de test."""
        return TypeSerie(id="type-1", title="Manga", to_display=True)

    @pytest.fixture
    def sample_box(self) -> Box:
        """Fixture pour créer une box de test."""
        return Box(
            id="box-1",
            title="Box 1",
            number=1,
            release_date="2022-10-01",
            isbn="9780987654321",
            asin=None,
            commercial_stop=False,
            box_edition_id="be-1",
            box_possessions_count=50,
            image_url="http://example.com/box1.jpg",
        )

    @pytest.fixture
    def sample_box_edition(self) -> BoxEdition:
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
    def sample_box_volume(self) -> BoxVolume:
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

    def test_get_planning_v2_empty(self, repository: InMemoryPlanningRepository) -> None:
        """Test get_planning_v2 quand le repository est vide."""
        # Act
        result = repository.get_planning_v2("2022-09-30")

        # Assert
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

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
        """Test get_planning_v2 avec des données."""
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

        # Act
        result = repository.get_planning_v2(month)

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

    def test_add_planning_with_multiple_items(
        self,
        repository: InMemoryPlanningRepository,
        sample_volume: Volume,
        sample_edition: Edition,
    ) -> None:
        """Test add_planning avec plusieurs items."""
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

        # Act
        repository.add_planning(month=month, volumes=[sample_volume, volume2], editions=[sample_edition])

        # Assert
        result = repository.get_planning_v2(month)
        assert len(result.volumes) == 2
        assert len(result.editions) == 1

    def test_add_planning_overwrites_existing_month(
        self, repository: InMemoryPlanningRepository, sample_volume: Volume
    ) -> None:
        """Test que add_planning écrase les données existantes pour un mois donné."""
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

        # Act
        repository.add_planning(month=month, volumes=[sample_volume])
        repository.add_planning(month=month, volumes=[volume2])

        # Assert
        result = repository.get_planning_v2(month)
        assert len(result.volumes) == 1
        assert result.volumes[0] == volume2

    def test_get_planning_v2_different_months(
        self, repository: InMemoryPlanningRepository, sample_volume: Volume
    ) -> None:
        """Test que les données sont isolées par mois."""
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

        # Act
        repository.add_planning(month=month1, volumes=[sample_volume])
        repository.add_planning(month=month2, volumes=[volume2])

        # Assert
        result1 = repository.get_planning_v2(month1)
        result2 = repository.get_planning_v2(month2)
        assert len(result1.volumes) == 1
        assert result1.volumes[0] == sample_volume
        assert len(result2.volumes) == 1
        assert result2.volumes[0] == volume2

    def test_clear(self, repository: InMemoryPlanningRepository, sample_volume: Volume) -> None:
        """Test la méthode clear."""
        # Arrange
        month = "2022-09-30"
        repository.add_planning(month=month, volumes=[sample_volume])
        assert len(repository.get_planning_v2(month).volumes) == 1

        # Act
        repository.clear()
        result = repository.get_planning_v2(month)

        # Assert
        assert len(result.volumes) == 0

    def test_clear_empty_repository(self, repository: InMemoryPlanningRepository) -> None:
        """Test clear sur un repository déjà vide."""
        # Act
        repository.clear()
        result = repository.get_planning_v2("2022-09-30")

        # Assert
        assert len(result.volumes) == 0

    def test_add_planning_with_none_values(self, repository: InMemoryPlanningRepository) -> None:
        """Test add_planning avec des valeurs None (devrait créer des listes vides)."""
        # Arrange
        month = "2022-09-30"

        # Act
        repository.add_planning(month=month)

        # Assert
        result = repository.get_planning_v2(month)
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0
        assert len(result.box_volumes) == 0

    def test_add_planning_with_empty_lists(self, repository: InMemoryPlanningRepository) -> None:
        """Test add_planning avec des listes vides explicites."""
        # Arrange
        month = "2022-09-30"

        # Act
        repository.add_planning(
            month=month,
            volumes=[],
            editions=[],
            series=[],
            types=[],
            boxes=[],
            box_editions=[],
            box_volumes=[],
        )

        # Assert
        result = repository.get_planning_v2(month)
        assert isinstance(result, GetPlanningV2Response)
        assert len(result.volumes) == 0
        assert len(result.editions) == 0
