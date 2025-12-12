"""Tests pour APIOfferRepository."""

from unittest.mock import MagicMock

import pytest

from mangacollec.application.dto import (GetAmazonOfferV1Response,
                                         GetBDFugueOfferV1Response)
from mangacollec.domain.exceptions import (AmazonOfferNotFoundException,
                                           BDFugueOfferNotFoundException)
from mangacollec.infrastructure.repositories import APIOfferRepository


class TestAPIOfferRepositoryAmazon:
    """Tests pour les opérations Amazon du repository."""

    @pytest.fixture
    def mock_client_api(self):
        """Fixture pour créer un mock du client API."""
        return MagicMock()

    @pytest.fixture
    def repository(self, mock_client_api):
        """Fixture pour créer le repository avec un mock."""
        return APIOfferRepository(mock_client_api)

    def test_get_amazon_offer_v1_success(self, repository, mock_client_api):
        """Test de récupération d'une offre Amazon via l'API."""
        mock_response = {
            "asin": "2380712956",
            "formatted_price": "7,30 €",
            "availability": "En stock",
            "merchant": "Expédié et vendu par Amazon.",
            "store_link": "https://www.amazon.fr/dp/2380712956",
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_amazon_offer_v1("2380712956")

        mock_client_api.get.assert_called_once_with("/v1/amazon_offer/2380712956")
        assert isinstance(response, GetAmazonOfferV1Response)
        assert len(response.amazon_offers) == 1
        assert response.amazon_offers[0].asin == "2380712956"
        assert response.amazon_offers[0].formatted_price == "7,30 €"

    def test_get_amazon_offer_v1_not_found(self, repository, mock_client_api):
        """Test de récupération d'une offre Amazon inexistante."""
        mock_client_api.get.side_effect = Exception("Not found")

        with pytest.raises(AmazonOfferNotFoundException) as exc_info:
            repository.get_amazon_offer_v1("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_get_amazon_offer_v1_with_optional_fields_none(self, repository, mock_client_api):
        """Test de récupération d'une offre Amazon avec champs optionnels None."""
        mock_response = {
            "asin": "2380712956",
            "merchant": "Expédié et vendu par Amazon.",
            "store_link": "https://www.amazon.fr/dp/2380712956",
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_amazon_offer_v1("2380712956")

        assert isinstance(response, GetAmazonOfferV1Response)
        assert response.amazon_offers[0].formatted_price is None
        assert response.amazon_offers[0].availability is None


class TestAPIOfferRepositoryBDFugue:
    """Tests pour les opérations BDFugue du repository."""

    @pytest.fixture
    def mock_client_api(self):
        """Fixture pour créer un mock du client API."""
        return MagicMock()

    @pytest.fixture
    def repository(self, mock_client_api):
        """Fixture pour créer le repository avec un mock."""
        return APIOfferRepository(mock_client_api)

    def test_get_bdfugue_offer_v1_success(self, repository, mock_client_api):
        """Test de récupération d'une offre BDFugue via l'API."""
        mock_response = {
            "id": "9782380712957",
            "formatted_price": "7,30 €",
            "availability": "En stock !",
            "merchant": "Expédié et vendu par BDfugue.",
            "store_link": "https://www.bdfugue.com/spy-x-family-tome-8",
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_bdfugue_offer_v1("9782380712957")

        mock_client_api.get.assert_called_once_with("/v1/bdfugue_offer/9782380712957")
        assert isinstance(response, GetBDFugueOfferV1Response)
        assert len(response.bdfugue_offers) == 1
        assert response.bdfugue_offers[0].id == "9782380712957"
        assert response.bdfugue_offers[0].formatted_price == "7,30 €"

    def test_get_bdfugue_offer_v1_not_found(self, repository, mock_client_api):
        """Test de récupération d'une offre BDFugue inexistante."""
        mock_client_api.get.side_effect = Exception("Not found")

        with pytest.raises(BDFugueOfferNotFoundException) as exc_info:
            repository.get_bdfugue_offer_v1("nonexistent")

        assert "nonexistent" in str(exc_info.value)

    def test_get_bdfugue_offer_v1_with_optional_fields_none(self, repository, mock_client_api):
        """Test de récupération d'une offre BDFugue avec champs optionnels None."""
        mock_response = {
            "id": "9782380712957",
            "merchant": "Expédié et vendu par BDfugue.",
            "store_link": "https://www.bdfugue.com/test",
        }
        mock_client_api.get.return_value = mock_response

        response = repository.get_bdfugue_offer_v1("9782380712957")

        assert isinstance(response, GetBDFugueOfferV1Response)
        assert response.bdfugue_offers[0].formatted_price is None
        assert response.bdfugue_offers[0].availability is None
