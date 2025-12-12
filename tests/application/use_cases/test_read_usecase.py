"""Tests for Read use cases."""

import pytest

from mangacollec.application.use_cases import (CreateReadsMultipleV1UseCase,
                                               DeleteReadsMultipleV1UseCase)
from mangacollec.infrastructure.repositories import InMemoryReadRepository


class TestCreateReadsMultipleV1UseCase:
    """Tests for CreateReadsMultipleV1UseCase."""

    @pytest.fixture
    def repository(self) -> InMemoryReadRepository:
        """Create a fresh InMemoryReadRepository for each test."""
        return InMemoryReadRepository()

    @pytest.fixture
    def use_case(self, repository: InMemoryReadRepository) -> CreateReadsMultipleV1UseCase:
        """Create CreateReadsMultipleV1UseCase with repository."""
        return CreateReadsMultipleV1UseCase(repository)

    def test_create_single_read(
        self, use_case: CreateReadsMultipleV1UseCase, repository: InMemoryReadRepository
    ) -> None:
        """Test creating a single read."""
        volume_ids = ["volume_123"]

        response = use_case(volume_ids)

        assert len(response.reads) == 1
        assert len(response.read_editions) == 1
        assert response.reads[0].volume_id == "volume_123"
        assert response.reads[0].user_id == "test_user"
        assert response.read_editions[0].reading is True

    def test_create_multiple_reads(
        self, use_case: CreateReadsMultipleV1UseCase, repository: InMemoryReadRepository
    ) -> None:
        """Test creating multiple reads."""
        volume_ids = ["volume_1", "volume_2", "volume_3"]

        response = use_case(volume_ids)

        assert len(response.reads) == 3
        assert len(response.read_editions) == 3
        assert response.reads[0].volume_id == "volume_1"
        assert response.reads[1].volume_id == "volume_2"
        assert response.reads[2].volume_id == "volume_3"

    def test_create_reads_empty_list(
        self, use_case: CreateReadsMultipleV1UseCase, repository: InMemoryReadRepository
    ) -> None:
        """Test creating reads with empty volume list."""
        volume_ids: list[str] = []

        response = use_case(volume_ids)

        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_create_reads_increments_ids(
        self, use_case: CreateReadsMultipleV1UseCase, repository: InMemoryReadRepository
    ) -> None:
        """Test that IDs are incremented correctly."""
        volume_ids = ["volume_1", "volume_2"]

        response = use_case(volume_ids)

        # Les IDs doivent être incrémentés
        assert response.reads[0].id == "1"
        assert response.reads[1].id == "2"
        assert response.read_editions[0].id == "1"
        assert response.read_editions[1].id == "2"


class TestDeleteReadsMultipleV1UseCase:
    """Tests for DeleteReadsMultipleV1UseCase."""

    @pytest.fixture
    def repository(self) -> InMemoryReadRepository:
        """Create a fresh InMemoryReadRepository for each test."""
        return InMemoryReadRepository()

    @pytest.fixture
    def use_case(self, repository: InMemoryReadRepository) -> DeleteReadsMultipleV1UseCase:
        """Create DeleteReadsMultipleV1UseCase with repository."""
        return DeleteReadsMultipleV1UseCase(repository)

    def test_delete_existing_read(
        self,
        use_case: DeleteReadsMultipleV1UseCase,
        repository: InMemoryReadRepository,
    ) -> None:
        """Test deleting an existing read."""
        # Créer d'abord des lectures
        create_use_case = CreateReadsMultipleV1UseCase(repository)
        create_response = create_use_case(["volume_1"])
        read_id = create_response.reads[0].id

        # Supprimer
        response = use_case([read_id])

        assert len(response.reads) == 1
        assert len(response.read_editions) == 1
        assert response.reads[0].id == read_id
        assert response.reads[0].deleted is True
        assert response.read_editions[0].deleted is True

    def test_delete_multiple_reads(
        self,
        use_case: DeleteReadsMultipleV1UseCase,
        repository: InMemoryReadRepository,
    ) -> None:
        """Test deleting multiple reads."""
        # Créer d'abord des lectures
        create_use_case = CreateReadsMultipleV1UseCase(repository)
        create_response = create_use_case(["volume_1", "volume_2", "volume_3"])
        read_ids = [read.id for read in create_response.reads]

        # Supprimer
        response = use_case(read_ids)

        assert len(response.reads) == 3
        assert len(response.read_editions) == 3
        assert all(read.deleted for read in response.reads)

    def test_delete_nonexistent_read(
        self,
        use_case: DeleteReadsMultipleV1UseCase,
        repository: InMemoryReadRepository,
    ) -> None:
        """Test deleting a non-existent read."""
        read_ids = ["nonexistent_id"]

        response = use_case(read_ids)

        # Le repository InMemory retourne deleted=False pour les IDs inexistants
        assert len(response.reads) == 1
        assert response.reads[0].id == "nonexistent_id"
        assert response.reads[0].deleted is False

    def test_delete_empty_list(
        self,
        use_case: DeleteReadsMultipleV1UseCase,
        repository: InMemoryReadRepository,
    ) -> None:
        """Test deleting with empty ID list."""
        read_ids: list[str] = []

        response = use_case(read_ids)

        assert len(response.reads) == 0
        assert len(response.read_editions) == 0

    def test_delete_mixed_existing_and_nonexistent(
        self,
        use_case: DeleteReadsMultipleV1UseCase,
        repository: InMemoryReadRepository,
    ) -> None:
        """Test deleting a mix of existing and non-existent reads."""
        # Créer une lecture
        create_use_case = CreateReadsMultipleV1UseCase(repository)
        create_response = create_use_case(["volume_1"])
        existing_id = create_response.reads[0].id

        # Supprimer avec un mélange d'IDs
        read_ids = [existing_id, "nonexistent_id"]
        response = use_case(read_ids)

        assert len(response.reads) == 2
        # Premier devrait être supprimé
        assert response.reads[0].id == existing_id
        assert response.reads[0].deleted is True
        # Second devrait échouer
        assert response.reads[1].id == "nonexistent_id"
        assert response.reads[1].deleted is False
