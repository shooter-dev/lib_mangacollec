"""Tests for the PublisherMapper."""

from mangacollec.application.dto import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
from mangacollec.application.mappers import PublisherMapper
from mangacollec.domain.entities import (
    Edition,
    Publisher,
    PublisherListItem,
    Serie,
    TypeSerie,
    Volume,
)


class TestPublisherMapper:
    """Tests for the PublisherMapper."""

    def test_from_dict(self) -> None:
        """Test from_dict method."""
        data = {
            "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "title": "Pika",
            "closed": False,
            "editions_count": 687,
            "no_amazon": False,
        }
        publisher = PublisherMapper.from_dict(data)
        assert isinstance(publisher, Publisher)
        assert publisher.id == "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        assert publisher.title == "Pika"
        assert not publisher.closed
        assert publisher.editions_count == 687
        assert not publisher.no_amazon

    def test_to_dict(self) -> None:
        """Test to_dict method."""
        publisher = Publisher(
            id="bdef8c9e-7395-465d-8175-a1b985d4aa92",
            title="Pika",
            closed=False,
            editions_count=687,
            no_amazon=False,
        )
        data = PublisherMapper.to_dict(publisher)
        assert data == {
            "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "title": "Pika",
            "closed": False,
            "editions_count": 687,
            "no_amazon": False,
        }

    def test_to_list_item(self) -> None:
        """Test to_list_item method."""
        publisher = Publisher(
            id="bdef8c9e-7395-465d-8175-a1b985d4aa92",
            title="Pika",
            closed=False,
            editions_count=687,
            no_amazon=False,
        )
        list_item = PublisherMapper.to_list_item(publisher)
        assert isinstance(list_item, PublisherListItem)
        assert list_item.id == "bdef8c9e-7395-465d-8175-a1b985d4aa92"
        assert list_item.title == "Pika"

    def test_from_all_publishers_response(self) -> None:
        """Test from_all_publishers_response method."""
        response = {
            "publishers": [
                {
                    "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
                    "title": "Pika",
                    "closed": False,
                    "editions_count": 687,
                    "no_amazon": False,
                },
                {
                    "id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
                    "title": "Kana",
                    "closed": False,
                    "editions_count": 596,
                    "no_amazon": False,
                },
            ]
        }

        result = PublisherMapper.from_all_publishers_response(response)

        assert isinstance(result, GetAllPublishersV2Response)
        assert len(result.publishers) == 2
        assert all(isinstance(p, Publisher) for p in result.publishers)
        assert result.publishers[0].title == "Pika"
        assert result.publishers[1].title == "Kana"

    def test_from_all_publishers_response_empty(self) -> None:
        """Test from_all_publishers_response method with empty response."""
        response = {"publishers": []}

        result = PublisherMapper.from_all_publishers_response(response)

        assert isinstance(result, GetAllPublishersV2Response)
        assert len(result.publishers) == 0

    def test_from_api_response(self) -> None:
        """Test from_api_response method."""
        response = {
            "publishers": [
                {
                    "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
                    "title": "Pika",
                    "closed": False,
                    "editions_count": 687,
                    "no_amazon": False,
                }
            ],
            "editions": [
                {
                    "id": "8f59063a-8a23-40f7-af11-6c3cdb7e7242",
                    "title": None,
                    "series_id": "96142188-6709-4acf-8fb6-d3d6a077d1b1",
                    "publisher_id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
                    "parent_edition_id": None,
                    "volumes_count": 36,
                    "last_volume_number": 36,
                    "commercial_stop": False,
                    "not_finished": False,
                    "follow_editions_count": 1089,
                }
            ],
            "box_editions": [],
            "series": [
                {
                    "id": "96142188-6709-4acf-8fb6-d3d6a077d1b1",
                    "title": "One Piece",
                    "type_id": "type-1",
                    "adult_content": False,
                    "editions_count": 1,
                    "tasks_count": 0,
                }
            ],
            "types": [
                {
                    "id": "type-1",
                    "title": "Manga",
                    "to_display": True,
                }
            ],
            "volumes": [
                {
                    "id": "volume-1",
                    "title": "Volume 1",
                    "number": 1,
                    "release_date": "2023-01-01",
                    "isbn": "978-2-7234-5678-9",
                    "asin": None,
                    "edition_id": "8f59063a-8a23-40f7-af11-6c3cdb7e7242",
                    "possessions_count": 0,
                    "not_sold": False,
                    "image_url": None,
                }
            ],
            "boxes": [],
        }

        result = PublisherMapper.from_api_response(response)

        assert isinstance(result, GetPublisherByIdV2Response)
        assert len(result.publishers) == 1
        assert isinstance(result.publishers[0], Publisher)
        assert result.publishers[0].title == "Pika"
        assert len(result.editions) == 1
        assert isinstance(result.editions[0], Edition)
        assert len(result.series) == 1
        assert isinstance(result.series[0], Serie)
        assert len(result.types) == 1
        assert isinstance(result.types[0], TypeSerie)
        assert len(result.volumes) == 1
        assert isinstance(result.volumes[0], Volume)
        assert len(result.boxes) == 0
        assert len(result.box_editions) == 0

    def test_from_api_response_with_empty_lists(self) -> None:
        """Test from_api_response method with empty related entities."""
        response = {
            "publishers": [
                {
                    "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
                    "title": "Pika",
                    "closed": False,
                    "editions_count": 687,
                    "no_amazon": False,
                }
            ],
            "editions": [],
            "box_editions": [],
            "series": [],
            "types": [],
            "volumes": [],
            "boxes": [],
        }

        result = PublisherMapper.from_api_response(response)

        assert isinstance(result, GetPublisherByIdV2Response)
        assert len(result.publishers) == 1
        assert len(result.editions) == 0
        assert len(result.box_editions) == 0
        assert len(result.series) == 0
        assert len(result.types) == 0
        assert len(result.volumes) == 0
        assert len(result.boxes) == 0
