"""Tests pour le AuthorMapper.

This module contains unit tests for the AuthorMapper.
"""

from src.application.mappers.author_mapper import AuthorMapper
from src.domain.entities import Author, AuthorListItem


class TestAuthorMapper:
    """Tests pour le mapper Author."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Author."""
        data = {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
        }

        author = AuthorMapper.from_dict(data)

        assert isinstance(author, Author)
        assert author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert author.name == "Kishimoto"
        assert author.first_name == "Masashi"
        assert author.tasks_count == 32

    def test_from_dict_without_first_name(self) -> None:
        """Test de conversion sans first_name."""
        data = {
            "id": "test-id",
            "name": "Boichi",
            "tasks_count": 14,
        }

        author = AuthorMapper.from_dict(data)

        assert author.id == "test-id"
        assert author.name == "Boichi"
        assert author.first_name is None
        assert author.tasks_count == 14

    def test_from_dict_without_tasks_count(self) -> None:
        """Test de conversion sans tasks_count (valeur par défaut)."""
        data = {
            "id": "test-id",
            "name": "Test",
            "first_name": "Author",
        }

        author = AuthorMapper.from_dict(data)

        assert author.tasks_count == 0

    def test_to_dict(self) -> None:
        """Test de conversion d'un Author en dictionnaire."""
        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

        result = AuthorMapper.to_dict(author)

        assert result == {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32,
        }

    def test_to_list_item_with_first_name(self) -> None:
        """Test de conversion d'un Author en AuthorListItem avec prénom."""
        author = Author(
            id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            name="Kishimoto",
            first_name="Masashi",
            tasks_count=32,
        )

        item = AuthorMapper.to_list_item(author)

        assert isinstance(item, AuthorListItem)
        assert item.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
        assert item.full_name == "Masashi Kishimoto"

    def test_to_list_item_without_first_name(self) -> None:
        """Test de conversion d'un Author en AuthorListItem sans prénom."""
        author = Author(
            id="test-id",
            name="Boichi",
            first_name=None,
            tasks_count=14,
        )

        item = AuthorMapper.to_list_item(author)

        assert item.id == "test-id"
        assert item.full_name == "Boichi"

    def test_from_all_authors_response(self) -> None:
        """Test de conversion de la réponse get_all."""
        response = {
            "authors": [
                {
                    "id": "id1",
                    "name": "Kishimoto",
                    "first_name": "Masashi",
                    "tasks_count": 32,
                },
                {
                    "id": "id2",
                    "name": "Boichi",
                    "tasks_count": 14,
                },
            ]
        }

        result = AuthorMapper.from_all_authors_response(response)

        assert len(result.authors) == 2
        assert result.authors[0].name == "Kishimoto"
        assert result.authors[0].first_name == "Masashi"
        assert result.authors[1].name == "Boichi"
        assert result.authors[1].first_name is None

    def test_from_all_authors_response_empty(self) -> None:
        """Test de conversion de la réponse get_all vide."""
        response = {"authors": []}

        result = AuthorMapper.from_all_authors_response(response)

        assert result.authors == []

    def test_from_all_authors_response_no_key(self) -> None:
        """Test de conversion sans clé 'authors'."""
        response = {}

        result = AuthorMapper.from_all_authors_response(response)

        assert result.authors == []

    def test_from_api_response(self) -> None:
        """Test de conversion de la réponse complète get_by_id."""
        response = {
            "authors": [
                {
                    "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
                    "name": "Kishimoto",
                    "first_name": "Masashi",
                    "tasks_count": 32,
                }
            ],
            "tasks": [
                {
                    "id": "task-1",
                    "job_id": "job-1",
                    "series_id": "series-1",
                    "author_id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
                }
            ],
            "jobs": [{"id": "job-1", "title": "Auteur"}],
            "series": [
                {
                    "id": "series-1",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 7,
                    "tasks_count": 1,
                }
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

        result = AuthorMapper.from_api_response(response)

        # Vérifier les auteurs
        assert len(result.authors) == 1
        assert result.authors[0].name == "Kishimoto"

        # Vérifier les tasks
        assert len(result.tasks) == 1
        assert result.tasks[0].id == "task-1"

        # Vérifier les jobs
        assert len(result.jobs) == 1
        assert result.jobs[0].title == "Auteur"

        # Vérifier les series
        assert len(result.series) == 1
        assert result.series[0].title == "Naruto"

        # Vérifier les editions
        assert len(result.editions) == 1
        assert result.editions[0].title == "Edition Collector"

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert result.volumes[0].number == 1

    def test_from_api_response_empty_relations(self) -> None:
        """Test de conversion avec relations vides."""
        response = {
            "authors": [
                {
                    "id": "test-id",
                    "name": "Test",
                    "first_name": None,
                    "tasks_count": 0,
                }
            ],
            "tasks": [],
            "jobs": [],
            "series": [],
            "editions": [],
            "volumes": [],
        }

        result = AuthorMapper.from_api_response(response)

        assert len(result.authors) == 1
        assert result.tasks == []
        assert result.jobs == []
        assert result.series == []
        assert result.editions == []
        assert result.volumes == []
