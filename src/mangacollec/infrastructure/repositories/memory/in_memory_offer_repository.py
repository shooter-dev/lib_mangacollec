"""Implémentation en mémoire du repository Offer pour les tests.

This module provides an in-memory implementation of the Offer repository for testing.
"""

from mangacollec.application.dto import (
    GetAmazonOfferV1Response,
    GetBDFugueOfferV1Response,
)
from mangacollec.domain.entities import AmazonOffer, BDFugueOffer
from mangacollec.domain.exceptions import (
    AmazonOfferNotFoundException,
    BDFugueOfferNotFoundException,
)
from mangacollec.domain.repositories import IOfferRepository


class InMemoryOfferRepository(IOfferRepository):
    """Implémentation en mémoire du repository Offer (tests/dev)."""

    def __init__(self) -> None:
        """Initialise le repository avec deux dictionnaires vides."""
        self._amazon_data: dict[str, AmazonOffer] = {}
        self._bdfugue_data: dict[str, BDFugueOffer] = {}

    def get_amazon_offer_v1(self, volume_asin: str) -> GetAmazonOfferV1Response:
        """Récupère une offre Amazon par ASIN.

        Args:
            volume_asin: ASIN du volume Amazon

        Returns:
            GetAmazonOfferV1Response contenant l'offre Amazon

        Raises:
            AmazonOfferNotFoundException: Si l'offre n'existe pas
        """
        offer = self._amazon_data.get(volume_asin)
        if offer is None:
            raise AmazonOfferNotFoundException(volume_asin)
        return GetAmazonOfferV1Response(amazon_offers=[offer])

    def get_bdfugue_offer_v1(self, volume_isbn: str) -> GetBDFugueOfferV1Response:
        """Récupère une offre BDFugue par ISBN.

        Args:
            volume_isbn: ISBN du volume

        Returns:
            GetBDFugueOfferV1Response contenant l'offre BDFugue

        Raises:
            BDFugueOfferNotFoundException: Si l'offre n'existe pas
        """
        offer = self._bdfugue_data.get(volume_isbn)
        if offer is None:
            raise BDFugueOfferNotFoundException(volume_isbn)
        return GetBDFugueOfferV1Response(bdfugue_offers=[offer])

    def add_amazon(self, offer: AmazonOffer) -> AmazonOffer:
        """Ajoute une offre Amazon au repository (méthode pour les tests).

        Args:
            offer: Entité AmazonOffer à ajouter

        Returns:
            L'entité AmazonOffer ajoutée
        """
        self._amazon_data[offer.asin] = offer
        return offer

    def add_bdfugue(self, offer: BDFugueOffer) -> BDFugueOffer:
        """Ajoute une offre BDFugue au repository (méthode pour les tests).

        Args:
            offer: Entité BDFugueOffer à ajouter

        Returns:
            L'entité BDFugueOffer ajoutée
        """
        self._bdfugue_data[offer.id] = offer
        return offer

    def clear(self) -> None:
        """Vide le repository (méthode pour les tests)."""
        self._amazon_data.clear()
        self._bdfugue_data.clear()
