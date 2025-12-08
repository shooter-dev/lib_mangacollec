"""In-memory publisher repository."""
from src.application.dto.responses.publisher_responses import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
from src.application.mappers.publisher_mapper import PublisherMapper
from src.domain.entities.publisher import Publisher, PublisherListItem
from src.domain.exceptions import PublisherNotFoundException
from src.domain.repositories.publisher_repository import IPublisherRepository


class InMemoryPublisherRepository(IPublisherRepository):
    """In-memory publisher repository."""

    def __init__(self) -> None:
        """Initialize the repository."""
        self._publishers: dict[str, Publisher] = {}

    def get_all_v2(self) -> GetAllPublishersV2Response:
        """
        Get all publishers.

        Returns:
            A GetAllPublishersV2Response.
        """
        return GetAllPublishersV2Response(
            publishers=list(self._publishers.values())
        )

    def get_by_id_v2(self, publisher_id: str) -> GetPublisherByIdV2Response:
        """
        Get a publisher by its id.

        Args:
            publisher_id: The id of the publisher.

        Returns:
            A GetPublisherByIdV2Response.
        """
        if publisher_id not in self._publishers:
            raise PublisherNotFoundException(publisher_id)

        publisher = self._publishers[publisher_id]
        return GetPublisherByIdV2Response(
            publishers=[publisher],
            editions=[],
            box_editions=[],
            series=[],
            types=[],
            volumes=[],
            boxes=[],
        )

    def get_list(self) -> list[PublisherListItem]:
        """
        Get a list of all publishers.

        Returns:
            A list of PublisherListItem.
        """
        return [
            PublisherMapper.to_list_item(publisher)
            for publisher in self._publishers.values()
        ]

    def add(self, publisher: Publisher) -> None:
        """
        Add a publisher to the repository.

        Args:
            publisher: The publisher to add.
        """
        self._publishers[publisher.id] = publisher

    def clear(self) -> None:
        """Clear the repository."""
        self._publishers.clear()
