"""Tests for Read response DTOs."""

from datetime import datetime, timezone

import pytest

from mangacollec.application.dto import (
    CreateReadsMultipleV1Response,
    DeleteReadsMultipleV1Response,
)
from mangacollec.domain.entities import (
    Read,
    ReadDeleted,
    ReadEdition,
    ReadEditionDeleted,
)


class TestCreateReadsMultipleV1Response:
    """Tests for CreateReadsMultipleV1Response DTO."""

    def test_create_response_with_data(self) -> None:
        """Test creating response with reads and read_editions."""
        reads = [
            Read(
                id="read_1",
                user_id="user_123",
                volume_id="volume_1",
                created_at=datetime.now(timezone.utc),
            ),
            Read(
                id="read_2",
                user_id="user_123",
                volume_id="volume_2",
                created_at=datetime.now(timezone.utc),
            ),
        ]
        read_editions = [
            ReadEdition(
                id="read_edition_1",
                edition_id="edition_1",
                user_id="user_123",
                reading=True,
                created_at=datetime.now(timezone.utc),
            ),
            ReadEdition(
                id="read_edition_2",
                edition_id="edition_2",
                user_id="user_123",
                reading=True,
                created_at=datetime.now(timezone.utc),
            ),
        ]

        response = CreateReadsMultipleV1Response(reads=reads, read_editions=read_editions)

        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[1].id == "read_2"
        assert response.read_editions[0].id == "read_edition_1"
        assert response.read_editions[1].id == "read_edition_2"

    def test_create_response_empty(self) -> None:
        """Test creating response with empty lists."""
        response = CreateReadsMultipleV1Response(reads=[], read_editions=[])

        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_create_response_is_frozen(self) -> None:
        """Test that CreateReadsMultipleV1Response is immutable."""
        response = CreateReadsMultipleV1Response(reads=[], read_editions=[])

        with pytest.raises(AttributeError):
            response.reads = []  # type: ignore


class TestDeleteReadsMultipleV1Response:
    """Tests for DeleteReadsMultipleV1Response DTO."""

    def test_delete_response_with_data(self) -> None:
        """Test creating response with deleted reads and read_editions."""
        reads = [
            ReadDeleted(id="read_1", deleted=True),
            ReadDeleted(id="read_2", deleted=True),
        ]
        read_editions = [
            ReadEditionDeleted(id="read_edition_1", deleted=True),
            ReadEditionDeleted(id="read_edition_2", deleted=True),
        ]

        response = DeleteReadsMultipleV1Response(reads=reads, read_editions=read_editions)

        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[0].deleted is True
        assert response.reads[1].id == "read_2"
        assert response.reads[1].deleted is True
        assert response.read_editions[0].id == "read_edition_1"
        assert response.read_editions[0].deleted is True

    def test_delete_response_partial_failure(self) -> None:
        """Test creating response with partial deletion failures."""
        reads = [
            ReadDeleted(id="read_1", deleted=True),
            ReadDeleted(id="read_2", deleted=False),  # Failed to delete
        ]
        read_editions = [
            ReadEditionDeleted(id="read_edition_1", deleted=True),
        ]

        response = DeleteReadsMultipleV1Response(reads=reads, read_editions=read_editions)

        assert len(response.reads) == 2
        assert response.reads[0].deleted is True
        assert response.reads[1].deleted is False
        assert len(response.read_editions) == 1

    def test_delete_response_empty(self) -> None:
        """Test creating response with empty lists."""
        response = DeleteReadsMultipleV1Response(reads=[], read_editions=[])

        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_delete_response_is_frozen(self) -> None:
        """Test that DeleteReadsMultipleV1Response is immutable."""
        response = DeleteReadsMultipleV1Response(reads=[], read_editions=[])

        with pytest.raises(AttributeError):
            response.reads = []  # type: ignore
