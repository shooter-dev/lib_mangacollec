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
    "FollowEditionDeleted",
    "Job",
    "Kind",
    "LoanDeleted",
    "NativeAdVolumeHomeFirst",
    "Possession",
    "PossessionDeleted",
    "Publisher",
    "PublisherListItem",
    "Read",
    "ReadDeleted",
    "ReadEdition",
    "ReadEditionDeleted",
    "Serie",
    "SerieListItem",
    "Task",
    "TypeSerie",
    "Volume",
    "User",
    "UserCollection",
]

from mangacollec.domain.entities.author import Author, AuthorListItem
from mangacollec.domain.entities.box import Box
from mangacollec.domain.entities.box_edition import BoxEdition
from mangacollec.domain.entities.box_volume import BoxVolume
from mangacollec.domain.entities.client import ClientMangaCollec
from mangacollec.domain.entities.edition import Edition
from mangacollec.domain.entities.follow_edition import FollowEdition
from mangacollec.domain.entities.follow_edition_deleted import FollowEditionDeleted
from mangacollec.domain.entities.job import Job
from mangacollec.domain.entities.kind import Kind
from mangacollec.domain.entities.loan import LoanDeleted
from mangacollec.domain.entities.native_ad_volume_home_first import (
    NativeAdVolumeHomeFirst,
)
from mangacollec.domain.entities.offer import AmazonOffer, BDFugueOffer
from mangacollec.domain.entities.possession import Possession, PossessionDeleted
from mangacollec.domain.entities.publisher import Publisher, PublisherListItem
from mangacollec.domain.entities.read import (
    Read,
    ReadDeleted,
    ReadEdition,
    ReadEditionDeleted,
)
from mangacollec.domain.entities.serie import Serie, SerieListItem
from mangacollec.domain.entities.task import Task
from mangacollec.domain.entities.type import TypeSerie
from mangacollec.domain.entities.user import User, UserCollection
from mangacollec.domain.entities.volume import Volume
