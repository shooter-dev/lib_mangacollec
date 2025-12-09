"""Tests for APIPublisherRepository."""

from unittest.mock import Mock

import pytest

from mangacollec.application import (GetAllPublishersV2Response,
                                     GetPublisherByIdV2Response)
from mangacollec.application import \
    IMangaCollecAPI
from mangacollec.domain.entities import Publisher, PublisherListItem
from mangacollec.domain import PublisherNotFoundException
from mangacollec.infrastructure import \
    APIPublisherRepository


class TestAPIPublisherRepository:
    """Tests for APIPublisherRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture for creating a mock of the API client."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIPublisherRepository:
        """Fixture for creating a repository with a mock API."""
        return APIPublisherRepository(mock_api_client)

    @pytest.fixture
    def sample_publisher_data(self) -> dict:
        """Fixture for creating test publisher data."""
        return {
            "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "title": "Pika",
            "closed": False,
            "editions_count": 687,
            "no_amazon": False,
        }

    def test_get_by_id_success(
        self,
        repository: APIPublisherRepository,
        mock_api_client: Mock,
        sample_publisher_data: dict,
    ) -> None:
        """Test retrieving a publisher by ID with all its relations."""
        mock_api_client.get.return_value = {
            "publishers": [sample_publisher_data],
            "editions": [],
            "box_editions": [],
            "series": [],
            "types": [],
            "volumes": [],
            "boxes": [],
        }

        result = repository.get_by_id_v2("bdef8c9e-7395-465d-8175-a1b985d4aa92")

        assert isinstance(result, GetPublisherByIdV2Response)
        assert len(result.publishers) == 1
        publisher = result.publishers[0]
        assert isinstance(publisher, Publisher)
        assert publisher.id == "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        assert publisher.title == "Pika"

        mock_api_client.get.assert_called_once_with("/v2/publishers/bdef8c9e-7395-465d-8175-a1b985d4aa92")

    def test_get_by_id_not_found(self, repository: APIPublisherRepository, mock_api_client: Mock) -> None:
        """Test retrieving a non-existent publisher."""
        mock_api_client.get.return_value = {"publishers": []}

        with pytest.raises(PublisherNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_all_success(
        self,
        repository: APIPublisherRepository,
        mock_api_client: Mock,
        sample_publisher_data: dict,
    ) -> None:
        """Test retrieving all publishers."""
        mock_api_client.get.return_value = {"publishers": [sample_publisher_data]}

        result = repository.get_all_v2()

        assert isinstance(result, GetAllPublishersV2Response)
        assert len(result.publishers) == 1
        assert result.publishers[0].title == "Pika"

        mock_api_client.get.assert_called_once_with("/v2/publishers/")

    def test_get_list_success(
        self,
        repository: APIPublisherRepository,
        mock_api_client: Mock,
        sample_publisher_data: dict,
    ) -> None:
        """Test retrieving the simplified list of publishers."""
        mock_api_client.get.return_value = {"publishers": [sample_publisher_data]}

        items = repository.get_list()

        assert len(items) == 1
        assert isinstance(items[0], PublisherListItem)
        assert items[0].title == "Pika"
