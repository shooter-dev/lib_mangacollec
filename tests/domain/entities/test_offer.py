"""Tests pour les entités AmazonOffer et BDFugueOffer.

This module contains unit tests for AmazonOffer and BDFugueOffer entities.
"""

import pytest

from mangacollec.domain.entities import AmazonOffer, BDFugueOffer


class TestAmazonOffer:
    """Tests pour l'entité AmazonOffer."""

    def test_create_amazon_offer_with_all_fields(self) -> None:
        """Test de création d'une offre Amazon avec tous les champs."""
        offer = AmazonOffer(
            asin="2380712956",
            formatted_price="7,30 €",
            availability="En stock",
            merchant="Expédié et vendu par Amazon.",
            store_link="https://www.amazon.fr/dp/2380712956?tag=manga-web-21",
        )

        assert offer.asin == "2380712956"
        assert offer.formatted_price == "7,30 €"
        assert offer.availability == "En stock"
        assert offer.merchant == "Expédié et vendu par Amazon."
        assert offer.store_link == "https://www.amazon.fr/dp/2380712956?tag=manga-web-21"

    def test_create_amazon_offer_with_optional_fields_none(self) -> None:
        """Test de création d'une offre Amazon avec champs optionnels None."""
        offer = AmazonOffer(
            asin="2380712956",
            formatted_price=None,
            availability=None,
            merchant="Expédié et vendu par Amazon.",
            store_link="https://www.amazon.fr/dp/2380712956",
        )

        assert offer.asin == "2380712956"
        assert offer.formatted_price is None
        assert offer.availability is None
        assert offer.merchant == "Expédié et vendu par Amazon."
        assert offer.store_link == "https://www.amazon.fr/dp/2380712956"

    def test_amazon_offer_is_frozen(self) -> None:
        """Test que l'entité AmazonOffer est immuable."""
        offer = AmazonOffer(
            asin="test-asin",
            formatted_price="10 €",
            availability="En stock",
            merchant="Test",
            store_link="https://test.com",
        )

        with pytest.raises(AttributeError):
            offer.asin = "new-asin"


class TestBDFugueOffer:
    """Tests pour l'entité BDFugueOffer."""

    def test_create_bdfugue_offer_with_all_fields(self) -> None:
        """Test de création d'une offre BDFugue avec tous les champs."""
        offer = BDFugueOffer(
            id="9782380712957",
            formatted_price="7,30 €",
            availability="En stock !",
            merchant="Expédié et vendu par BDfugue.",
            store_link="https://www.bdfugue.com/spy-x-family-tome-8?ref=358",
        )

        assert offer.id == "9782380712957"
        assert offer.formatted_price == "7,30 €"
        assert offer.availability == "En stock !"
        assert offer.merchant == "Expédié et vendu par BDfugue."
        assert offer.store_link == "https://www.bdfugue.com/spy-x-family-tome-8?ref=358"

    def test_create_bdfugue_offer_with_optional_fields_none(self) -> None:
        """Test de création d'une offre BDFugue avec champs optionnels None."""
        offer = BDFugueOffer(
            id="9782380712957",
            formatted_price=None,
            availability=None,
            merchant="Expédié et vendu par BDfugue.",
            store_link="https://www.bdfugue.com/test",
        )

        assert offer.id == "9782380712957"
        assert offer.formatted_price is None
        assert offer.availability is None
        assert offer.merchant == "Expédié et vendu par BDfugue."
        assert offer.store_link == "https://www.bdfugue.com/test"

    def test_bdfugue_offer_is_frozen(self) -> None:
        """Test que l'entité BDFugueOffer est immuable."""
        offer = BDFugueOffer(
            id="test-isbn",
            formatted_price="10 €",
            availability="En stock",
            merchant="Test",
            store_link="https://test.com",
        )

        with pytest.raises(AttributeError):
            offer.id = "new-isbn"
