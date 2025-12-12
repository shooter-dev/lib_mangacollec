"""Tests pour les use cases Offer."""

import pytest

from mangacollec.application.use_cases import GetAmazonOfferV1UseCase, GetBDFugueOfferV1UseCase
from mangacollec.domain.entities import AmazonOffer, BDFugueOffer
from mangacollec.domain.exceptions import AmazonOfferNotFoundException, BDFugueOfferNotFoundException
from mangacollec.infrastructure.repositories import InMemoryOfferRepository


class TestGetAmazonOfferV1UseCase:
    """Tests pour GetAmazonOfferV1UseCase."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository vide."""
        return InMemoryOfferRepository()

    @pytest.fixture
    def use_case(self, repository):
        """Fixture pour créer le use case."""
        return GetAmazonOfferV1UseCase(repository)

    @pytest.fixture
    def sample_amazon_offer(self):
        """Fixture pour créer une offre Amazon de test."""
        return AmazonOffer(
            asin="2380712956",
            formatted_price="7,30 €",
            availability="En stock",
            merchant="Expédié et vendu par Amazon.",
            store_link="https://www.amazon.fr/dp/2380712956",
        )

    def test_get_amazon_offer_v1_success(self, use_case, repository, sample_amazon_offer):
        """Test de récupération d'une offre Amazon existante."""
        repository.add_amazon(sample_amazon_offer)

        result = use_case("2380712956")

        assert isinstance(result, AmazonOffer)
        assert result.asin == "2380712956"
        assert result.formatted_price == "7,30 €"
        assert result.availability == "En stock"
        assert result.merchant == "Expédié et vendu par Amazon."

    def test_get_amazon_offer_v1_not_found(self, use_case):
        """Test de récupération d'une offre Amazon inexistante."""
        with pytest.raises(AmazonOfferNotFoundException) as exc_info:
            use_case("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_get_amazon_offer_v1_with_optional_fields_none(self, use_case, repository):
        """Test de récupération d'une offre Amazon avec champs optionnels None."""
        offer = AmazonOffer(
            asin="2380712956",
            formatted_price=None,
            availability=None,
            merchant="Expédié et vendu par Amazon.",
            store_link="https://www.amazon.fr/dp/2380712956",
        )
        repository.add_amazon(offer)

        result = use_case("2380712956")

        assert result.formatted_price is None
        assert result.availability is None


class TestGetBDFugueOfferV1UseCase:
    """Tests pour GetBDFugueOfferV1UseCase."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository vide."""
        return InMemoryOfferRepository()

    @pytest.fixture
    def use_case(self, repository):
        """Fixture pour créer le use case."""
        return GetBDFugueOfferV1UseCase(repository)

    @pytest.fixture
    def sample_bdfugue_offer(self):
        """Fixture pour créer une offre BDFugue de test."""
        return BDFugueOffer(
            id="9782380712957",
            formatted_price="7,30 €",
            availability="En stock !",
            merchant="Expédié et vendu par BDfugue.",
            store_link="https://www.bdfugue.com/spy-x-family-tome-8",
        )

    def test_get_bdfugue_offer_v1_success(self, use_case, repository, sample_bdfugue_offer):
        """Test de récupération d'une offre BDFugue existante."""
        repository.add_bdfugue(sample_bdfugue_offer)

        result = use_case("9782380712957")

        assert isinstance(result, BDFugueOffer)
        assert result.id == "9782380712957"
        assert result.formatted_price == "7,30 €"
        assert result.availability == "En stock !"
        assert result.merchant == "Expédié et vendu par BDfugue."

    def test_get_bdfugue_offer_v1_not_found(self, use_case):
        """Test de récupération d'une offre BDFugue inexistante."""
        with pytest.raises(BDFugueOfferNotFoundException) as exc_info:
            use_case("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_get_bdfugue_offer_v1_with_optional_fields_none(self, use_case, repository):
        """Test de récupération d'une offre BDFugue avec champs optionnels None."""
        offer = BDFugueOffer(
            id="9782380712957",
            formatted_price=None,
            availability=None,
            merchant="Expédié et vendu par BDfugue.",
            store_link="https://www.bdfugue.com/test",
        )
        repository.add_bdfugue(offer)

        result = use_case("9782380712957")

        assert result.formatted_price is None
        assert result.availability is None
