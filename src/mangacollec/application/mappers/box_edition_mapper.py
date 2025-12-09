"""BoxEdition mapper."""

from mangacollec.domain.entities import BoxEdition


class BoxEditionMapper:
    """BoxEdition mapper."""

    @staticmethod
    def from_dict(data: dict) -> BoxEdition:
        """
        Convert a dictionary to a BoxEdition entity.

        Args:
            data: The dictionary to convert.

        Returns:
            A BoxEdition entity.
        """
        return BoxEdition(
            id=data["id"],
            title=data.get("title"),
            publisher_id=data["publisher_id"],
            boxes_count=data["boxes_count"],
            adult_content=data["adult_content"],
            box_follow_editions_count=data["box_follow_editions_count"],
        )
