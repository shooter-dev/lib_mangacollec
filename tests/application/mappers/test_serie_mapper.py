"""Tests pour le SerieMapper.

This module contains unit tests for the SerieMapper.
"""

import pytest

from mangacollec.application.mappers import SerieMapper
from mangacollec.domain.entities import Serie, SerieListItem


class TestSerieMapper:
    """Tests pour le mapper Serie."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en Serie."""
        data = {
            "id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            "title": "Naruto",
            "type_id": "e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            "adult_content": False,
            "editions_count": 12,
            "tasks_count": 5,
            "kinds_ids": ["kind-1", "kind-2"],
        }

        serie = SerieMapper.from_dict(data)

        assert isinstance(serie, Serie)
        assert serie.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert serie.title == "Naruto"
        assert serie.type_id == "e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d"
        assert serie.adult_content is False
        assert serie.editions_count == 12
        assert serie.tasks_count == 5
        assert serie.kinds_ids == ["kind-1", "kind-2"]

    def test_from_dict_without_kinds_ids(self) -> None:
        """Test de conversion sans kinds_ids."""
        data = {
            "id": "test-id",
            "title": "One Piece",
            "type_id": "type-id",
            "adult_content": False,
            "editions_count": 25,
            "tasks_count": 3,
        }

        serie = SerieMapper.from_dict(data)

        assert serie.id == "test-id"
        assert serie.title == "One Piece"
        assert serie.type_id == "type-id"
        assert serie.adult_content is False
        assert serie.editions_count == 25
        assert serie.tasks_count == 3
        assert serie.kinds_ids is None

    def test_from_dict_with_adult_content(self) -> None:
        """Test de conversion avec contenu adulte."""
        data = {
            "id": "test-id",
            "title": "Adult Serie",
            "type_id": "type-id",
            "adult_content": True,
            "editions_count": 5,
            "tasks_count": 2,
        }

        serie = SerieMapper.from_dict(data)

        assert serie.adult_content is True

    def test_to_dict(self) -> None:
        """Test de conversion d'une Serie en dictionnaire."""
        serie = Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
            type_id="e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1", "kind-2"],
        )

        result = SerieMapper.to_dict(serie)

        assert result == {
            "id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            "title": "Naruto",
            "type_id": "e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            "adult_content": False,
            "editions_count": 12,
            "tasks_count": 5,
            "kinds_ids": ["kind-1", "kind-2"],
        }

    def test_to_dict_with_none_kinds_ids(self) -> None:
        """Test de conversion d'une Serie sans kinds_ids."""
        serie = Serie(
            id="test-id",
            title="Test Serie",
            type_id="type-id",
            adult_content=False,
            editions_count=1,
            tasks_count=1,
            kinds_ids=None,
        )

        result = SerieMapper.to_dict(serie)

        assert result["kinds_ids"] is None

    def test_to_list_item(self) -> None:
        """Test de conversion d'une Serie en SerieListItem."""
        serie = Serie(
            id="39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
            title="Naruto",
            type_id="e88e8bae-05f0-4c6f-a3fb-7e3e0b3a7e0d",
            adult_content=False,
            editions_count=12,
            tasks_count=5,
            kinds_ids=["kind-1"],
        )

        item = SerieMapper.to_list_item(serie)

        assert isinstance(item, SerieListItem)
        assert item.id == "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e"
        assert item.title == "Naruto"

    def test_from_all_series_response(self) -> None:
        """Test de conversion de la réponse get_all."""
        response = {
            "series": [
                {
                    "id": "id1",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 12,
                    "tasks_count": 5,
                    "kinds_ids": ["kind-1"],
                },
                {
                    "id": "id2",
                    "title": "One Piece",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 25,
                    "tasks_count": 3,
                },
            ],
            "types": [
                {"id": "type-1", "title": "Manga", "to_display": True},
            ],
        }

        result = SerieMapper.from_all_series_response(response)

        assert len(result.series) == 2
        assert result.series[0].title == "Naruto"
        assert result.series[0].kinds_ids == ["kind-1"]
        assert result.series[1].title == "One Piece"
        assert result.series[1].kinds_ids is None
        assert len(result.types) == 1
        assert result.types[0].title == "Manga"

    def test_from_all_series_response_empty(self) -> None:
        """Test de conversion de la réponse get_all vide."""
        response = {"series": [], "types": []}

        result = SerieMapper.from_all_series_response(response)

        assert result.series == []
        assert result.types == []

    def test_from_all_series_response_no_keys(self) -> None:
        """Test de conversion sans clés 'series' et 'types'."""
        response = {}

        result = SerieMapper.from_all_series_response(response)

        assert result.series == []
        assert result.types == []

    def test_from_api_response(self) -> None:
        """Test de conversion de la réponse complète get_by_id."""
        response = {
            "series": [
                {
                    "id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
                    "title": "Naruto",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 12,
                    "tasks_count": 5,
                    "kinds_ids": ["kind-1"],
                }
            ],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
            "kinds": [{"id": "kind-1", "name": "Shonen", "name_en": "Shonen"}],
            "tasks": [
                {
                    "id": "task-1",
                    "job_id": "job-1",
                    "series_id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
                    "author_id": "author-1",
                }
            ],
            "jobs": [{"id": "job-1", "title": "Auteur"}],
            "authors": [
                {
                    "id": "author-1",
                    "name": "Kishimoto",
                    "first_name": "Masashi",
                    "tasks_count": 32,
                }
            ],
            "editions": [
                {
                    "id": "edition-1",
                    "title": "Edition standard",
                    "series_id": "39c0f48b-c9f3-488d-9f01-bb9f21f30b0e",
                    "publisher_id": "publisher-1",
                    "parent_edition_id": None,
                    "volumes_count": 72,
                    "last_volume_number": 72,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 100,
                }
            ],
            "publishers": [
                {
                    "id": "publisher-1",
                    "title": "Kana",
                    "closed": False,
                    "editions_count": 200,
                    "no_amazon": False,
                }
            ],
            "volumes": [
                {
                    "id": "volume-1",
                    "title": None,
                    "number": 1,
                    "release_date": "2002-10-02",
                    "isbn": "978-2-505-00001-0",
                    "asin": "B00005XXXX",
                    "edition_id": "edition-1",
                    "possessions_count": 500,
                    "not_sold": False,
                    "image_url": "https://example.com/image.jpg",
                }
            ],
            "box_editions": [
                {
                    "id": "box-edition-1",
                    "title": "Coffret Naruto",
                    "publisher_id": "publisher-1",
                    "boxes_count": 3,
                    "adult_content": False,
                    "box_follow_editions_count": 50,
                }
            ],
            "boxes": [
                {
                    "id": "box-1",
                    "title": "Coffret 1",
                    "number": 1,
                    "release_date": "2020-01-01",
                    "isbn": "978-2-505-00002-0",
                    "asin": "B00006XXXX",
                    "commercial_stop": False,
                    "box_edition_id": "box-edition-1",
                    "box_possessions_count": 30,
                    "image_url": "https://example.com/box.jpg",
                }
            ],
            "box_volumes": [
                {
                    "id": "box-volume-1",
                    "title": "Box Volume 1",
                    "number": 1,
                    "release_date": "2020-01-01",
                    "isbn": "978-2-505-00003-0",
                    "asin": "B00007XXXX",
                    "edition_id": "edition-1",
                    "possessions_count": 15,
                    "not_sold": False,
                    "image_url": "https://example.com/box-volume-1.jpg",
                }
            ],
        }

        result = SerieMapper.from_api_response(response)

        # Vérifier les series
        assert len(result.series) == 1
        assert result.series[0].title == "Naruto"
        assert result.series[0].kinds_ids == ["kind-1"]

        # Vérifier les types
        assert len(result.types) == 1
        assert result.types[0].title == "Manga"

        # Vérifier les kinds
        assert len(result.kinds) == 1
        assert result.kinds[0].name == "Shonen"

        # Vérifier les tasks
        assert len(result.tasks) == 1
        assert result.tasks[0].id == "task-1"

        # Vérifier les jobs
        assert len(result.jobs) == 1
        assert result.jobs[0].title == "Auteur"

        # Vérifier les authors
        assert len(result.authors) == 1
        assert result.authors[0].name == "Kishimoto"

        # Vérifier les editions
        assert len(result.editions) == 1
        assert result.editions[0].title == "Edition standard"

        # Vérifier les publishers
        assert len(result.publishers) == 1
        assert result.publishers[0].title == "Kana"

        # Vérifier les volumes
        assert len(result.volumes) == 1
        assert result.volumes[0].number == 1

        # Vérifier les box_editions
        assert len(result.box_editions) == 1
        assert result.box_editions[0].title == "Coffret Naruto"

        # Vérifier les boxes
        assert len(result.boxes) == 1
        assert result.boxes[0].title == "Coffret 1"

        # Vérifier les box_volumes
        assert len(result.box_volumes) == 1
        assert result.box_volumes[0].edition_id == "edition-1"

    def test_from_api_response_empty_relations(self) -> None:
        """Test de conversion avec relations vides."""
        response = {
            "series": [
                {
                    "id": "test-id",
                    "title": "Test Serie",
                    "type_id": "type-id",
                    "adult_content": False,
                    "editions_count": 0,
                    "tasks_count": 0,
                }
            ],
            "types": [],
            "kinds": [],
            "tasks": [],
            "jobs": [],
            "authors": [],
            "editions": [],
            "publishers": [],
            "volumes": [],
            "box_editions": [],
            "boxes": [],
            "box_volumes": [],
        }

        result = SerieMapper.from_api_response(response)

        assert len(result.series) == 1
        assert result.types == []
        assert result.kinds == []
        assert result.tasks == []
        assert result.jobs == []
        assert result.authors == []
        assert result.editions == []
        assert result.publishers == []
        assert result.volumes == []
        assert result.box_editions == []
        assert result.boxes == []
        assert result.box_volumes == []

    def test_from_dict_missing_required_field(self) -> None:
        """Test de conversion avec champ requis manquant."""
        # Test avec ID manquant
        data = {
            "title": "Naruto",
            "type_id": "type-1",
            "adult_content": False,
            "editions_count": 12,
            "tasks_count": 5,
        }

        with pytest.raises(KeyError, match="id"):
            SerieMapper.from_dict(data)

    def test_from_dict_empty_required_fields(self) -> None:
        """Test de conversion avec champs requis vides."""
        data = {
            "id": "",
            "title": "Test Serie",
            "type_id": "",
            "adult_content": False,
            "editions_count": 0,
            "tasks_count": 0,
        }

        serie = SerieMapper.from_dict(data)

        assert serie.id == ""
        assert serie.title == "Test Serie"
        assert serie.type_id == ""

    def test_from_api_response_empty_series_list(self) -> None:
        """Test de conversion avec une liste de séries vide."""
        response = {
            "series": [],
            "types": [{"id": "type-1", "title": "Manga", "to_display": True}],
        }

        result = SerieMapper.from_api_response(response)

        assert len(result.series) == 0
        assert len(result.types) == 1
        assert result.types[0].title == "Manga"
