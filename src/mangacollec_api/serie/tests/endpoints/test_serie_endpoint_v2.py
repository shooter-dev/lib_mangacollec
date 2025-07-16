import pytest
from unittest.mock import Mock
from mangacollec_api.serie.endpoint.serie_endpoint import SerieEndpoint
from mangacollec_api.serie.entity.serie import Serie
from mangacollec_api.serie.entity.serie_endpoint_entity import SerieEndpointEntity
from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class TestSerieEndpointV2:
    """Tests pour les méthodes v2 de l'endpoint des séries."""
    
    def setup_method(self):
        """Configuration du mock client pour les tests."""
        self.mock_client = Mock(spec=IMangaCollecAPIClient)
        self.endpoint = SerieEndpoint(self.mock_client)

    def test_get_all_series_v2(self):
        """Test de récupération de toutes les séries (API v2)."""
        
        # Mock de la réponse API v2
        api_response = {
            "series": [
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
        
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_all_series_v2()
        
        self.mock_client.get.assert_called_once_with("/v2/series")
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(serie, Serie) for serie in result)
        assert result[0].title == "Dragon Ball"
        assert result[1].title == "One Piece"

    def test_get_series_by_id_v2(self):
        """Test de récupération d'une série par ID (API v2)."""
        
        series_id = "123e4567-e89b-12d3-a456-426614174000"
        
        # Mock de la réponse API v2 avec listes vides pour éviter les erreurs de constructeur
        api_response = {
            "series": [{
                "id": series_id, 
                "title": "Dragon Ball",
                "type_id": "manga",
                "adult_content": False,
                "editions_count": 42,
                "tasks_count": 5
            }],
            "types": [{"id": "manga", "title": "Manga", "to_display": True}],
            "kinds": [],
            "jobs": [],
            "tasks": [],
            "authors": [],
            "editions": [],
            "publishers": [],
            "volumes": [],
            "box_editions": [],
            "boxes": [],
            "box_volumes": []
        }
        
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_series_by_id_v2(series_id)
        
        self.mock_client.get.assert_called_once_with(f"/v2/series/{series_id}")
        assert isinstance(result, SerieEndpointEntity)
        
        # Vérifier que la série a été correctement désérialisée
        assert result.serie.id == series_id
        assert result.serie.title == "Dragon Ball"
        assert result.type.title == "Manga"
        assert len(result.kinds) == 0
        assert len(result.authors) == 0

    def test_get_series_by_id_v2_not_found(self):
        """Test avec une série non trouvée (API v2)."""
        
        series_id = "nonexistent-id"
        self.mock_client.get.return_value = None
        
        with pytest.raises(ValueError, match=f"Aucune série trouvée pour l'ID: {series_id}"):
            self.endpoint.get_series_by_id_v2(series_id)

    def test_get_series_by_id_v2_empty_response(self):
        """Test avec une réponse vide (API v2)."""
        
        series_id = "123e4567-e89b-12d3-a456-426614174000"
        self.mock_client.get.return_value = {}
        
        with pytest.raises(ValueError, match=f"Aucune série trouvée pour l'ID: {series_id}"):
            self.endpoint.get_series_by_id_v2(series_id)

    def test_get_all_series_v2_with_empty_response(self):
        """Test get_all_series_v2 avec une réponse vide."""
        
        api_response = {"series": []}
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_all_series_v2()
        
        self.mock_client.get.assert_called_once_with("/v2/series")
        assert isinstance(result, list)
        assert len(result) == 0

    def test_get_all_series_v2_with_none_response(self):
        """Test get_all_series_v2 avec une réponse None."""
        
        self.mock_client.get.return_value = None
        
        with pytest.raises(TypeError):
            self.endpoint.get_all_series_v2()


    def test_get_series_by_id_v2_with_populated_data(self):
        """Test get_series_by_id_v2 avec des données enrichies."""
        
        series_id = "123e4567-e89b-12d3-a456-426614174000"
        
        # Mock de la réponse API v2 avec quelques données
        api_response = {
            "series": [{
                "id": series_id, 
                "title": "Dragon Ball",
                "type_id": "manga",
                "adult_content": False,
                "editions_count": 42,
                "tasks_count": 5
            }],
            "types": [{"id": "manga", "title": "Manga", "to_display": True}],
            "kinds": [{"id": "kind1", "title": "Action"}],
            "jobs": [{"id": "job1", "title": "Author"}],
            "tasks": [{"id": "task1", "job_id": "job1", "series_id": series_id, "author_id": "author1"}],
            "authors": [{"id": "author1", "name": "Toriyama", "first_name": "Akira", "tasks_count": 5}],
            "editions": [],
            "publishers": [],
            "volumes": [],
            "box_editions": [],
            "boxes": [],
            "box_volumes": []
        }
        
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_series_by_id_v2(series_id)
        
        assert isinstance(result, SerieEndpointEntity)
        assert result.serie.title == "Dragon Ball"
        assert len(result.kinds) == 1
        assert len(result.jobs) == 1
        assert len(result.tasks) == 1
        assert len(result.authors) == 1
        assert result.kinds[0].title == "Action"
        assert result.authors[0].name == "Toriyama"


    def test_get_all_series_v2_with_large_dataset(self):
        """Test get_all_series_v2 avec un grand jeu de données."""
        
        # Générer 100 séries
        series_list = []
        for i in range(100):
            series_list.append({
                "id": f"series-{i:03d}",
                "title": f"Series {i}",
                "type_id": "manga",
                "adult_content": i % 10 == 0,  # Chaque 10ème série est adulte
                "editions_count": i * 2,
                "tasks_count": i
            })
        
        api_response = {"series": series_list}
        self.mock_client.get.return_value = api_response
        
        result = self.endpoint.get_all_series_v2()
        
        assert len(result) == 100
        assert all(isinstance(serie, Serie) for serie in result)
        assert result[0].title == "Series 0"
        assert result[99].title == "Series 99"
        assert result[10].adult_content is True  # Série 10 devrait être adulte
        assert result[11].adult_content is False