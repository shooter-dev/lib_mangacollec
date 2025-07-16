import datetime
from typing import List, Dict

from mangacollec_api.core.interfaces.entity import Entity

class Volume(Entity):
    id: str
    title: str | None
    number: str
    release_date: datetime
    isbn: str | None
    asin: str | None
    edition_id: str
    possessions_count: int
    not_sold: bool
    image_url: str

    def __init__(
        self,
        id: str,
        title: str | None,
        number: str,
        release_date: datetime,
        isbn: str | None,
        asin: str | None,
        edition_id: str,
        possessions_count: int,
        not_sold: bool,
        image_url: str,
    ):
        self.id: str = id
        self.title: str | None = title
        self.number: str = number
        self.release_date: datetime = release_date
        self.isbn: str | None = isbn
        self.asin: str | None = asin
        self.edition_id: str = edition_id
        self.possessions_count: int = possessions_count
        self.not_sold: bool = not_sold
        self.image_url: str = image_url

    def to_dict(self) -> Dict[str, any]:
        return {
            "id": self.id,
            "title": self.title,
            "number": self.number,
            "release_date": self.release_date,
            "isbn": self.isbn,
            "asin": self.asin,
            "edition_id": self.edition_id,
            "possessions_count": self.possessions_count,
            "not_sold": self.not_sold,
            "image_url": self.image_url,
        }

    def __srt__(self):
        return self.title

    def __repr__(self):
        return self.id
