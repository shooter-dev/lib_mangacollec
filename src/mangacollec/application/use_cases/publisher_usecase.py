"""Publisher use cases."""

from mangacollec.application.dto.publisher_responses import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
from mangacollec.domain.entities.publisher import PublisherListItem
from mangacollec.domain.repositories.publisher_repository_interface import (
    IPublisherRepository,
)


class GetAllPublishersV2UseCase:
    """Get all publishers use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(self) -> GetAllPublishersV2Response:
        """
        Execute the use case.

        Returns:
            A GetAllPublishersV2Response.
        """
        return self.repository.get_all_v2()


class GetPublisherByIdV2UseCase:
    """Get publisher by id use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(self, publisher_id: str) -> GetPublisherByIdV2Response:
        """
        Execute the use case.

        Args:
            publisher_id: The id of the publisher.

        Returns:
            A GetPublisherByIdV2Response.
        """
        return self.repository.get_by_id_v2(publisher_id)


class GetListPublishersUseCase:
    """Get list publishers use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(self) -> list[PublisherListItem]:
        """
        Execute the use case.

        Returns:
            A list of PublisherListItem.
        """
        return self.repository.get_list()
