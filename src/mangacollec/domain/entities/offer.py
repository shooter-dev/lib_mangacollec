"""Entités Offer.

Cette entité représente les offres commerciales Amazon et BDFugue pour les volumes.
----------
This entity represents Amazon and BDFugue commercial offers for volumes.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Offer:
    formatted_price: str | None
    availability: str | None
    merchant: str
    store_link: str


@dataclass(frozen=True)
class AmazonOffer(Offer):
    asin: str


@dataclass(frozen=True)
class BDFugueOffer(Offer):
    id: str
