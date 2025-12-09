"""Publisher API repository."""

from mangacollec.application.dto.responses.publisher_responses import GetAllPublishersV2Response, GetPublisherByIdV2Response
from mangacollec.application.interfaces.mangacollec_api_interface import IMangaCollecAPI
from mangacollec.application.mappers.publisher_mapper import PublisherMapper
from mangacollec.domain.entities.publisher import PublisherListItem
from mangacollec.domain.exceptions.publisher_exceptions import PublisherNotFoundException
from mangacollec.domain.repositories.publisher_repository import IPublisherRepository


class APIPublisherRepository(IPublisherRepository):
    """Publisher API repository."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """
        Initialize the repository.

        Args:
            client_api: The MangaCollec API client.
        """
        self.client_api = client_api

    def get_all_v2(self) -> GetAllPublishersV2Response:
        """
        Get all publishers.

        Returns:
            A GetAllPublishersV2Response.
        """
        try:
            response = self.client_api.get("/v2/publishers/")
            return PublisherMapper.from_all_publishers_response(response)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve publishers: {e}") from e

    def get_by_id_v2(self, publisher_id: str) -> GetPublisherByIdV2Response:
        """
        Get a publisher by its id.

        Args:
            publisher_id: The id of the publisher.

        Returns:
            A GetPublisherByIdV2Response.
        """
        try:
            response = self.client_api.get(f"/v2/publishers/{publisher_id}")

            if not response.get("publishers") or len(response["publishers"]) == 0:
                raise PublisherNotFoundException(publisher_id)

            return PublisherMapper.from_api_response(response)

        except Exception as e:
            if isinstance(e, PublisherNotFoundException):
                raise
            raise PublisherNotFoundException(publisher_id) from e

    def get_list(self) -> list[PublisherListItem]:
        """
        Get a list of all publishers.

        Returns:
            A list of PublisherListItem.
        """
        all_publishers_response = self.get_all_v2()
        return [PublisherMapper.to_list_item(publisher) for publisher in all_publishers_response.publishers]
