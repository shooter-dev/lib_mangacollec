"""Implémentation du repository Offer via l'API MangaCollec.

This module provides the API implementation of the Offer repository.
"""

from mangacollec.application.dto import (
    GetAmazonOfferV1Response,
    GetBDFugueOfferV1Response,
)
from mangacollec.application.interfaces import IMangaCollecAPI
from mangacollec.application.mappers import OfferMapper
from mangacollec.domain.exceptions import (
    AmazonOfferNotFoundException,
    BDFugueOfferNotFoundException,
)
from mangacollec.domain.repositories import IOfferRepository


class APIOfferRepository(IOfferRepository):
    """Implémentation du repository Offer via MangaCollecAPI V1."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_amazon_offer_v1(self, volume_asin: str) -> GetAmazonOfferV1Response:
        """Récupère une offre Amazon par ASIN via l'API.

        Args:
            volume_asin: ASIN du volume Amazon

        Returns:
            GetAmazonOfferV1Response contenant l'offre Amazon

        Raises:
            AmazonOfferNotFoundException: Si l'offre n'existe pas
        """
        try:
            response = self.client_api.get(f"/v1/amazon_offer/{volume_asin}")
            return OfferMapper.from_amazon_offer_response(response)

        except Exception as e:
            if isinstance(e, AmazonOfferNotFoundException):
                raise
            raise AmazonOfferNotFoundException(volume_asin) from e

    def get_bdfugue_offer_v1(self, volume_isbn: str) -> GetBDFugueOfferV1Response:
        """Récupère une offre BDFugue par ISBN via l'API.

        Args:
            volume_isbn: ISBN du volume

        Returns:
            GetBDFugueOfferV1Response contenant l'offre BDFugue

        Raises:
            BDFugueOfferNotFoundException: Si l'offre n'existe pas
        """
        try:
            response = self.client_api.get(f"/v1/bdfugue_offer/{volume_isbn}")
            return OfferMapper.from_bdfugue_offer_response(response)

        except Exception as e:
            if isinstance(e, BDFugueOfferNotFoundException):
                raise
            raise BDFugueOfferNotFoundException(volume_isbn) from e
