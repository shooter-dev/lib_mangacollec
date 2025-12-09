"""Domain entities package."""

__all__ = [
    "Author",
    "AuthorListItem",
    "Box",
    "BoxEdition",
    "ClientMangaCollec",
    "Edition",
    "Job",
    "Publisher",
    "PublisherListItem",
    "Serie",
    "Task",
    "TypeSerie",
    "Volume",
]

from mangacollec.domain.entities.author import Author, AuthorListItem
from mangacollec.domain.entities.box import Box
from mangacollec.domain.entities.box_edition import BoxEdition
from mangacollec.domain.entities.client import ClientMangaCollec
from mangacollec.domain.entities.edition import Edition
from mangacollec.domain.entities.job import Job
from mangacollec.domain.entities.publisher import Publisher, PublisherListItem
from mangacollec.domain.entities.serie import Serie
from mangacollec.domain.entities.task import Task
from mangacollec.domain.entities.type import TypeSerie
from mangacollec.domain.entities.volume import Volume
