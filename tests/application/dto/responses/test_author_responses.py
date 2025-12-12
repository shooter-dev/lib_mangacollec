"""Tests pour les DTOs de réponse Author.

This module contains unit tests for Author response DTOs.
"""

import pytest

from mangacollec.application.dto import (GetAllAuthorsV2Response,
                                         GetAuthorByIdV2Response)
from mangacollec.domain.entities import (Author, Edition, Job, Serie, Task,
                                         Volume)


class TestGetAllAuthorsV2Response:
    """Tests pour GetAllAuthorsV2Response."""

    def test_create_get_all_authors_response(self) -> None:
        """Test de création d'une réponse avec des auteurs."""
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
        ]

        response = GetAllAuthorsV2Response(authors=authors)

        assert len(response.authors) == 2
        assert response.authors[0].name == "Kishimoto"
        assert response.authors[1].name == "Boichi"

    def test_create_get_all_authors_response_empty(self) -> None:
        """Test de création d'une réponse vide."""
        response = GetAllAuthorsV2Response(authors=[])

        assert response.authors == []

    def test_get_all_authors_response_is_frozen(self) -> None:
        """Test que la réponse est immuable."""
        authors = [
            Author(
                id="test-id",
                name="Test",
                first_name="Author",
                tasks_count=1,
            )
        ]
        response = GetAllAuthorsV2Response(authors=authors)

        with pytest.raises(AttributeError):
            response.authors = []


class TestGetAuthorByIdV2Response:
    """Tests pour GetAuthorByIdV2Response."""

    def test_create_get_author_by_id_response(self) -> None:
        """Test de création d'une réponse complète avec toutes les relations."""
        authors = [
            Author(
                id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
                name="Kishimoto",
                first_name="Masashi",
                tasks_count=32,
            )
        ]

        tasks = [
            Task(
                id="task-1",
                job_id="job-1",
                series_id="series-1",
                author_id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
            )
        ]

        jobs = [Job(id="job-1", title="Auteur")]

        series = [
            Serie(
                id="series-1",
                title="Naruto",
                type_id="type-1",
                adult_content=False,
                editions_count=7,
                tasks_count=1,
            )
        ]

        editions = [
            Edition(
                id="edition-1",
                title="Edition Collector",
                series_id="series-1",
                publisher_id="publisher-1",
                parent_edition_id=None,
                volumes_count=72,
                last_volume_number=72,
                commercial_stop=False,
                not_finished=False,
                follow_editions_count=1443,
            )
        ]

        volumes = [
            Volume(
                id="volume-1",
                title=None,
                number=1,
                release_date="2002-03-01",
                isbn="9782012345678",
                asin="2012345678",
                edition_id="edition-1",
                possessions_count=100,
                not_sold=False,
                image_url="https://example.com/image.jpg",
                nb_pages=None,
                content=None,
            )
        ]

        response = GetAuthorByIdV2Response(
            authors=authors,
            tasks=tasks,
            jobs=jobs,
            series=series,
            editions=editions,
            volumes=volumes,
        )

        # Vérifier l'auteur
        assert len(response.authors) == 1
        assert response.authors[0].name == "Kishimoto"
        assert response.authors[0].first_name == "Masashi"

        # Vérifier les tasks
        assert len(response.tasks) == 1
        assert response.tasks[0].id == "task-1"

        # Vérifier les jobs
        assert len(response.jobs) == 1
        assert response.jobs[0].title == "Auteur"

        # Vérifier les series
        assert len(response.series) == 1
        assert response.series[0].title == "Naruto"

        # Vérifier les editions
        assert len(response.editions) == 1
        assert response.editions[0].title == "Edition Collector"

        # Vérifier les volumes
        assert len(response.volumes) == 1
        assert response.volumes[0].number == 1

    def test_create_get_author_by_id_response_empty_relations(self) -> None:
        """Test de création d'une réponse avec des relations vides."""
        authors = [
            Author(
                id="test-id",
                name="Test",
                first_name=None,
                tasks_count=0,
            )
        ]

        response = GetAuthorByIdV2Response(
            authors=authors,
            tasks=[],
            jobs=[],
            series=[],
            editions=[],
            volumes=[],
        )

        assert len(response.authors) == 1
        assert response.tasks == []
        assert response.jobs == []
        assert response.series == []
        assert response.editions == []
        assert response.volumes == []

    def test_get_author_by_id_response_is_frozen(self) -> None:
        """Test que la réponse est immuable."""
        authors = [
            Author(
                id="test-id",
                name="Test",
                first_name="Author",
                tasks_count=1,
            )
        ]
        response = GetAuthorByIdV2Response(
            authors=authors,
            tasks=[],
            jobs=[],
            series=[],
            editions=[],
            volumes=[],
        )

        with pytest.raises(AttributeError):
            response.authors = []

        with pytest.raises(AttributeError):
            response.tasks = []

        with pytest.raises(AttributeError):
            response.jobs = []
