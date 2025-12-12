"""Tests for ReadMapper."""

from datetime import datetime, timezone

from mangacollec.application.dto import (CreateReadsMultipleV1Response,
                                         DeleteReadsMultipleV1Response)
from mangacollec.application.mappers import ReadMapper
from mangacollec.domain.entities import (Read, ReadDeleted, ReadEdition,
                                         ReadEditionDeleted)


class TestReadMapperFromDict:
    """Tests for ReadMapper.from_read_dict()."""

    def test_from_read_dict(self) -> None:
        """Test converting API dict to Read entity."""
        api_data = {
            "id": "read_123",
            "user_id": "user_456",
            "volume_id": "volume_789",
            "created_at": "2024-12-11T10:30:00Z",
        }

        read = ReadMapper.from_read_dict(api_data)

        assert read.id == "read_123"
        assert read.user_id == "user_456"
        assert read.volume_id == "volume_789"
        assert read.created_at.year == 2024
        assert read.created_at.month == 12
        assert read.created_at.day == 11

    def test_from_read_edition_dict(self) -> None:
        """Test converting API dict to ReadEdition entity."""
        api_data = {
            "id": "read_edition_123",
            "user_id": "user_456",
            "edition_id": "edition_789",
            "reading": True,
            "created_at": "2024-12-11T10:30:00Z",
        }

        read_edition = ReadMapper.from_read_edition_dict(api_data)

        assert read_edition.id == "read_edition_123"
        assert read_edition.user_id == "user_456"
        assert read_edition.edition_id == "edition_789"
        assert read_edition.reading is True
        assert read_edition.created_at.year == 2024

    def test_from_read_deleted_dict(self) -> None:
        """Test converting API dict to ReadDeleted entity."""
        api_data = {
            "id": "read_123",
            "deleted": True,
        }

        read_deleted = ReadMapper.from_read_deleted_dict(api_data)

        assert read_deleted.id == "read_123"
        assert read_deleted.deleted is True

    def test_from_read_edition_deleted_dict(self) -> None:
        """Test converting API dict to ReadEditionDeleted entity."""
        api_data = {
            "id": "read_edition_123",
            "deleted": True,
        }

        read_edition_deleted = ReadMapper.from_read_edition_deleted_dict(api_data)

        assert read_edition_deleted.id == "read_edition_123"
        assert read_edition_deleted.deleted is True


class TestReadMapperToDict:
    """Tests for ReadMapper.to_*_dict() methods."""

    def test_to_read_dict(self) -> None:
        """Test converting Read entity to dict."""
        read = Read(
            id="read_123",
            user_id="user_456",
            volume_id="volume_789",
            created_at=datetime(2024, 12, 11, 10, 30, 0, tzinfo=timezone.utc),
        )

        result = ReadMapper.to_read_dict(read)

        assert result["id"] == "read_123"
        assert result["user_id"] == "user_456"
        assert result["volume_id"] == "volume_789"
        assert "2024-12-11" in result["created_at"]

    def test_to_read_edition_dict(self) -> None:
        """Test converting ReadEdition entity to dict."""
        read_edition = ReadEdition(
            id="read_edition_123",
            edition_id="edition_456",
            user_id="user_789",
            reading=True,
            created_at=datetime(2024, 12, 11, 10, 30, 0, tzinfo=timezone.utc),
        )

        result = ReadMapper.to_read_edition_dict(read_edition)

        assert result["id"] == "read_edition_123"
        assert result["edition_id"] == "edition_456"
        assert result["user_id"] == "user_789"
        assert result["reading"] is True
        assert "2024-12-11" in result["created_at"]

    def test_to_read_deleted_dict(self) -> None:
        """Test converting ReadDeleted entity to dict."""
        read_deleted = ReadDeleted(id="read_123", deleted=True)

        result = ReadMapper.to_read_deleted_dict(read_deleted)

        assert result["id"] == "read_123"
        assert result["deleted"] is True

    def test_to_read_edition_deleted_dict(self) -> None:
        """Test converting ReadEditionDeleted entity to dict."""
        read_edition_deleted = ReadEditionDeleted(id="read_edition_123", deleted=True)

        result = ReadMapper.to_read_edition_deleted_dict(read_edition_deleted)

        assert result["id"] == "read_edition_123"
        assert result["deleted"] is True


class TestReadMapperResponseConversion:
    """Tests for ReadMapper response conversion methods."""

    def test_from_create_reads_response(self) -> None:
        """Test converting API create response to CreateReadsMultipleV1Response."""
        api_response = {
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

        response = ReadMapper.from_create_reads_response(api_response)

        assert isinstance(response, CreateReadsMultipleV1Response)
        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[1].id == "read_2"
        assert response.read_editions[0].id == "read_edition_1"
        assert response.read_editions[1].id == "read_edition_2"

    def test_from_create_reads_response_empty(self) -> None:
        """Test converting empty API create response."""
        api_response = {"reads": [], "read_editions": []}

        response = ReadMapper.from_create_reads_response(api_response)

        assert isinstance(response, CreateReadsMultipleV1Response)
        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_from_delete_reads_response(self) -> None:
        """Test converting API delete response to DeleteReadsMultipleV1Response."""
        api_response = {
            "reads": [
                {"id": "read_1", "deleted": True},
                {"id": "read_2", "deleted": True},
            ],
            "read_editions": [
                {"id": "read_edition_1", "deleted": True},
                {"id": "read_edition_2", "deleted": True},
            ],
        }

        response = ReadMapper.from_delete_reads_response(api_response)

        assert isinstance(response, DeleteReadsMultipleV1Response)
        assert len(response.reads) == 2
        assert len(response.read_editions) == 2
        assert response.reads[0].id == "read_1"
        assert response.reads[0].deleted is True
        assert response.reads[1].id == "read_2"
        assert response.reads[1].deleted is True
        assert response.read_editions[0].id == "read_edition_1"
        assert response.read_editions[0].deleted is True
        assert response.read_editions[1].id == "read_edition_2"
        assert response.read_editions[1].deleted is True

    def test_from_delete_reads_response_partial_failure(self) -> None:
        """Test converting API delete response with partial failures."""
        api_response = {
            "reads": [
                {"id": "read_1", "deleted": True},
                {"id": "read_2", "deleted": False},
            ],
            "read_editions": [
                {"id": "read_edition_1", "deleted": True},
            ],
        }

        response = ReadMapper.from_delete_reads_response(api_response)

        assert isinstance(response, DeleteReadsMultipleV1Response)
        assert len(response.reads) == 2
        assert len(response.read_editions) == 1
        assert response.reads[0].deleted is True
        assert response.reads[1].deleted is False

    def test_from_delete_reads_response_empty(self) -> None:
        """Test converting empty API delete response."""
        api_response = {"reads": [], "read_editions": []}

        response = ReadMapper.from_delete_reads_response(api_response)

        assert isinstance(response, DeleteReadsMultipleV1Response)
        assert len(response.reads) == 0
        assert len(response.read_editions) == 0
