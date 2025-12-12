"""Tests unitaires pour OfferMapper."""

import pytest

from mangacollec.application.dto import (
    GetAmazonOfferV1Response,
    GetBDFugueOfferV1Response,
)
from mangacollec.application.mappers import OfferMapper
from mangacollec.domain.entities import AmazonOffer, BDFugueOffer


class TestOfferMapperAmazon:
    """Tests pour les méthodes Amazon du mapper."""

    def test_from_dict_amazon_with_all_fields(self):
        """Test la conversion d'un dict Amazon complet en AmazonOffer."""
        data = {
            "asin": "2380712956",
            "formatted_price": "7,30 €",
            "availability": "En stock",
            "merchant": "Expédié et vendu par Amazon.",
            "store_link": "https://www.amazon.fr/dp/2380712956?tag=manga-web-21",
        }

        offer = OfferMapper.from_dict_amazon(data)

        assert isinstance(offer, AmazonOffer)
        assert offer.asin == "2380712956"
        assert offer.formatted_price == "7,30 €"
        assert offer.availability == "En stock"
        assert offer.merchant == "Expédié et vendu par Amazon."
        assert offer.store_link == "https://www.amazon.fr/dp/2380712956?tag=manga-web-21"

    def test_from_dict_amazon_with_optional_fields_none(self):
        """Test la conversion d'un dict Amazon avec champs optionnels manquants."""
        data = {
            "asin": "2380712956",
            "merchant": "Expédié et vendu par Amazon.",
            "store_link": "https://www.amazon.fr/dp/2380712956",
        }

        offer = OfferMapper.from_dict_amazon(data)

        assert isinstance(offer, AmazonOffer)
        assert offer.asin == "2380712956"
        assert offer.formatted_price is None
        assert offer.availability is None
        assert offer.merchant == "Expédié et vendu par Amazon."

    def test_to_dict_amazon(self):
        """Test la conversion d'un AmazonOffer en dictionnaire."""
        offer = AmazonOffer(
            asin="2380712956",
            formatted_price="7,30 €",
            availability="En stock",
            merchant="Expédié et vendu par Amazon.",
            store_link="https://www.amazon.fr/dp/2380712956",
        )

        result = OfferMapper.to_dict_amazon(offer)

        assert isinstance(result, dict)
        assert result["asin"] == "2380712956"
        assert result["formatted_price"] == "7,30 €"
        assert result["availability"] == "En stock"
        assert result["merchant"] == "Expédié et vendu par Amazon."
        assert result["store_link"] == "https://www.amazon.fr/dp/2380712956"

    def test_from_amazon_offer_response(self):
        """Test la conversion d'une réponse API Amazon en GetAmazonOfferV1Response."""
        response = {
            "asin": "2380712956",
            "formatted_price": "7,30 €",
            "availability": "En stock",
            "merchant": "Expédié et vendu par Amazon.",
            "store_link": "https://www.amazon.fr/dp/2380712956",
        }

        result = OfferMapper.from_amazon_offer_response(response)

        assert isinstance(result, GetAmazonOfferV1Response)
        assert len(result.amazon_offers) == 1
        assert result.amazon_offers[0].asin == "2380712956"
        assert result.amazon_offers[0].formatted_price == "7,30 €"


class TestOfferMapperBDFugue:
    """Tests pour les méthodes BDFugue du mapper."""

    def test_from_dict_bdfugue_with_all_fields(self):
        """Test la conversion d'un dict BDFugue complet en BDFugueOffer."""
        data = {
            "id": "9782380712957",
            "formatted_price": "7,30 €",
            "availability": "En stock !",
            "merchant": "Expédié et vendu par BDfugue.",
            "store_link": "https://www.bdfugue.com/spy-x-family-tome-8?ref=358",
        }

        offer = OfferMapper.from_dict_bdfugue(data)

        assert isinstance(offer, BDFugueOffer)
        assert offer.id == "9782380712957"
        assert offer.formatted_price == "7,30 €"
        assert offer.availability == "En stock !"
        assert offer.merchant == "Expédié et vendu par BDfugue."
        assert offer.store_link == "https://www.bdfugue.com/spy-x-family-tome-8?ref=358"

    def test_from_dict_bdfugue_with_optional_fields_none(self):
        """Test la conversion d'un dict BDFugue avec champs optionnels manquants."""
        data = {
            "id": "9782380712957",
            "merchant": "Expédié et vendu par BDfugue.",
            "store_link": "https://www.bdfugue.com/test",
        }

        offer = OfferMapper.from_dict_bdfugue(data)

        assert isinstance(offer, BDFugueOffer)
        assert offer.id == "9782380712957"
        assert offer.formatted_price is None
        assert offer.availability is None
        assert offer.merchant == "Expédié et vendu par BDfugue."

    def test_to_dict_bdfugue(self):
        """Test la conversion d'un BDFugueOffer en dictionnaire."""
        offer = BDFugueOffer(
            id="9782380712957",
            formatted_price="7,30 €",
            availability="En stock !",
            merchant="Expédié et vendu par BDfugue.",
            store_link="https://www.bdfugue.com/spy-x-family-tome-8",
        )

        result = OfferMapper.to_dict_bdfugue(offer)

        assert isinstance(result, dict)
        assert result["id"] == "9782380712957"
        assert result["formatted_price"] == "7,30 €"
        assert result["availability"] == "En stock !"
        assert result["merchant"] == "Expédié et vendu par BDfugue."
        assert result["store_link"] == "https://www.bdfugue.com/spy-x-family-tome-8"

    def test_from_bdfugue_offer_response(self):
        """Test la conversion d'une réponse API BDFugue en GetBDFugueOfferV1Response."""
        response = {
            "id": "9782380712957",
            "formatted_price": "7,30 €",
            "availability": "En stock !",
            "merchant": "Expédié et vendu par BDfugue.",
            "store_link": "https://www.bdfugue.com/spy-x-family-tome-8",
        }

        result = OfferMapper.from_bdfugue_offer_response(response)

        assert isinstance(result, GetBDFugueOfferV1Response)
        assert len(result.bdfugue_offers) == 1
        assert result.bdfugue_offers[0].id == "9782380712957"
        assert result.bdfugue_offers[0].formatted_price == "7,30 €"


class TestOfferMapperImmutability:
    """Tests pour l'immuabilité des entités créées."""

    def test_from_dict_amazon_immutability(self):
        """Test que l'entité AmazonOffer créée est immuable."""
        data = {
            "asin": "test",
            "merchant": "Test",
            "store_link": "https://test.com",
        }

        offer = OfferMapper.from_dict_amazon(data)

        with pytest.raises(Exception):
            offer.asin = "new"

    def test_from_dict_bdfugue_immutability(self):
        """Test que l'entité BDFugueOffer créée est immuable."""
        data = {
            "id": "test",
            "merchant": "Test",
            "store_link": "https://test.com",
        }

        offer = OfferMapper.from_dict_bdfugue(data)

        with pytest.raises(Exception):
            offer.id = "new"
