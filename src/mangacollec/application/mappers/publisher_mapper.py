"""Publisher mapper."""

from mangacollec.application.dto.publisher_responses import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
from mangacollec.application.mappers.box_edition_mapper import BoxEditionMapper
from mangacollec.application.mappers.box_mapper import BoxMapper
from mangacollec.application.mappers.serie_mapper import SerieMapper
from mangacollec.application.mappers.type_mapper import TypeSerieMapper
from mangacollec.application.mappers.volume_mapper import VolumeMapper
from mangacollec.domain.entities import Publisher, PublisherListItem


class PublisherMapper:
    """Publisher mapper."""

    @staticmethod
    def from_dict(data: dict) -> Publisher:
        """
        Convert a dictionary to a Publisher entity.

        Args:
            data: The dictionary to convert.

        Returns:
            A Publisher entity.
        """
        return Publisher(
            id=data["id"],
            title=data["title"],
            closed=data["closed"],
            editions_count=data["editions_count"],
            no_amazon=data["no_amazon"],
        )

    @staticmethod
    def to_dict(publisher: Publisher) -> dict:
        """
        Convert a Publisher entity to a dictionary.

        Args:
            publisher: The Publisher entity to convert.

        Returns:
            A dictionary representing the Publisher.
        """
        return {
            "id": publisher.id,
            "title": publisher.title,
            "closed": publisher.closed,
            "editions_count": publisher.editions_count,
            "no_amazon": publisher.no_amazon,
        }

    @staticmethod
    def to_list_item(publisher: Publisher) -> PublisherListItem:
        """
        Convert a Publisher entity to a PublisherListItem.

        Args:
            publisher: The Publisher entity to convert.

        Returns:
            A PublisherListItem entity.
        """
        return PublisherListItem(
            id=publisher.id,
            title=publisher.title,
        )

    @staticmethod
    def from_all_publishers_response(
        response: dict,
    ) -> GetAllPublishersV2Response:
        """
        Convert the API response for get_all to GetAllPublishersV2Response.

        Args:
            response: The API response.

        Returns:
            A GetAllPublishersV2Response.
        """
        return GetAllPublishersV2Response(
            publishers=[PublisherMapper.from_dict(publisher) for publisher in response.get("publishers", [])]
        )

    @staticmethod
    def from_api_response(response: dict) -> GetPublisherByIdV2Response:
        """
        Convert the API response to GetPublisherByIdV2Response.

        Args:
            response: The API response.

        Returns:
            A GetPublisherByIdV2Response.
        """
        from mangacollec.application.mappers.edition_mapper import EditionMapper

        return GetPublisherByIdV2Response(
            publishers=[PublisherMapper.from_dict(publisher) for publisher in response.get("publishers", [])],
            editions=[EditionMapper.from_dict(edition) for edition in response.get("editions", [])],
            box_editions=[BoxEditionMapper.from_dict(box_edition) for box_edition in response.get("box_editions", [])],
            series=[SerieMapper.from_dict(serie) for serie in response.get("series", [])],
            types=[TypeSerieMapper.from_dict(type) for type in response.get("types", [])],
            volumes=[VolumeMapper.from_dict(volume) for volume in response.get("volumes", [])],
            boxes=[BoxMapper.from_dict(box) for box in response.get("boxes", [])],
        )
