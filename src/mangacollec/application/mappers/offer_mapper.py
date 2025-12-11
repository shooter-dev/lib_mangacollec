"""Mapper pour la conversion entre les réponses API et les entités Offer.

This module provides mapping functions between API responses and Offer entities.
"""

from mangacollec.application.dto import (GetAmazonOfferV1Response,
                                         GetBDFugueOfferV1Response)
from mangacollec.domain.entities import AmazonOffer, BDFugueOffer


class OfferMapper:
    """Mapper pour convertir entre API et entités du domaine Offer."""

    @staticmethod
    def from_dict_amazon(data: dict) -> AmazonOffer:
        """Convertit la réponse API en entité AmazonOffer.

        Args:
            data: Dictionnaire contenant les données de l'API Amazon

        Returns:
            Entité AmazonOffer
        """
        return AmazonOffer(
            asin=data["asin"],
            formatted_price=data.get("formatted_price"),
            availability=data.get("availability"),
            merchant=data["merchant"],
            store_link=data["store_link"],
        )

    @staticmethod
    def from_dict_bdfugue(data: dict) -> BDFugueOffer:
        """Convertit la réponse API en entité BDFugueOffer.

        Args:
            data: Dictionnaire contenant les données de l'API BDFugue

        Returns:
            Entité BDFugueOffer
        """
        return BDFugueOffer(
            id=data["id"],
            formatted_price=data.get("formatted_price"),
            availability=data.get("availability"),
            merchant=data["merchant"],
            store_link=data["store_link"],
        )

    @staticmethod
    def to_dict_amazon(offer: AmazonOffer) -> dict:
        """Convertit l'entité AmazonOffer en dictionnaire.

        Args:
            offer: Entité AmazonOffer

        Returns:
            Dictionnaire représentant l'offre Amazon
        """
        return {
            "asin": offer.asin,
            "formatted_price": offer.formatted_price,
            "availability": offer.availability,
            "merchant": offer.merchant,
            "store_link": offer.store_link,
        }

    @staticmethod
    def to_dict_bdfugue(offer: BDFugueOffer) -> dict:
        """Convertit l'entité BDFugueOffer en dictionnaire.

        Args:
            offer: Entité BDFugueOffer

        Returns:
            Dictionnaire représentant l'offre BDFugue
        """
        return {
            "id": offer.id,
            "formatted_price": offer.formatted_price,
            "availability": offer.availability,
            "merchant": offer.merchant,
            "store_link": offer.store_link,
        }

    @staticmethod
    def from_amazon_offer_response(response: dict) -> GetAmazonOfferV1Response:
        """Convertit la réponse de l'API V1 pour Amazon offer en GetAmazonOfferV1Response.

        Args:
            response: Réponse API contenant l'offre Amazon (objet unique)

        Returns:
            GetAmazonOfferV1Response contenant l'offre dans une liste
        """
        amazon_offer = OfferMapper.from_dict_amazon(response)
        return GetAmazonOfferV1Response(amazon_offers=[amazon_offer])

    @staticmethod
    def from_bdfugue_offer_response(response: dict) -> GetBDFugueOfferV1Response:
        """Convertit la réponse de l'API V1 pour BDFugue offer en GetBDFugueOfferV1Response.

        Args:
            response: Réponse API contenant l'offre BDFugue (objet unique)

        Returns:
            GetBDFugueOfferV1Response contenant l'offre dans une liste
        """
        bdfugue_offer = OfferMapper.from_dict_bdfugue(response)
        return GetBDFugueOfferV1Response(bdfugue_offers=[bdfugue_offer])
