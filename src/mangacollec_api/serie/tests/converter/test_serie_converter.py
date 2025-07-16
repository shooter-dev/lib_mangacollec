import pytest
from mangacollec_api.serie.converter.serie_converter import SerieConverter
from mangacollec_api.serie.entity.serie import Serie


class TestSerieConverter:
    def setup_method(self):
        """Configuration du convertisseur pour les tests."""
        self.converter = SerieConverter()

    def test_deserialize_complete_serie(self):
        """Test de désérialisation d'une série complète."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.id == "123e4567-e89b-12d3-a456-426614174000"
        assert serie.title == "Dragon Ball"
        assert serie.type_id == "manga"
        assert serie.adult_content is False
        assert serie.editions_count == 42
        assert serie.tasks_count == 5

    def test_deserialize_serie_with_adult_content(self):
        """Test de désérialisation d'une série avec contenu adulte."""
        
        data = {
            "id": "456e7890-e89b-12d3-a456-426614174000",
            "title": "Prison School",
            "type_id": "manga",
            "adult_content": True,
            "editions_count": 28,
            "tasks_count": 3
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.adult_content is True
        assert serie.title == "Prison School"

    def test_deserialize_serie_with_zero_counts(self):
        """Test de désérialisation d'une série avec zéro éditions et tâches."""
        
        data = {
            "id": "789e0123-e89b-12d3-a456-426614174000",
            "title": "Nouvelle série",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 0,
            "tasks_count": 0
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.editions_count == 0
        assert serie.tasks_count == 0

    def test_deserialize_serie_with_empty_title(self):
        """Test de désérialisation d'une série avec titre vide."""
        
        data = {
            "id": "abc1234-e89b-12d3-a456-426614174000",
            "title": "",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 1,
            "tasks_count": 1
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.title == ""

    def test_deserialize_with_missing_field(self):
        """Test de désérialisation avec un champ manquant."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42
            # tasks_count manquant
        }
        
        with pytest.raises(KeyError):
            self.converter.deserialize(data)

    def test_deserialize_with_none_data(self):
        """Test de désérialisation avec données None."""
        
        with pytest.raises(TypeError):
            self.converter.deserialize(None)

    def test_deserialize_with_empty_dict(self):
        """Test de désérialisation avec dictionnaire vide."""
        
        data = {}
        
        with pytest.raises(KeyError):
            self.converter.deserialize(data)

    def test_deserialize_with_extra_fields(self):
        """Test de désérialisation avec des champs supplémentaires."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5,
            "extra_field": "extra_value",
            "another_field": 123,
            "description": "Une description supplémentaire"
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.id == "123e4567-e89b-12d3-a456-426614174000"
        assert serie.title == "Dragon Ball"
        assert serie.type_id == "manga"
        assert serie.adult_content is False
        assert serie.editions_count == 42
        assert serie.tasks_count == 5
        # Les champs supplémentaires sont ignorés

    def test_deserialize_with_wrong_types(self):
        """Test de désérialisation avec des types incorrects."""
        
        data = {
            "id": 123,  # Devrait être string
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": "false",  # Devrait être bool
            "editions_count": "42",  # Devrait être int
            "tasks_count": 5.5  # Devrait être int
        }
        
        # Le convertisseur ne valide pas les types, il les accepte tels quels
        serie = self.converter.deserialize(data)
        
        assert serie.id == 123
        assert serie.adult_content == "false"
        assert serie.editions_count == "42"
        assert serie.tasks_count == 5.5

    def test_deserialize_with_unicode_characters(self):
        """Test de désérialisation avec des caractères unicode."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "ドラゴンボール",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.title == "ドラゴンボール"

    def test_deserialize_with_large_counts(self):
        """Test de désérialisation avec de grands nombres."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Very Long Series",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 999999,
            "tasks_count": 888888
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.editions_count == 999999
        assert serie.tasks_count == 888888

    def test_deserialize_with_negative_counts(self):
        """Test de désérialisation avec des nombres négatifs."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Test Series",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": -1,
            "tasks_count": -5
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.editions_count == -1
        assert serie.tasks_count == -5

    def test_deserialize_with_long_strings(self):
        """Test de désérialisation avec des chaînes très longues."""
        
        long_title = "A" * 1000
        long_type_id = "B" * 500
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": long_title,
            "type_id": long_type_id,
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.title == long_title
        assert serie.type_id == long_type_id
        assert len(serie.title) == 1000
        assert len(serie.type_id) == 500

    def test_deserialize_with_special_characters(self):
        """Test de désérialisation avec des caractères spéciaux."""
        
        data = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Serie's \"Special\" Title & More!",
            "type_id": "manga/anime",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5
        }
        
        serie = self.converter.deserialize(data)
        
        assert isinstance(serie, Serie)
        assert serie.title == "Serie's \"Special\" Title & More!"
        assert serie.type_id == "manga/anime"

    def test_serialize_not_implemented(self):
        """Test que la méthode serialize n'est pas implémentée."""
        
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        # La méthode serialize n'est pas implémentée
        result = self.converter.serialize(serie)
        assert result is None

    def test_deserialize_with_different_type_ids(self):
        """Test de désérialisation avec différents types d'ID de type."""
        
        type_ids = ["manga", "anime", "novel", "webtoon", "game"]
        
        for type_id in type_ids:
            data = {
                "id": f"123e4567-e89b-12d3-a456-42661417400{type_ids.index(type_id)}",
                "title": f"Test {type_id.capitalize()}",
                "type_id": type_id,
                "adult_content": False,
                "editions_count": 10,
                "tasks_count": 2
            }
            
            serie = self.converter.deserialize(data)
            
            assert isinstance(serie, Serie)
            assert serie.type_id == type_id
            assert serie.title == f"Test {type_id.capitalize()}"