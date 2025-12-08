"""Tests for the PublisherMapper."""

from src.application.mappers.publisher_mapper import PublisherMapper
from src.domain.entities.publisher import Publisher, PublisherListItem


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