"""Tests pour InMemoryAuthorRepository.

This module contains unit tests for the InMemory Author repository.
"""

import pytest

from src.domain.entities import Author, AuthorListItem
from src.domain.execptions.author_exceptions import AuthorNotFoundException
from src.infrastructure.repositories.memory.in_memory_author_repository import \
    InMemoryAuthorRepository


class TestInMemoryAuthorRepository:
    """Tests pour InMemoryAuthorRepository."""

    @pytest.fixture
    def repository(self) -> InMemoryAuthorRepository:
        """Fixture pour créer un repository en mémoire."""
        return InMemoryAuthorRepository()

    @pytest.fixture
    def sample_author(self) -> Author:
        """Fixture pour créer un auteur de test."""
        return Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

    def test_add_and_get_by_id(self, repository: InMemoryAuthorRepository, sample_author: Author) -> None:
        """Test d'ajout et récupération d'un auteur."""
        repository.add(sample_author)

        result = repository.get_by_id_v2("370ac96c-49e0-4f09-b7c4-662cb1374b21")

        assert len(result.authors) == 1
        author = result.authors[0]
        assert author == sample_author
        assert author.name == "Kishimoto"
        # Vérifier que les listes sont vides pour InMemory
        assert result.tasks == []
        assert result.jobs == []
        assert result.series == []
        assert result.editions == []
        assert result.volumes == []

    def test_get_by_id_not_found(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération d'un auteur inexistant."""
        with pytest.raises(AuthorNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_all_empty(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération avec repository vide."""
        result = repository.get_all_v2()

        assert result.authors == []

    def test_get_all_multiple_authors(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération de plusieurs auteurs."""
        author1 = Author(id="id1", name="Name1", first_name="First1", tasks_count=10)
        author2 = Author(id="id2", name="Name2", first_name=None, tasks_count=20)
        author3 = Author(id="id3", name="Name3", first_name="First3", tasks_count=30)

        repository.add(author1)
        repository.add(author2)
        repository.add(author3)

        result = repository.get_all_v2()

        assert len(result.authors) == 3
        assert author1 in result.authors
        assert author2 in result.authors
        assert author3 in result.authors

    def test_get_list_empty(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération de la liste simplifiée avec repository vide."""
        items = repository.get_list()

        assert items == []

    def test_get_list_with_authors(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération de la liste simplifiée."""
        author1 = Author(id="id1", name="Kishimoto", first_name="Masashi", tasks_count=10)
        author2 = Author(id="id2", name="Boichi", first_name=None, tasks_count=20)

        repository.add(author1)
        repository.add(author2)

        items = repository.get_list()

        assert len(items) == 2
        assert all(isinstance(item, AuthorListItem) for item in items)

        kishimoto = next(item for item in items if item.id == "id1")
        assert kishimoto.full_name == "Masashi Kishimoto"

        boichi = next(item for item in items if item.id == "id2")
        assert boichi.full_name == "Boichi"

    def test_clear(self, repository: InMemoryAuthorRepository) -> None:
        """Test du nettoyage du repository."""
        author = Author(id="test-id", name="Test", first_name="Author", tasks_count=1)
        repository.add(author)

        assert len(repository.get_all_v2().authors) == 1

        repository.clear()

        assert len(repository.get_all_v2().authors) == 0
