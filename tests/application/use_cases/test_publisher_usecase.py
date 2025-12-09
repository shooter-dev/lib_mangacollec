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
        """Test retrieving an existing publisher."""
        usecase = GetPublisherByIdV2UseCase(repository)

        response = usecase.execute("bdef8c9e-7395-465d-8175-a1b985d4aa92")

        assert len(response.publishers) == 1
        publisher = response.publishers[0]
        assert isinstance(publisher, Publisher)
        assert publisher.id == "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        assert publisher.title == "Pika"

    def test_get_nonexistent_publisher(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving a non-existent publisher."""
        usecase = GetPublisherByIdV2UseCase(repository)

        with pytest.raises(PublisherNotFoundException):
            usecase.execute("nonexistent-id")


class TestGetAllPublisherUseCase:
    """Tests for GetAllPublisherUseCase."""

    def test_get_all_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving all publishers."""
        usecase = GetAllPublishersV2UseCase(repository)

        result = usecase.execute()

        assert len(result.publishers) == 2
        assert all(isinstance(publisher, Publisher) for publisher in result.publishers)

    def test_get_all_publishers_empty(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving with an empty repository."""
        usecase = GetAllPublishersV2UseCase(repository)

        result = usecase.execute()

        assert result.publishers == []


class TestGetListPublisherUseCase:
    """Tests for GetListPublisherUseCase."""

    def test_get_list_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving the simplified list."""
        usecase = GetListPublishersUseCase(repository)

        items = usecase.execute()

        assert len(items) == 2
        assert all(isinstance(item, PublisherListItem) for item in items)
        assert items[0].title == "Pika"
        assert items[1].title == "Kana"
