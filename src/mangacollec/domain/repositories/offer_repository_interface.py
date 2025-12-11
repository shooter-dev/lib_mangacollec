"""Interface du repository pour la ressource Offer.

This module defines the repository interface for Offer operations.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (GetAmazonOfferV1Response,
                                         GetBDFugueOfferV1Response)


class IOfferRepository(ABC):
    """Interface du repository pour Offer.

    Permet de récupérer les offres commerciales Amazon et BDFugue.
    Pas de create/update/delete (lecture seule).
    """

    @abstractmethod
    def get_amazon_offer_v1(self, volume_asin: str) -> GetAmazonOfferV1Response:
        """Récupère une offre Amazon par ASIN.

        Args:
            volume_asin: ASIN du volume Amazon

        Returns:
            GetAmazonOfferV1Response contenant l'offre Amazon

        Raises:
            AmazonOfferNotFoundException: Si l'offre n'existe pas
        """

    @abstractmethod
    def get_bdfugue_offer_v1(self, volume_isbn: str) -> GetBDFugueOfferV1Response:
        """Récupère une offre BDFugue par ISBN.

        Args:
            volume_isbn: ISBN du volume

        Returns:
            GetBDFugueOfferV1Response contenant l'offre BDFugue

        Raises:
            BDFugueOfferNotFoundException: Si l'offre n'existe pas
        """
