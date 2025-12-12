"""Publisher repository interface."""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
from mangacollec.domain.entities.publisher import PublisherListItem


class IPublisherRepository(ABC):
    """Publisher repository interface."""

    @abstractmethod
    def get_all_v2(self) -> GetAllPublishersV2Response:
        """
        Get all publishers.

        Returns:
            A GetAllPublishersV2Response.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id_v2(self, publisher_id: str) -> GetPublisherByIdV2Response:
        """
        Get a publisher by its id.

        Args:
            publisher_id: The id of the publisher.

        Returns:
            A GetPublisherByIdV2Response.
        """
        raise NotImplementedError

    @abstractmethod
    def get_list(self) -> list[PublisherListItem]:
        """
        Get a list of all publishers.

        Returns:
            A list of PublisherListItem.
        """
        raise NotImplementedError
