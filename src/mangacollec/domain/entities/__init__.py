"""Domain entities package."""

__all__ = [
    "AmazonOffer",
    "Author",
    "AuthorListItem",
    "BDFugueOffer",
    "Box",
    "BoxEdition",
    "BoxVolume",
    "ClientMangaCollec",
    "Edition",
    "FollowEdition",
    "Job",
    "Kind",
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
from mangacollec.domain.entities.box_volume import BoxVolume
from mangacollec.domain.entities.client import ClientMangaCollec
from mangacollec.domain.entities.edition import Edition
from mangacollec.domain.entities.follow_edition import FollowEdition
from mangacollec.domain.entities.job import Job
from mangacollec.domain.entities.kind import Kind
from mangacollec.domain.entities.offer import AmazonOffer, BDFugueOffer
from mangacollec.domain.entities.publisher import Publisher, PublisherListItem
from mangacollec.domain.entities.serie import Serie
from mangacollec.domain.entities.task import Task
from mangacollec.domain.entities.type import TypeSerie
from mangacollec.domain.entities.volume import Volume
