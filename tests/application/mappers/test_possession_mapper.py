"""Tests for PossessionMapper."""

from datetime import datetime

from mangacollec.application.dto import (AddPossessionsMultipleV1Response,
                                         DeletePossessionsMultipleV1Response)
from mangacollec.application.mappers import PossessionMapper
from mangacollec.domain.entities import Possession


class TestPossessionMapperFromDict:
    """Tests for PossessionMapper.from_dict()."""

    def test_from_dict(self) -> None:
        """Test converting API dict to Possession entity."""
        api_data = {
            "id": "possession_123",
            "user_id": "user_456",
            "volume_id": "volume_789",
            "created_at": "2024-12-11T10:30:00Z",
        }

        possession = PossessionMapper.from_dict(api_data)

        assert possession.id == "possession_123"
        assert possession.user_id == "user_456"
        assert possession.volume_id == "volume_789"
        assert possession.created_at.year == 2024
        assert possession.created_at.month == 12
        assert possession.created_at.day == 11

    def test_from_dict_deleted(self) -> None:
        """Test converting API dict to PossessionDeleted entity."""
        api_data = {
            "id": "possession_123",
            "deleted": True,
        }

        possession_deleted = PossessionMapper.from_dict_deleted(api_data)

        assert possession_deleted.id == "possession_123"
        assert possession_deleted.deleted is True

    def test_from_dict_follow_edition_deleted(self) -> None:
        """Test converting API dict to FollowEditionDeleted entity."""
        api_data = {
            "id": "follow_edition_123",
            "deleted": True,
        }

        follow_edition_deleted = PossessionMapper.from_dict_follow_edition_deleted(api_data)

        assert follow_edition_deleted.id == "follow_edition_123"
        assert follow_edition_deleted.deleted is True

    def test_from_dict_loan_deleted(self) -> None:
        """Test converting API dict to LoanDeleted entity."""
        api_data = {
            "id": "loan_123",
            "deleted": True,
        }

        loan_deleted = PossessionMapper.from_dict_loan_deleted(api_data)

        assert loan_deleted.id == "loan_123"
        assert loan_deleted.deleted is True


class TestPossessionMapperToDict:
    """Tests for PossessionMapper.to_dict()."""

    def test_to_dict(self) -> None:
        """Test converting Possession entity to dict."""
        possession = Possession(
            id="possession_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=datetime(2024, 12, 11, 10, 30, 0),
        )

        result = PossessionMapper.to_dict(possession)

        assert result["id"] == "possession_123"
        assert result["user_id"] == "user_456"
        assert result["volume_id"] == "volume_789"
        assert "created_at" in result


class TestPossessionMapperFromAddPossessionsResponse:
    """Tests for PossessionMapper.from_add_possessions_response()."""

    def test_from_add_possessions_response(self) -> None:
        """Test converting full API response to AddPossessionsMultipleV1Response."""
        api_response = {
            "possessions": [
                {
                    "id": "possession_1",
                    "user_id": "user_1",
                    "volume_id": "volume_1",
                    "created_at": "2024-12-11T10:30:00Z",
                },
                {
                    "id": "possession_2",
                    "user_id": "user_1",
                    "volume_id": "volume_2",
                    "created_at": "2024-12-11T10:31:00Z",
                },
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

        response = PossessionMapper.from_add_possessions_response(api_response)

        assert isinstance(response, AddPossessionsMultipleV1Response)
        assert len(response.possessions) == 2
        assert len(response.follow_editions) == 1
        assert response.possessions[0].id == "possession_1"
        assert response.follow_editions[0].id == "follow_1"

    def test_from_add_possessions_response_empty(self) -> None:
        """Test converting empty API response."""
        api_response = {
            "possessions": [],
            "follow_editions": [],
        }

        response = PossessionMapper.from_add_possessions_response(api_response)

        assert isinstance(response, AddPossessionsMultipleV1Response)
        assert len(response.possessions) == 0
        assert len(response.follow_editions) == 0


class TestPossessionMapperFromDeletePossessionsResponse:
    """Tests for PossessionMapper.from_delete_possessions_response()."""

    def test_from_delete_possessions_response(self) -> None:
        """Test converting full API response to DeletePossessionsMultipleV1Response."""
        api_response = {
            "possessions": [
                {"id": "possession_1", "deleted": True},
                {"id": "possession_2", "deleted": True},
            ],
            "follow_editions": [
                {"id": "follow_1", "deleted": True},
            ],
            "loans": [
                {"id": "loan_1", "deleted": True},
            ],
        }

        response = PossessionMapper.from_delete_possessions_response(api_response)

        assert isinstance(response, DeletePossessionsMultipleV1Response)
        assert len(response.possessions) == 2
        assert len(response.follow_editions) == 1
        assert len(response.loans) == 1
        assert response.possessions[0].id == "possession_1"
        assert response.possessions[0].deleted is True
        assert response.follow_editions[0].id == "follow_1"
        assert response.loans[0].id == "loan_1"

    def test_from_delete_possessions_response_empty_loans(self) -> None:
        """Test converting API response with no loans."""
        api_response = {
            "possessions": [
                {"id": "possession_1", "deleted": True},
            ],
            "follow_editions": [
                {"id": "follow_1", "deleted": True},
            ],
            "loans": [],
        }

        response = PossessionMapper.from_delete_possessions_response(api_response)

        assert isinstance(response, DeletePossessionsMultipleV1Response)
        assert len(response.possessions) == 1
        assert len(response.follow_editions) == 1
        assert len(response.loans) == 0
