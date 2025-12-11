"""Use cases pour la ressource Offer.

This module contains all use cases for Offer operations.
"""

from mangacollec.domain.entities import AmazonOffer, BDFugueOffer
from mangacollec.domain.repositories import IOfferRepository


class GetAmazonOfferV1UseCase:
    """Cas d'utilisation : récupérer une offre Amazon par ASIN."""

    def __init__(self, repository: IOfferRepository) -> None:
        self.repository = repository

    def __call__(self, volume_asin: str) -> AmazonOffer:
        """Exécute le use case.

        Args:
            volume_asin: ASIN du volume Amazon

        Returns:
            AmazonOffer

        Raises:
            AmazonOfferNotFoundException: Si l'offre n'existe pas
        """
        response = self.repository.get_amazon_offer_v1(volume_asin)
        return response.amazon_offers[0]


class GetBDFugueOfferV1UseCase:
    """Cas d'utilisation : récupérer une offre BDFugue par ISBN."""

    def __init__(self, repository: IOfferRepository) -> None:
        self.repository = repository

    def __call__(self, volume_isbn: str) -> BDFugueOffer:
        """Exécute le use case.

        Args:
            volume_isbn: ISBN du volume

        Returns:
            BDFugueOffer

        Raises:
            BDFugueOfferNotFoundException: Si l'offre n'existe pas
        """
        response = self.repository.get_bdfugue_offer_v1(volume_isbn)
        return response.bdfugue_offers[0]
