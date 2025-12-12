"""Tests for APIPossessionRepository."""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.domain.exceptions import (
    PossessionCreationException,
    PossessionDeletionException,
)
from mangacollec.infrastructure.repositories import APIPossessionRepository


class TestAPIPossessionRepository:
    """Tests for APIPossessionRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Create a mock API client."""
        return Mock()

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIPossessionRepository:
        """Create an APIPossessionRepository with mocked API client."""
        return APIPossessionRepository(mock_api_client)

    def test_add_possessions_multiple_v1_success(
        self, repository: APIPossessionRepository, mock_api_client: Mock
    ) -> None:
        """Test adding multiple possessions successfully."""
        mock_api_client.post.return_value = {
            "possessions": [
                {
                    "id": "possession_1",
                    "user_id": "user_1",
                    "volume_id": "volume_1",
                    "created_at": "2024-12-11T10:30:00Z",
                }
            ],
            "follow_editions": [
                {
                    "id": "follow_1",
                    "user_id": "user_1",
                    "edition_id": "edition_1",
                    "following": True,
                    "created_at": "2024-12-11T10:30:00Z",
                    "updated_at": "2024-12-11T10:30:00Z",
                }
            ],
        }

        volume_ids = ["volume_1"]
        response = repository.add_possessions_multiple_v1(volume_ids)

        assert isinstance(response, AddPossessionsMultipleV1Response)
        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        mock_api_client.post.assert_called_once_with("/v1/possessions_multiple", data={"volume_ids": volume_ids})

    def test_add_possessions_multiple_v1_failure(
        self, repository: APIPossessionRepository, mock_api_client: Mock
    ) -> None:
        """Test adding possessions with API failure."""
        mock_api_client.post.side_effect = Exception("API Error")

        with pytest.raises(PossessionCreationException) as exc_info:
            repository.add_possessions_multiple_v1(["volume_1"])

        assert "API Error" in str(exc_info.value)

    def test_delete_possessions_multiple_v1_success(
        self, repository: APIPossessionRepository, mock_api_client: Mock
    ) -> None:
        """Test deleting multiple possessions successfully."""
        mock_api_client.delete.return_value = {
            "possessions": [
                {"id": "possession_1", "deleted": True},
            ],
            "follow_editions": [
                {"id": "follow_1", "deleted": True},
            ],
            "loans": [],
        }

        possession_ids = ["possession_1"]
        response = repository.delete_possessions_multiple_v1(possession_ids)

        assert isinstance(response, DeletePossessionsMultipleV1Response)
        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        assert len(response.loans) == 0
        assert response.possessions[0].deleted is True
        mock_api_client.delete.assert_called_once_with(
            "/v1/possessions_multiple", data={"possession_ids": possession_ids}
        )

    def test_delete_possessions_multiple_v1_with_loans(
        self, repository: APIPossessionRepository, mock_api_client: Mock
    ) -> None:
        """Test deleting possessions with associated loans."""
        mock_api_client.delete.return_value = {
            "possessions": [
                {"id": "possession_1", "deleted": True},
            ],
            "follow_editions": [
                {"id": "follow_1", "deleted": True},
            ],
            "loans": [
                {"id": "loan_1", "deleted": True},
            ],
        }

        possession_ids = ["possession_1"]
        response = repository.delete_possessions_multiple_v1(possession_ids)

        assert len(response.loans) == 1
        assert response.loans[0].deleted is True

    def test_delete_possessions_multiple_v1_failure(
        self, repository: APIPossessionRepository, mock_api_client: Mock
    ) -> None:
        """Test deleting possessions with API failure."""
        mock_api_client.delete.side_effect = Exception("API Error")

        with pytest.raises(PossessionDeletionException) as exc_info:
            repository.delete_possessions_multiple_v1(["possession_1"])

        assert "API Error" in str(exc_info.value)
