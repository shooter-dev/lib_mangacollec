"""Box mapper."""

from mangacollec.domain.entities.box import Box
from mangacollec.domain.value_objects.asin import ASIN
from mangacollec.domain.value_objects.isbn import ISBN
from mangacollec.domain.value_objects.url import URL


class BoxMapper:
    """Box mapper."""

    @staticmethod
    def from_dict(data: dict) -> Box:
        """
        Convert a dictionary to a Box entity.

        Args:
            data: The dictionary to convert.

        Returns:
            A Box entity.
        """
        return Box(
            id=data["id"],
            title=data.get("title"),
            number=data["number"],
            release_date=data.get("release_date"),
            isbn=ISBN(value=data["isbn"]) if data.get("isbn") else None,
            asin=ASIN(value=data["asin"]) if data.get("asin") else None,
            commercial_stop=data["commercial_stop"],
            box_edition_id=data["box_edition_id"],
            box_possessions_count=data.get("box_possessions_count"),
            image_url=URL(value=data["image_url"]) if data.get("image_url") else None,
        )
