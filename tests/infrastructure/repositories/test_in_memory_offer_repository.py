"""Tests pour InMemoryOfferRepository."""

import pytest

from mangacollec.domain.entities import AmazonOffer, BDFugueOffer
from mangacollec.domain.exceptions import (
    AmazonOfferNotFoundException,
    BDFugueOfferNotFoundException,
)
from mangacollec.infrastructure.repositories import InMemoryOfferRepository


class TestInMemoryOfferRepositoryAmazon:
    """Tests pour les opérations Amazon du repository."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository vide."""
        return InMemoryOfferRepository()

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

    def test_get_amazon_offer_v1_success(self, repository, sample_amazon_offer):
        """Test de récupération d'une offre Amazon existante."""
        repository.add_amazon(sample_amazon_offer)

        response = repository.get_amazon_offer_v1("2380712956")

        assert len(response.amazon_offers) == 1
        assert response.amazon_offers[0].asin == "2380712956"
        assert response.amazon_offers[0].formatted_price == "7,30 €"

    def test_get_amazon_offer_v1_not_found(self, repository):
        """Test de récupération d'une offre Amazon inexistante."""
        with pytest.raises(AmazonOfferNotFoundException) as exc_info:
            repository.get_amazon_offer_v1("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_add_amazon(self, repository, sample_amazon_offer):
        """Test d'ajout d'une offre Amazon."""
        result = repository.add_amazon(sample_amazon_offer)

        assert result == sample_amazon_offer
        response = repository.get_amazon_offer_v1("2380712956")
        assert len(response.amazon_offers) == 1


class TestInMemoryOfferRepositoryBDFugue:
    """Tests pour les opérations BDFugue du repository."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository vide."""
        return InMemoryOfferRepository()

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

    def test_get_bdfugue_offer_v1_success(self, repository, sample_bdfugue_offer):
        """Test de récupération d'une offre BDFugue existante."""
        repository.add_bdfugue(sample_bdfugue_offer)

        response = repository.get_bdfugue_offer_v1("9782380712957")

        assert len(response.bdfugue_offers) == 1
        assert response.bdfugue_offers[0].id == "9782380712957"
        assert response.bdfugue_offers[0].formatted_price == "7,30 €"

    def test_get_bdfugue_offer_v1_not_found(self, repository):
        """Test de récupération d'une offre BDFugue inexistante."""
        with pytest.raises(BDFugueOfferNotFoundException) as exc_info:
            repository.get_bdfugue_offer_v1("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_add_bdfugue(self, repository, sample_bdfugue_offer):
        """Test d'ajout d'une offre BDFugue."""
        result = repository.add_bdfugue(sample_bdfugue_offer)

        assert result == sample_bdfugue_offer
        response = repository.get_bdfugue_offer_v1("9782380712957")
        assert len(response.bdfugue_offers) == 1


class TestInMemoryOfferRepositoryClear:
    """Tests pour la méthode clear du repository."""

    @pytest.fixture
    def repository(self):
        """Fixture pour créer un repository vide."""
        return InMemoryOfferRepository()

    def test_clear(self, repository):
        """Test du nettoyage du repository."""
        amazon_offer = AmazonOffer(
            asin="test1",
            formatted_price=None,
            availability=None,
            merchant="Test",
            store_link="https://test.com",
        )
        bdfugue_offer = BDFugueOffer(
            id="test2",
            formatted_price=None,
            availability=None,
            merchant="Test",
            store_link="https://test.com",
        )

        repository.add_amazon(amazon_offer)
        repository.add_bdfugue(bdfugue_offer)
        repository.clear()

        with pytest.raises(AmazonOfferNotFoundException):
            repository.get_amazon_offer_v1("test1")

        with pytest.raises(BDFugueOfferNotFoundException):
            repository.get_bdfugue_offer_v1("test2")
