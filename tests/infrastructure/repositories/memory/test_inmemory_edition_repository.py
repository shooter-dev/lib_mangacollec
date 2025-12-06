"""Tests pour InMemoryEditionRepository.

This module contains unit tests for the InMemory Edition repository.
"""

import pytest

from src.application.dto.responses import GetEditionByIdV2Response
from src.domain.entities import Edition, Publisher, Serie, TypeSerie, Volume
from src.domain.execptions.edition_exceptions import EditionNotFoundException
from src.infrastructure.repositories.memory.in_memory_edition_repository import (
    InMemoryEditionRepository,
)


class TestInMemoryEditionRepository:
    """Tests pour InMemoryEditionRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryEditionRepository:
        """Fixture pour créer un repository en mémoire vide."""
        return InMemoryEditionRepository()

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

    def test_repository_initialization(self, repository: InMemoryEditionRepository) -> None:
        """Test d'initialisation du repository."""
        assert repository._editions == {}
        assert repository._publishers == {}
        assert repository._series == {}
        assert repository._types == {}
        assert repository._volumes == {}

    def test_add_edition(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
    ) -> None:
        """Test d'ajout d'une édition."""
        result = repository.add_edition(sample_edition)

        assert result == sample_edition
        assert repository._editions["edition-123"] == sample_edition

    def test_add_publisher(
        self,
        repository: InMemoryEditionRepository,
        sample_publisher: Publisher,
    ) -> None:
        """Test d'ajout d'un publisher."""
        result = repository.add_publisher(sample_publisher)

        assert result == sample_publisher
        assert repository._publishers["publisher-789"] == sample_publisher

    def test_add_serie(
        self,
        repository: InMemoryEditionRepository,
        sample_serie: Serie,
    ) -> None:
        """Test d'ajout d'une série."""
        result = repository.add_serie(sample_serie)

        assert result == sample_serie
        assert repository._series["series-456"] == sample_serie

    def test_add_type(
        self,
        repository: InMemoryEditionRepository,
        sample_type: TypeSerie,
    ) -> None:
        """Test d'ajout d'un type."""
        result = repository.add_type(sample_type)

        assert result == sample_type
        assert repository._types["type-001"] == sample_type

    def test_add_volumes(
        self,
        repository: InMemoryEditionRepository,
        sample_volume: Volume,
    ) -> None:
        """Test d'ajout de volumes."""
        volumes = [sample_volume]
        result = repository.add_volumes("edition-123", volumes)

        assert result == volumes
        assert repository._volumes["edition-123"] == volumes

    def test_get_edition_by_id_success(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
        sample_type: TypeSerie,
        sample_volume: Volume,
    ) -> None:
        """Test de récupération d'une édition par ID avec toutes les relations."""
        # Préparation
        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)
        repository.add_serie(sample_serie)
        repository.add_type(sample_type)
        repository.add_volumes("edition-123", [sample_volume])

        # Exécution
        response = repository.get_edition_by_id_v2("edition-123")

        # Vérifications
        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.editions) == 1
        assert response.editions[0] == sample_edition
        assert len(response.publishers) == 1
        assert isinstance(response.publishers[0], Publisher)
        assert response.publishers[0] == sample_publisher
        assert len(response.series) == 1
        assert response.series[0] == sample_serie
        assert len(response.types) == 1
        assert response.types[0] == sample_type
        assert len(response.volumes) == 1
        assert response.volumes[0] == sample_volume

    def test_get_edition_by_id_not_found(
        self,
        repository: InMemoryEditionRepository,
    ) -> None:
        """Test de récupération d'une édition inexistante."""
        with pytest.raises(EditionNotFoundException) as exc_info:
            repository.get_edition_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_edition_by_id_with_default_publisher(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
    ) -> None:
        """Test de récupération avec publisher par défaut (non trouvé)."""
        repository.add_edition(sample_edition)

        response = repository.get_edition_by_id_v2("edition-123")

        # Vérifier que le publisher par défaut a été créé
        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.publishers) == 1
        assert isinstance(response.publishers[0], Publisher)
        assert response.publishers[0].id == "publisher-789"
        assert response.publishers[0].title == "Unknown Publisher"
        assert response.publishers[0].closed is False
        assert response.publishers[0].editions_count == 0
        assert response.publishers[0].no_amazon is False

    def test_get_edition_by_id_without_serie(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération sans série."""
        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert response.series == []
        assert response.types == []

    def test_get_edition_by_id_without_volumes(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test de récupération sans volumes."""
        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert response.volumes == []

    def test_get_edition_by_id_without_type(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
        sample_publisher: Publisher,
        sample_serie: Serie,
    ) -> None:
        """Test de récupération avec série mais sans type."""
        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)
        repository.add_serie(sample_serie)

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.series) == 1
        assert response.types == []

    def test_get_edition_by_id_multiple_volumes(
        self,
        repository: InMemoryEditionRepository,
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
        )

        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)
        repository.add_volumes("edition-123", [volume1, volume2])

        response = repository.get_edition_by_id_v2("edition-123")

        assert isinstance(response, GetEditionByIdV2Response)
        assert len(response.volumes) == 2
        assert response.volumes[0].number == 1
        assert response.volumes[1].number == 2

    def test_clear_repository(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
        sample_publisher: Publisher,
    ) -> None:
        """Test du nettoyage du repository."""
        repository.add_edition(sample_edition)
        repository.add_publisher(sample_publisher)

        repository.clear()

        assert repository._editions == {}
        assert repository._publishers == {}
        assert repository._series == {}
        assert repository._types == {}
        assert repository._volumes == {}

    def test_add_multiple_editions(
        self,
        repository: InMemoryEditionRepository,
    ) -> None:
        """Test d'ajout de plusieurs éditions."""
        edition1 = Edition(
            id="edition-1",
            title="Edition 1",
            series_id="series-1",
            publisher_id="publisher-1",
            parent_edition_id=None,
            volumes_count=10,
            last_volume_number=10,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=100,
        )
        edition2 = Edition(
            id="edition-2",
            title="Edition 2",
            series_id="series-1",
            publisher_id="publisher-1",
            parent_edition_id="edition-1",
            volumes_count=5,
            last_volume_number=5,
            commercial_stop=False,
            not_finished=False,
            follow_editions_count=50,
        )

        repository.add_edition(edition1)
        repository.add_edition(edition2)

        assert len(repository._editions) == 2
        assert repository._editions["edition-1"] == edition1
        assert repository._editions["edition-2"] == edition2

    def test_override_edition(
        self,
        repository: InMemoryEditionRepository,
        sample_edition: Edition,
    ) -> None:
        """Test de remplacement d'une édition existante."""
        repository.add_edition(sample_edition)

        # Créer une nouvelle édition avec le même ID mais des valeurs différentes
        updated_edition = Edition(
            id="edition-123",
            title="Updated Edition",
            series_id="series-456",
            publisher_id="publisher-789",
            parent_edition_id=None,
            volumes_count=100,
            last_volume_number=100,
            commercial_stop=True,
            not_finished=False,
            follow_editions_count=2000,
        )

        repository.add_edition(updated_edition)

        assert repository._editions["edition-123"] == updated_edition
        assert repository._editions["edition-123"].title == "Updated Edition"
        assert repository._editions["edition-123"].volumes_count == 100
