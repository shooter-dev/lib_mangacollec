"""Tests for Publisher use cases."""

import pytest

from mangacollec.application.use_cases import (
    GetAllPublishersV2UseCase,
    GetListPublishersUseCase,
    GetPublisherByIdV2UseCase,
)
from mangacollec.domain.entities import Publisher, PublisherListItem
from mangacollec.domain.exceptions import PublisherNotFoundException
from mangacollec.infrastructure.repositories import InMemoryPublisherRepository


@pytest.fixture
def repository() -> InMemoryPublisherRepository:
    """Fixture to create an in-memory repository."""
    return InMemoryPublisherRepository()


@pytest.fixture
def sample_publishers(repository: InMemoryPublisherRepository) -> list[Publisher]:
    """Fixture to create test publishers."""
    publishers = [
        Publisher(
            id="bdef8c9e-7395-465d-8175-a1b985d4aa92",
            title="Pika",
            closed=False,
            editions_count=687,
            no_amazon=False,
        ),
        Publisher(
            id="4c9547ff-2ef6-439a-80b8-ea705a385b76",
            title="Kana",
            closed=False,
            editions_count=596,
            no_amazon=False,
        ),
    ]

    for publisher in publishers:
        repository.add(publisher)

    return publishers


class TestGetByIdPublisherUseCase:
    """Tests for GetByIdPublisherUseCase."""

    def test_get_existing_publisher(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving an existing publisher with all relations."""
        usecase = GetPublisherByIdV2UseCase(repository)

        publisher, editions, box_editions, series, types, volumes, boxes = usecase(
            "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        )

        assert isinstance(publisher, Publisher)
        assert publisher.id == "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        assert publisher.title == "Pika"
        # Vérifier que les listes sont vides (InMemory repository)
        assert editions == []
        assert box_editions == []
        assert series == []
        assert types == []
        assert volumes == []
        assert boxes == []

    def test_get_nonexistent_publisher(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving a non-existent publisher."""
        usecase = GetPublisherByIdV2UseCase(repository)

        with pytest.raises(PublisherNotFoundException) as exc_info:
            usecase("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)


class TestGetAllPublisherUseCase:
    """Tests for GetAllPublisherUseCase."""

    def test_get_all_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving all publishers."""
        usecase = GetAllPublishersV2UseCase(repository)

        result = usecase()

        assert len(result) == 2
        assert all(isinstance(publisher, Publisher) for publisher in result)

    def test_get_all_publishers_empty(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving with an empty repository."""
        usecase = GetAllPublishersV2UseCase(repository)

        result = usecase()

        assert result == []


class TestGetListPublisherUseCase:
    """Tests for GetListPublisherUseCase."""

    def test_get_list_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving the simplified list."""
        usecase = GetListPublishersUseCase(repository)

        items = usecase()

        assert len(items) == 2
        assert all(isinstance(item, PublisherListItem) for item in items)
        assert items[0].title == "Pika"
        assert items[1].title == "Kana"
