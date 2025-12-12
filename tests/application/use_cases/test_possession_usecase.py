"""Tests for Possession use cases."""

from datetime import datetime
from unittest.mock import Mock

import pytest

from mangacollec.application.dto import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.application.use_cases import (
    AddPossessionsMultipleV1UseCase,
    DeletePossessionsMultipleV1UseCase,
)
from mangacollec.domain.entities import (
    FollowEdition,
    FollowEditionDeleted,
    LoanDeleted,
    Possession,
    PossessionDeleted,
)


class TestAddPossessionsMultipleV1UseCase:
    """Tests for AddPossessionsMultipleV1UseCase."""

    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Create a mock repository."""
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository: Mock) -> AddPossessionsMultipleV1UseCase:
        """Create AddPossessionsMultipleV1UseCase with mocked repository."""
        return AddPossessionsMultipleV1UseCase(mock_repository)

    def test_add_possessions_multiple_v1(
        self, use_case: AddPossessionsMultipleV1UseCase, mock_repository: Mock
    ) -> None:
        """Test adding multiple possessions."""
        mock_response = AddPossessionsMultipleV1Response(
            possessions=[
                Possession(
                    id="possession_1",
                    user_id="user_1",
                    volume_id="volume_1",
                    created_at=datetime.now(),
                )
            ],
            follow_editions=[
                FollowEdition(
                    id="follow_1",
                    user_id="user_1",
                    edition_id="edition_1",
                    following=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            ],
        )
        mock_repository.add_possessions_multiple_v1.return_value = mock_response

        volume_ids = ["volume_1"]
        response = use_case(volume_ids)

        assert response == mock_response
        mock_repository.add_possessions_multiple_v1.assert_called_once_with(volume_ids)

    def test_add_possessions_multiple_v1_empty_list(
        self, use_case: AddPossessionsMultipleV1UseCase, mock_repository: Mock
    ) -> None:
        """Test adding possessions with empty list."""
        mock_response = AddPossessionsMultipleV1Response(
            possessions=[],
            follow_editions=[],
        )
        mock_repository.add_possessions_multiple_v1.return_value = mock_response

        volume_ids: list[str] = []
        response = use_case(volume_ids)

        assert len(response.possessions) == 0
        assert len(response.follow_editions) == 0


class TestDeletePossessionsMultipleV1UseCase:
    """Tests for DeletePossessionsMultipleV1UseCase."""

    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Create a mock repository."""
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository: Mock) -> DeletePossessionsMultipleV1UseCase:
        """Create DeletePossessionsMultipleV1UseCase with mocked repository."""
        return DeletePossessionsMultipleV1UseCase(mock_repository)

    def test_delete_possessions_multiple_v1(
        self, use_case: DeletePossessionsMultipleV1UseCase, mock_repository: Mock
    ) -> None:
        """Test deleting multiple possessions."""
        mock_response = DeletePossessionsMultipleV1Response(
            possessions=[
                PossessionDeleted(id="possession_1", deleted=True),
            ],
            follow_editions=[
                FollowEditionDeleted(id="follow_1", deleted=True),
            ],
            loans=[
                LoanDeleted(id="loan_1", deleted=True),
            ],
        )
        mock_repository.delete_possessions_multiple_v1.return_value = mock_response

        possession_ids = ["possession_1"]
        response = use_case(possession_ids)

        assert response == mock_response
        mock_repository.delete_possessions_multiple_v1.assert_called_once_with(possession_ids)

    def test_delete_possessions_multiple_v1_no_loans(
        self, use_case: DeletePossessionsMultipleV1UseCase, mock_repository: Mock
    ) -> None:
        """Test deleting possessions without associated loans."""
        mock_response = DeletePossessionsMultipleV1Response(
            possessions=[
                PossessionDeleted(id="possession_1", deleted=True),
            ],
            follow_editions=[
                FollowEditionDeleted(id="follow_1", deleted=True),
            ],
            loans=[],
        )
        mock_repository.delete_possessions_multiple_v1.return_value = mock_response

        possession_ids = ["possession_1"]
        response = use_case(possession_ids)

        assert len(response.loans) == 0
