"""Tests for Possession response DTOs."""

from datetime import datetime

from mangacollec.application.dto import (AddPossessionsMultipleV1Response,
                                         DeletePossessionsMultipleV1Response)
from mangacollec.domain.entities import (FollowEdition, FollowEditionDeleted,
                                         LoanDeleted, Possession,
                                         PossessionDeleted)


class TestAddPossessionsMultipleV1Response:
    """Tests for AddPossessionsMultipleV1Response."""

    def test_creation(self) -> None:
        """Test creating AddPossessionsMultipleV1Response."""
        possessions = [
            Possession(
                id="possession_1",
                user_id="user_1",
                volume_id="volume_1",
                created_at=datetime.now(),
            )
        ]
        follow_editions = [
            FollowEdition(
                id="follow_1",
                user_id="user_1",
                edition_id="edition_1",
                following=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        ]

        response = AddPossessionsMultipleV1Response(
            possessions=possessions,
            follow_editions=follow_editions,
        )

        assert response.possessions == possessions
        assert response.follow_editions == follow_editions

    def test_creation_empty(self) -> None:
        """Test creating AddPossessionsMultipleV1Response with empty lists."""
        response = AddPossessionsMultipleV1Response(
            possessions=[],
            follow_editions=[],
        )

        assert len(response.possessions) == 0
        assert len(response.follow_editions) == 0


class TestDeletePossessionsMultipleV1Response:
    """Tests for DeletePossessionsMultipleV1Response."""

    def test_creation(self) -> None:
        """Test creating DeletePossessionsMultipleV1Response."""
        possessions = [
            PossessionDeleted(id="possession_1", deleted=True),
        ]
        follow_editions = [
            FollowEditionDeleted(id="follow_1", deleted=True),
        ]
        loans = [
            LoanDeleted(id="loan_1", deleted=True),
        ]

        response = DeletePossessionsMultipleV1Response(
            possessions=possessions,
            follow_editions=follow_editions,
            loans=loans,
        )

        assert response.possessions == possessions
        assert response.follow_editions == follow_editions
        assert response.loans == loans

    def test_creation_no_loans(self) -> None:
        """Test creating DeletePossessionsMultipleV1Response without loans."""
        possessions = [
            PossessionDeleted(id="possession_1", deleted=True),
        ]
        follow_editions = [
            FollowEditionDeleted(id="follow_1", deleted=True),
        ]

        response = DeletePossessionsMultipleV1Response(
            possessions=possessions,
            follow_editions=follow_editions,
            loans=[],
        )

        assert len(response.loans) == 0
