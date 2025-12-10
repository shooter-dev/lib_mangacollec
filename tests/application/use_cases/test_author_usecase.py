"""Tests pour les use cases Author.

This module contains unit tests for Author use cases.
"""

import pytest

from mangacollec.application.dto import SearchAuthor
from mangacollec.application.use_cases import (GetAllAuthorUseCase,
                                               GetByIdAuthorUseCase,
                                               GetListAuthorUseCase,
                                               SearchAuthorUseCase)
from mangacollec.domain.entities import Author, AuthorListItem
from mangacollec.domain.exceptions import AuthorNotFoundException
from mangacollec.infrastructure.repositories import InMemoryAuthorRepository


@pytest.fixture
def repository() -> InMemoryAuthorRepository:
    """Fixture pour créer un repository en mémoire."""
    return InMemoryAuthorRepository()


@pytest.fixture
def sample_authors(repository: InMemoryAuthorRepository) -> list[Author]:
    """Fixture pour créer des auteurs de test."""
    authors = [
        Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        ),
        Author(
            id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
            name="Boichi",
            first_name=None,
            tasks_count=14,
        ),
        Author(
            id="123e4567-e89b-12d3-a456-426614174000",
            name="Oda",
            first_name="Eiichiro",
            tasks_count=45,
        ),
    ]

    for author in authors:
        repository.add(author)

    return authors


class TestGetByIdAuthorUseCase:
    """Tests pour GetByIdAuthorUseCase."""

    def test_get_existing_author(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de récupération d'un auteur existant avec toutes ses relations."""
        usecase = GetByIdAuthorUseCase(repository)

        author, tasks, jobs, series, editions, volumes = usecase("370ac96c-49e0-4f09-b7c4-662cb1374b21")

        assert isinstance(author, Author)
        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        # Vérifier que les listes sont vides (InMemory repository)
        assert tasks == []
        assert jobs == []
        assert series == []
        assert editions == []
        assert volumes == []

    def test_get_nonexistent_author(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération d'un auteur inexistant."""
        usecase = GetByIdAuthorUseCase(repository)

        with pytest.raises(AuthorNotFoundException) as exc_info:
            usecase("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)


class TestGetAllAuthorUseCase:
    """Tests pour GetAllAuthorUseCase."""

    def test_get_all_authors(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de récupération de tous les auteurs."""
        usecase = GetAllAuthorUseCase(repository)

        result = usecase()

        assert len(result) == 3
        assert all(isinstance(author, Author) for author in result)

    def test_get_all_authors_empty(self, repository: InMemoryAuthorRepository) -> None:
        """Test de récupération avec repository vide."""
        usecase = GetAllAuthorUseCase(repository)

        result = usecase()

        assert result == []


class TestGetListAuthorUseCase:
    """Tests pour GetListAuthorUseCase."""

    def test_get_list_authors(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de récupération de la liste simplifiée."""
        usecase = GetListAuthorUseCase(repository)

        items = usecase()

        assert len(items) == 3
        assert all(isinstance(item, AuthorListItem) for item in items)

        kishimoto = next(item for item in items if item.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21")
        assert kishimoto.full_name == "Masashi Kishimoto"

        boichi = next(item for item in items if item.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108")
        assert boichi.full_name == "Boichi"


class TestSearchAuthorUseCase:
    """Tests pour SearchAuthorUseCase."""

    def test_search_by_name(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de recherche par nom (case insensitive)."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(name="oda")

        results = usecase(criteria, sample_authors)

        assert len(results) == 1
        assert results[0].name == "Oda"

    def test_search_by_first_name(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de recherche par prénom."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(first_name="masashi")

        results = usecase(criteria, sample_authors)

        assert len(results) == 1
        assert results[0].first_name == "Masashi"

    def test_search_by_min_tasks_count(
        self, repository: InMemoryAuthorRepository, sample_authors: list[Author]
    ) -> None:
        """Test de recherche par nombre minimum de tâches."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(min_tasks_count=30)

        results = usecase(criteria, sample_authors)

        assert len(results) == 2
        assert all(author.tasks_count >= 30 for author in results)

    def test_search_by_max_tasks_count(
        self, repository: InMemoryAuthorRepository, sample_authors: list[Author]
    ) -> None:
        """Test de recherche par nombre maximum de tâches."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(max_tasks_count=20)

        results = usecase(criteria, sample_authors)

        assert len(results) == 1
        assert results[0].name == "Boichi"

    def test_search_no_results(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de recherche sans résultats."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(name="NonExistent")

        results = usecase(criteria, sample_authors)

        assert results == []

    def test_search_multiple_criteria(self, repository: InMemoryAuthorRepository, sample_authors: list[Author]) -> None:
        """Test de recherche avec plusieurs critères."""
        usecase = SearchAuthorUseCase()
        criteria = SearchAuthor(name="kishimoto", min_tasks_count=30)

        results = usecase(criteria, sample_authors)

        assert len(results) == 1
        assert results[0].name == "Kishimoto"
        assert results[0].tasks_count >= 30
