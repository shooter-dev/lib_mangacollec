"""Tests for APIReadRepository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.exceptions import (ReadCreationException,
                                           ReadDeletionException)
from mangacollec.infrastructure.repositories import APIReadRepository


class TestAPIReadRepository:
    """Tests for APIReadRepository."""

    @pytest.fixture
    def mock_client_api(self) -> MagicMock:
        """Create a mock MangaCollecAPI client."""
        return MagicMock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_client_api: MagicMock) -> APIReadRepository:
        """Create APIReadRepository with mock client."""
        return APIReadRepository(mock_client_api)

    def test_create_reads_multiple_v1_success(self, repository: APIReadRepository, mock_client_api: MagicMock) -> None:
        """Test creating multiple reads successfully."""
        volume_ids = ["volume_1", "volume_2"]

        # Mock API response
        mock_client_api.post.return_value = {
            "reads": [
                {
                    "id": "read_1",
                    "user_id": "user_123",
                    "volume_id": "volume_1",
                    "created_at": "2024-12-11T10:30:00Z",
                },
                {
                    "id": "read_2",
                    "user_id": "user_123",
                    "volume_id": "volume_2",
                    "created_at": "2024-12-11T10:31:00Z",
                },
            ],
            "read_editions": [
                {
                    "id": "read_edition_1",
                    "user_id": "user_123",
                    "edition_id": "edition_1",
                    "reading": True,
                    "created_at": "2024-12-11T10:30:00Z",
                },
                {
                    "id": "read_edition_2",
                    "user_id": "user_123",
                    "edition_id": "edition_2",
                    "reading": True,
                    "created_at": "2024-12-11T10:31:00Z",
                },
            ],
        }

        # Call repository
        response = repository.create_reads_multiple_v1(volume_ids)

        # Verify API call
        mock_client_api.post.assert_called_once_with(
            "/v1/reads_multiple",
            data=[{"volume_id": "volume_1"}, {"volume_id": "volume_2"}],
        )

        # Verify response
        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[0].volume_id == "volume_1"
        assert response.reads[1].id == "read_2"
        assert response.reads[1].volume_id == "volume_2"
        assert response.read_editions[0].id == "read_edition_1"
        assert response.read_editions[0].reading is True

    def test_create_reads_multiple_v1_single_volume(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test creating a single read."""
        volume_ids = ["volume_1"]

        mock_client_api.post.return_value = {
            "reads": [
                {
                    "id": "read_1",
                    "user_id": "user_123",
                    "volume_id": "volume_1",
                    "created_at": "2024-12-11T10:30:00Z",
                }
            ],
            "read_editions": [
                {
                    "id": "read_edition_1",
                    "user_id": "user_123",
                    "edition_id": "edition_1",
                    "reading": True,
                    "created_at": "2024-12-11T10:30:00Z",
                }
            ],
        }

        response = repository.create_reads_multiple_v1(volume_ids)

        mock_client_api.post.assert_called_once_with("/v1/reads_multiple", data=[{"volume_id": "volume_1"}])
        assert len(response.reads) == 1
        assert len(response.read_editions) == 1

    def test_create_reads_multiple_v1_empty_list(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test creating reads with empty volume list."""
        volume_ids: list[str] = []

        mock_client_api.post.return_value = {"reads": [], "read_editions": []}

        response = repository.create_reads_multiple_v1(volume_ids)

        mock_client_api.post.assert_called_once_with("/v1/reads_multiple", data=[])
        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_create_reads_multiple_v1_api_error(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test creation fails when API raises an error."""
        volume_ids = ["volume_1"]

        mock_client_api.post.side_effect = Exception("API Error")

        with pytest.raises(ReadCreationException) as exc_info:
            repository.create_reads_multiple_v1(volume_ids)

        assert exc_info.value.volume_ids == volume_ids
        assert "API Error" in str(exc_info.value)

    def test_delete_reads_multiple_v1_success(self, repository: APIReadRepository, mock_client_api: MagicMock) -> None:
        """Test deleting multiple reads successfully."""
        read_ids = ["read_1", "read_2"]

        mock_client_api.delete.return_value = {
            "reads": [
                {"id": "read_1", "deleted": True},
                {"id": "read_2", "deleted": True},
            ],
            "read_editions": [
                {"id": "read_edition_1", "deleted": True},
                {"id": "read_edition_2", "deleted": True},
            ],
        }

        response = repository.delete_reads_multiple_v1(read_ids)

        mock_client_api.delete.assert_called_once_with("/v1/reads_multiple", data=[{"id": "read_1"}, {"id": "read_2"}])
        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[0].deleted is True
        assert response.reads[1].id == "read_2"
        assert response.reads[1].deleted is True

    def test_delete_reads_multiple_v1_single_read(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test deleting a single read."""
        read_ids = ["read_1"]

        mock_client_api.delete.return_value = {
            "reads": [{"id": "read_1", "deleted": True}],
            "read_editions": [{"id": "read_edition_1", "deleted": True}],
        }

        response = repository.delete_reads_multiple_v1(read_ids)

        mock_client_api.delete.assert_called_once_with("/v1/reads_multiple", data=[{"id": "read_1"}])
        assert len(response.reads) == 1
        assert len(response.read_editions) == 1

    def test_delete_reads_multiple_v1_empty_list(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test deleting with empty ID list."""
        read_ids: list[str] = []

        mock_client_api.delete.return_value = {"reads": [], "read_editions": []}

        response = repository.delete_reads_multiple_v1(read_ids)

        mock_client_api.delete.assert_called_once_with("/v1/reads_multiple", data=[])
        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_delete_reads_multiple_v1_partial_success(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test deleting reads with partial success."""
        read_ids = ["read_1", "nonexistent_id"]

        mock_client_api.delete.return_value = {
            "reads": [
                {"id": "read_1", "deleted": True},
                {"id": "nonexistent_id", "deleted": False},
            ],
            "read_editions": [{"id": "read_edition_1", "deleted": True}],
        }

        response = repository.delete_reads_multiple_v1(read_ids)

        assert len(response.reads) == 2
        assert response.reads[0].deleted is True
        assert response.reads[1].deleted is False
        assert len(response.read_editions) == 1

    def test_delete_reads_multiple_v1_api_error(
        self, repository: APIReadRepository, mock_client_api: MagicMock
    ) -> None:
        """Test deletion fails when API raises an error."""
        read_ids = ["read_1"]

        mock_client_api.delete.side_effect = Exception("API Error")

        with pytest.raises(ReadDeletionException) as exc_info:
            repository.delete_reads_multiple_v1(read_ids)

        assert exc_info.value.read_ids == read_ids
        assert "API Error" in str(exc_info.value)
