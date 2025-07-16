from mangacollec_api.serie.entity.serie import Serie


class TestSerie:
    def test_serie_creation(self):
        """Test de création d'une série."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        assert serie.id == "123e4567-e89b-12d3-a456-426614174000"
        assert serie.title == "Dragon Ball"
        assert serie.type_id == "manga"
        assert serie.adult_content is False
        assert serie.editions_count == 42
        assert serie.tasks_count == 5


    def test_serie_with_empty_title(self):
        """Test de création d'une série avec titre vide."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="",
            type_id="manga",
            adult_content=False,
            editions_count=1,
            tasks_count=1
        )
        
        assert serie.title == ""

    def test_serie_equality(self):
        """Test d'égalité entre deux séries."""
        serie1 = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        serie2 = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        # Si la classe Serie implémente __eq__, sinon cela comparera les instances
        assert serie1.id == serie2.id
        assert serie1.title == serie2.title
        assert serie1.type_id == serie2.type_id
        assert serie1.adult_content == serie2.adult_content
        assert serie1.editions_count == serie2.editions_count
        assert serie1.tasks_count == serie2.tasks_count

    def test_serie_string_representation(self):
        """Test de la représentation string d'une série."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        # Test que la série peut être convertie en string
        str_repr = str(serie)
        assert isinstance(str_repr, str)
        assert len(str_repr) > 0

    def test_serie_repr(self):
        """Test de la représentation repr d'une série."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        assert repr(serie) == "123e4567-e89b-12d3-a456-426614174000"

    def test_serie_to_dict(self):
        """Test de la conversion en dictionnaire."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        result = serie.to_dict()
        expected = {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "title": "Dragon Ball",
            "type_id": "manga",
            "adult_content": False,
            "editions_count": 42,
            "tasks_count": 5,
            "kinds_ids": []
        }
        
        assert result == expected

    def test_serie_with_kinds_ids(self):
        """Test de création d'une série avec kinds_ids."""
        kinds_ids = ["kind1", "kind2", "kind3"]
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5,
            kinds_ids=kinds_ids
        )
        
        assert serie.kinds_ids == kinds_ids
        assert len(serie.kinds_ids) == 3


    def test_serie_with_different_type_ids(self):
        """Test avec différents types d'ID de type."""
        type_ids = ["manga", "anime", "novel", "webtoon", "game"]
        
        for type_id in type_ids:
            serie = Serie(
                id=f"123e4567-e89b-12d3-a456-42661417400{type_ids.index(type_id)}",
                title=f"Test {type_id.capitalize()}",
                type_id=type_id,
                adult_content=False,
                editions_count=10,
                tasks_count=2
            )
            
            assert serie.type_id == type_id
            assert serie.title == f"Test {type_id.capitalize()}"

    def test_serie_field_types(self):
        """Test des types des champs de la série."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        assert isinstance(serie.id, str)
        assert isinstance(serie.title, str)
        assert isinstance(serie.type_id, str)
        assert isinstance(serie.adult_content, bool)
        assert isinstance(serie.editions_count, int)
        assert isinstance(serie.tasks_count, int)
        assert serie.kinds_ids is None

    def test_serie_with_empty_kinds_ids_list(self):
        """Test avec une liste kinds_ids vide."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5,
            kinds_ids=[]
        )
        
        assert serie.kinds_ids == []
        assert len(serie.kinds_ids) == 0

    def test_serie_typo_in_str_method(self):
        """Test pour vérifier la typo dans __srt__ au lieu de __str__."""
        serie = Serie(
            id="123e4567-e89b-12d3-a456-426614174000",
            title="Dragon Ball",
            type_id="manga",
            adult_content=False,
            editions_count=42,
            tasks_count=5
        )
        
        # Vérifier que la méthode __srt__ existe (typo dans le code)
        assert hasattr(serie, '__srt__')
        # Vérifier que __srt__ retourne le titre
        assert serie.__srt__() == "Dragon Ball"