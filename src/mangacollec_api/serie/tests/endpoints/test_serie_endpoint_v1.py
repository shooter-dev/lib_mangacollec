import pytest
from unittest.mock import Mock
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint
from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class TestSerieEndpointV1:
    """Tests pour les méthodes v1 de l'endpoint des séries."""
    
    def setup_method(self):
        """Configuration du mock client pour les tests."""
        self.mock_client = Mock(spec=IMangaCollecAPIClient)
        self.endpoint = SerieEndpoint(self.mock_client)

    def test_get_all_series(self):
        """Test de récupération de toutes les séries (API v1)."""
        
        # Mock de la réponse API
        expected_response = {
            "count": 2,
            "results": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "title": "Dragon Ball",
                    "type_id": "manga",
                    "adult_content": False,
                    "editions_count": 42,
                    "tasks_count": 5
                },
                {
                    "id": "456e7890-e89b-12d3-a456-426614174000",
                    "title": "One Piece",
                    "type_id": "manga",
                    "adult_content": False,
                    "editions_count": 100,
                    "tasks_count": 10
                }
            ]
        }
        
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_all_series()
        
        self.mock_client.get.assert_called_once_with("/v1/series")
        assert result == expected_response

    def test_get_series_by_id(self):
        """Test de récupération d'une série par ID (API v1)."""
        
        series_id = "123e4567-e89b-12d3-a456-426614174000"
        expected_response = {
            "id": series_id,
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5
        }
        
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_series_by_id(series_id)
        
        self.mock_client.get.assert_called_once_with(f"/v1/series/{series_id}")
        assert result == expected_response

    def test_get_all_series_empty_response(self):
        """Test avec une réponse vide."""
        
        expected_response = {"count": 0, "results": []}
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_all_series()
        
        assert result == expected_response

    def test_get_series_by_id_not_found(self):
        """Test avec une série non trouvée."""
        
        series_id = "nonexistent-id"
        self.mock_client.get.return_value = None
        
        result = self.endpoint.get_series_by_id(series_id)
        
        self.mock_client.get.assert_called_once_with(f"/v1/series/{series_id}")
        assert result is None

    def test_client_call_failure(self):
        """Test de gestion d'erreur lors de l'appel API."""
        
        # Simulation d'une exception lors de l'appel API
        self.mock_client.get.side_effect = Exception("API Error")
        
        with pytest.raises(Exception, match="API Error"):
            self.endpoint.get_all_series()

    def test_endpoint_methods_with_special_characters_in_id(self):
        """Test avec des caractères spéciaux dans l'ID."""
        
        series_id = "test-id-with-special-chars-!@#$%"
        expected_response = {
            "id": series_id,
            "title": "Test Series",
            "type_id": "test",
            "adult_content": False,
            "editions_count": 1,
            "tasks_count": 1
        }
        
        self.mock_client.get.return_value = expected_response
        
        result = self.endpoint.get_series_by_id(series_id)
        
        self.mock_client.get.assert_called_once_with(f"/v1/series/{series_id}")
        assert result == expected_response


    def test_endpoint_initialization(self):
        """Test de l'initialisation de l'endpoint."""
        
        assert self.endpoint.client == self.mock_client
        assert isinstance(self.endpoint.client, IMangaCollecAPIClient)

