"""Response DTOs pour User.

This module contains response DTOs for User operations.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import Edition, Serie, UserCollection, Volume


@dataclass(frozen=True)
class GetUserCollectionByUsernameV2Response:
    """Réponse pour GetUserCollectionByUsernameV2."""

    editions: list[Edition]
    series: list[Serie]


@dataclass(frozen=True)
class GetMeCollectionV2Response:
    """Réponse pour GetMeCollectionV2."""

    user_collection: UserCollection
    editions: list[Edition]
    series: list[Serie]


@dataclass(frozen=True)
class GetMeRecommendationsV1Response:
    """Réponse pour GetMeRecommendationsV1."""

    volumes: list[Volume]
