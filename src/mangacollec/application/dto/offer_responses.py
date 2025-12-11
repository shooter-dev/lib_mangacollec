"""Response DTOs pour Offer.

This module contains response DTOs for Offer operations.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import AmazonOffer, BDFugueOffer


@dataclass(frozen=True)
class GetAmazonOfferV1Response:
    """Réponse pour GetAmazonOfferV1."""

    amazon_offers: list[AmazonOffer]


@dataclass(frozen=True)
class GetBDFugueOfferV1Response:
    """Réponse pour GetBDFugueOfferV1."""

    bdfugue_offers: list[BDFugueOffer]
