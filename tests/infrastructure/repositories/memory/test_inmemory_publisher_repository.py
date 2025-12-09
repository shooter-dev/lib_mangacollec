"""Tests for InMemoryPublisherRepository."""

import pytest

from mangacollec.application.dto.responses.publisher_responses import (
    GetAllPublishersV2Response, GetPublisherByIdV2Response)
from mangacollec.domain.entities.publisher import Publisher, PublisherListItem
from mangacollec.domain import PublisherNotFoundException
from mangacollec.infrastructure import \
    InMemoryPublisherRepository


class TestInMemoryPublisherRepository:
    """Tests for InMemoryPublisherRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryPublisherRepository:
        """Fixture to create an in-memory repository."""
        return InMemoryPublisherRepository()

    @pytest.fixture
    def sample_publishers(self, repository: InMemoryPublisherRepository) -> list[Publisher]:
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

    def test_add_publisher(self, repository: InMemoryPublisherRepository) -> None:
        """Test adding a publisher to the repository."""
        publisher = Publisher(
            id="test-id",
            title="Test Publisher",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )

        repository.add(publisher)

        result = repository.get_by_id_v2("test-id")
        assert len(result.publishers) == 1
        assert result.publishers[0].title == "Test Publisher"

    def test_get_all_v2_empty(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving all publishers from an empty repository."""
        result = repository.get_all_v2()

        assert isinstance(result, GetAllPublishersV2Response)
        assert len(result.publishers) == 0

    def test_get_all_v2_with_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving all publishers."""
        result = repository.get_all_v2()

        assert isinstance(result, GetAllPublishersV2Response)
        assert len(result.publishers) == 2
        assert all(isinstance(p, Publisher) for p in result.publishers)

    def test_get_by_id_v2_existing(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving an existing publisher by ID."""
        result = repository.get_by_id_v2("bdef8c9e-7395-465d-8175-a1b985d4aa92")

        assert isinstance(result, GetPublisherByIdV2Response)
        assert len(result.publishers) == 1
        assert result.publishers[0].title == "Pika"
        assert len(result.editions) == 0
        assert len(result.box_editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.volumes) == 0
        assert len(result.boxes) == 0

    def test_get_by_id_v2_not_found(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving a non-existent publisher."""
        with pytest.raises(PublisherNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_list_empty(self, repository: InMemoryPublisherRepository) -> None:
        """Test retrieving the simplified list from an empty repository."""
        items = repository.get_list()

        assert len(items) == 0

    def test_get_list_with_publishers(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test retrieving the simplified list of publishers."""
        items = repository.get_list()

        assert len(items) == 2
        assert all(isinstance(item, PublisherListItem) for item in items)
        assert items[0].title == "Pika"
        assert items[1].title == "Kana"

    def test_clear(
        self,
        repository: InMemoryPublisherRepository,
        sample_publishers: list[Publisher],
    ) -> None:
        """Test clearing the repository."""
        repository.clear()

        result = repository.get_all_v2()
        assert len(result.publishers) == 0

    def test_add_overwrites_existing(self, repository: InMemoryPublisherRepository) -> None:
        """Test that adding a publisher with the same ID overwrites the existing one."""
        publisher1 = Publisher(
            id="test-id",
            title="First Title",
            closed=False,
            editions_count=10,
            no_amazon=False,
        )
        publisher2 = Publisher(
            id="test-id",
            title="Second Title",
            closed=True,
            editions_count=20,
            no_amazon=True,
        )

        repository.add(publisher1)
        repository.add(publisher2)

        result = repository.get_by_id_v2("test-id")
        assert len(result.publishers) == 1
        assert result.publishers[0].title == "Second Title"
        assert result.publishers[0].closed is True
        assert result.publishers[0].editions_count == 20
