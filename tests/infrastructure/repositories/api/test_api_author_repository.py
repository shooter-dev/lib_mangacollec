"""Tests pour APIAuthorRepository.

This module contains unit tests for the API Author repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application.dto import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.domain.entities import Author, AuthorListItem, Edition, Job, Serie, Task, Volume
from mangacollec.domain.exceptions.author_exceptions import AuthorNotFoundException
from mangacollec.infrastructure.repositories import APIAuthorRepository


class TestAPIV2AuthorRepository:
    """Tests pour APIAuthorRepository."""

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> APIAuthorRepository:
        """Fixture pour créer un repository avec mock API."""
        return APIAuthorRepository(mock_api_client)

    @pytest.fixture
    def sample_author_data(self) -> dict:
        """Fixture pour créer des données d'auteur de test."""
        return {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
        }

    def test_get_by_id_success(
        self,
        repository: APIAuthorRepository,
        mock_api_client: Mock,
        sample_author_data: dict,
    ) -> None:
        """Test de récupération d'un auteur par ID avec toutes ses relations."""
        mock_api_client.get.return_value = {
            "authors": [sample_author_data],
            "tasks": [],
            "jobs": [],
            "series": [],
            "editions": [],
            "volumes": [],
        }

        result = repository.get_by_id_v2("370ac96c-49e0-4f09-b7c4-662cb1374b21")

        # Vérifier que c'est une GetAuthorByIdV2Response
        assert isinstance(result, GetAuthorByIdV2Response)

        # Vérifier l'auteur
        assert len(result.authors) == 1
        author = result.authors[0]
        assert isinstance(author, Author)
        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

        # Vérifier les listes (vides dans ce test)
        assert isinstance(result.tasks, list)
        assert isinstance(result.jobs, list)
        assert isinstance(result.series, list)
        assert isinstance(result.editions, list)
        assert isinstance(result.volumes, list)

        mock_api_client.get.assert_called_once_with("/v2/authors/370ac96c-49e0-4f09-b7c4-662cb1374b21")

    def test_get_by_id_not_found_empty_list(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de récupération d'un auteur inexistant (liste vide)."""
        mock_api_client.get.return_value = {"authors": []}

        with pytest.raises(AuthorNotFoundException) as exc_info:
            repository.get_by_id_v2("nonexistent-id")

        assert "nonexistent-id" in str(exc_info.value)

    def test_get_by_id_not_found_no_authors_key(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de récupération sans clé 'authors' dans la réponse."""
        mock_api_client.get.return_value = {}

        with pytest.raises(AuthorNotFoundException):
            repository.get_by_id_v2("test-id")

    def test_get_by_id_api_exception(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(AuthorNotFoundException):
            repository.get_by_id_v2("test-id")

    def test_get_all_success(
        self,
        repository: APIAuthorRepository,
        mock_api_client: Mock,
        sample_author_data: dict,
    ) -> None:
        """Test de récupération de tous les auteurs."""
        mock_api_client.get.return_value = {
            "authors": [
                sample_author_data,
                {
                    "id": "id2",
                    "name": "Oda",
                    "first_name": "Eiichiro",
                    "tasks_count": 45,
                },
            ]
        }

        result = repository.get_all_v2()

        assert isinstance(result, GetAllAuthorsV2Response)
        assert len(result.authors) == 2
        assert all(isinstance(author, Author) for author in result.authors)
        assert result.authors[0].name == "Kishimoto"
        assert result.authors[1].name == "Oda"

        mock_api_client.get.assert_called_once_with("/v2/authors/")

    def test_get_all_empty(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de récupération avec liste vide."""
        mock_api_client.get.return_value = {"authors": []}

        result = repository.get_all_v2()

        assert isinstance(result, GetAllAuthorsV2Response)
        assert result.authors == []

    def test_get_all_no_authors_key(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de récupération sans clé 'authors'."""
        mock_api_client.get.return_value = {}

        result = repository.get_all_v2()

        assert isinstance(result, GetAllAuthorsV2Response)
        assert result.authors == []

    def test_get_all_api_exception(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de gestion d'erreur API pour get_all."""
        mock_api_client.get.side_effect = Exception("API Error")

        with pytest.raises(RuntimeError) as exc_info:
            repository.get_all_v2()

        assert "Failed to retrieve authors" in str(exc_info.value)

    def test_get_list_success(
        self,
        repository: APIAuthorRepository,
        mock_api_client: Mock,
        sample_author_data: dict,
    ) -> None:
        """Test de récupération de la liste simplifiée."""
        mock_api_client.get.return_value = {
            "authors": [
                sample_author_data,
                {"id": "id2", "name": "Boichi", "tasks_count": 14},
            ]
        }

        items = repository.get_list()

        assert len(items) == 2
        assert all(isinstance(item, AuthorListItem) for item in items)

        kishimoto = next(item for item in items if item.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21")
        assert kishimoto.full_name == "Masashi Kishimoto"

        boichi = next(item for item in items if item.id == "id2")
        assert boichi.full_name == "Boichi"

    def test_get_by_id_without_first_name(self, repository: APIAuthorRepository, mock_api_client: Mock) -> None:
        """Test de récupération d'un auteur sans prénom."""
        author_data = {
            "id": "test-id",
            "name": "Boichi",
            "tasks_count": 14,
        }
        mock_api_client.get.return_value = {
            "authors": [author_data],
            "tasks": [],
            "jobs": [],
            "series": [],
            "editions": [],
            "volumes": [],
        }

        result = repository.get_by_id_v2("test-id")
        author = result.authors[0]

        assert author.first_name is None
        assert author.name == "Boichi"

    def test_get_by_id_with_all_relations(
        self,
        repository: APIAuthorRepository,
        mock_api_client: Mock,
        sample_author_data: dict,
    ) -> None:
        """Test de récupération d'un auteur avec toutes ses relations."""
        # Données complètes de la réponse API
        mock_api_client.get.return_value = {
            "authors": [sample_author_data],
            "tasks": [
                {
                    "id": "task-1",
                    "job_id": "job-1",
                    "series_id": "series-1",
                    "author_id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
                },
                {
                    "id": "task-2",
                    "job_id": "job-2",
                    "series_id": "series-2",
                    "author_id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
                },
            ],
            "jobs": [
                {"id": "job-1", "title": "Auteur"},
                {"id": "job-2", "title": "Auteur original"},
            ],
            "series": [
                {
                    "id": "series-1",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 7,
                    "tasks_count": 1,
                },
                {
                    "id": "series-2",
                    "title": "Boruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 2,
                    "tasks_count": 1,
                },
            ],
            "editions": [
                {
                    "id": "edition-1",
                    "title": "Edition Collector",
                    "series_id": "series-1",
                    "publisher_id": "publisher-1",
                    "parent_edition_id": None,
                    "volumes_count": 72,
                    "last_volume_number": 72,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 1443,
                }
            ],
            "volumes": [
                {
                    "id": "volume-1",
                    "title": None,
                    "number": 1,
                    "release_date": "2002-03-01",
                    "isbn": "9782012345678",
                    "asin": "2012345678",
                    "edition_id": "edition-1",
                    "possessions_count": 100,
                    "not_sold": False,
                    "image_url": "https://example.com/image.jpg",
                }
            ],
        }

        result = repository.get_by_id_v2("370ac96c-49e0-4f09-b7c4-662cb1374b21")

        # Vérifier que c'est une GetAuthorByIdV2Response
        assert isinstance(result, GetAuthorByIdV2Response)

        # Vérifier l'auteur
        assert len(result.authors) == 1
        author = result.authors[0]
        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"

        # Vérifier les tasks
        assert len(result.tasks) == 2
        assert all(isinstance(task, Task) for task in result.tasks)
        assert result.tasks[0].id == "task-1"
        assert result.tasks[0].job_id == "job-1"
        assert result.tasks[1].id == "task-2"

        # Vérifier les jobs
        assert len(result.jobs) == 2
        assert all(isinstance(job, Job) for job in result.jobs)
        assert result.jobs[0].id == "job-1"
        assert result.jobs[0].title == "Auteur"
        assert result.jobs[1].title == "Auteur original"

        # Vérifier les series
        assert len(result.series) == 2
        assert all(isinstance(serie, Serie) for serie in result.series)
        assert result.series[0].title == "Naruto"
        assert result.series[0].editions_count == 7
        assert result.series[1].title == "Boruto"

        # Vérifier les editions
        assert len(result.editions) == 1
        assert all(isinstance(edition, Edition) for edition in result.editions)
        assert result.editions[0].id == "edition-1"
        assert result.editions[0].title == "Edition Collector"
        assert result.editions[0].volumes_count == 72

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert all(isinstance(volume, Volume) for volume in result.volumes)
        assert result.volumes[0].id == "volume-1"
        assert result.volumes[0].number == 1
        assert result.volumes[0].isbn == "9782012345678"
        assert result.volumes[0].image_url == "https://example.com/image.jpg"
