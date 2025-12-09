# Template de Tests pour Repository API

Ce template suit le pattern établi par `test_api_author_repository.py` pour garantir la cohérence des tests.

## 🎯 Structure Standard des Tests

```python
"""Tests pour API{Resource}Repository.

This module contains unit tests for the API {Resource} repository.
"""

from unittest.mock import Mock

import pytest

from mangacollec.application import (
    GetAll

{Resource}
sV2Response,  # Si endpoint GET list existe
Get
{Resource}
ByIdV2Response,
)
from mangacollec.application import IMangaCollecAPI
from mangacollec.domain.entities import

{Resource}, {Resource}
ListItem  # Si get_list existe
from mangacollec.domain.exceptions

{resource}
_exceptions
import

{Resource}
NotFoundException
from mangacollec.infrastructure.repositories.api

{resource}
_repository
import API

{Resource}
Repository


class TestAPI{Resource}Repository:
    """Tests pour API{Resource}Repository."""

    # ================================================================
    # FIXTURES (Setup des tests)
    # ================================================================

    @pytest.fixture
    def mock_api_client(self) -> Mock:
        """Fixture pour créer un mock du client API."""
        return Mock(spec=IMangaCollecAPI)

    @pytest.fixture
    def repository(self, mock_api_client: Mock) -> API{Resource}

    Repository:
    """Fixture pour créer un repository avec mock API."""
    return API
    {Resource}
    Repository(mock_api_client)


@pytest.fixture
def sample_{resource}


_data(self) -> dict:
"""Fixture pour créer des données de {resource} de test."""
return {
    "id": "{resource}-123",
    "name": "Sample {Resource}",
    # Ajouter les autres champs selon l'entité
}


# Si le repository retourne des entités liées, créer une fixture pour chaque
@pytest.fixture
def sample_related_data(self) -> dict:
    """Fixture pour créer des données d'entité liée de test."""
    return {
        "id": "related-456",
        "title": "Related Entity",
    }


# ================================================================
# TESTS GET BY ID (OBLIGATOIRES si endpoint existe)
# ================================================================

def test_get_by_id_success(
        self,
        repository: API{Resource}


Repository,
mock_api_client: Mock,
sample_
{resource}
_data: dict,
) -> None:
"""Test de récupération d'un(e) {resource} par ID avec toutes ses relations."""
# Préparer la réponse mock (structure normalisée V2)
mock_api_client.get.return_value = {
    "{resources}": [sample_{resource}_data],
    # Ajouter les entités liées selon l'API
    "related": [],
}

# Appeler la méthode
result = repository.get_by_id_v2("{resource}-123")

# Vérifier que c'est une Get{Resource}ByIdV2Response
assert isinstance(result, Get
{Resource}
ByIdV2Response)

# Vérifier la ressource principale
assert len(result.
{resources}) == 1
resource = result.
{resources}[0]
assert isinstance(resource, {Resource})
assert resource.id == "{resource}-123"
assert resource.name == "Sample {Resource}"

# Vérifier les entités liées
assert isinstance(result.related, list)

# Vérifier l'appel API
mock_api_client.get.assert_called_once_with("/v2/{resources}/{resource}-123")


def test_get_by_id_not_found_empty_list(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de récupération d'un(e) {resource} inexistant(e) (liste vide)."""
mock_api_client.get.return_value = {"{resources}": []}

with pytest.raises({Resource}NotFoundException) as exc_info:
    repository.get_by_id_v2("nonexistent-id")

assert "nonexistent-id" in str(exc_info.value)


def test_get_by_id_not_found_no_key(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de récupération sans clé '{resources}' dans la réponse."""
mock_api_client.get.return_value = {}

with pytest.raises({Resource}NotFoundException):
    repository.get_by_id_v2("test-id")


def test_get_by_id_api_exception(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de gestion d'erreur API."""
mock_api_client.get.side_effect = Exception("API Error")

with pytest.raises({Resource}NotFoundException):
    repository.get_by_id_v2("test-id")


def test_get_by_id_with_all_relations(
        self,
        repository: API{Resource}


Repository,
mock_api_client: Mock,
sample_
{resource}
_data: dict,
sample_related_data: dict,
) -> None:
"""Test de récupération avec toutes les relations."""
# Données complètes de la réponse API
mock_api_client.get.return_value = {
    "{resources}": [sample_{resource}_data],
    "related": [sample_related_data],
}

result = repository.get_by_id_v2("{resource}-123")

# Vérifier que c'est une Get{Resource}ByIdV2Response
assert isinstance(result, Get
{Resource}
ByIdV2Response)

# Vérifier la ressource
assert len(result.
{resources}) == 1
assert result.
{resources}[0].id == "{resource}-123"

# Vérifier les entités liées
assert len(result.related) == 1
assert result.related[0].id == "related-456"


def test_get_by_id_optional_fields(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de récupération avec champs optionnels manquants."""
resource_data = {
    "id": "test-id",
    "name": "Test {Resource}",
    # Champs optionnels omis
}
mock_api_client.get.return_value = {
    "{resources}": [resource_data],
    "related": [],
}

result = repository.get_by_id_v2("test-id")
resource = result.
{resources}[0]

# Vérifier que les champs optionnels sont None
assert resource.optional_field is None


# ================================================================
# TESTS GET ALL (OBLIGATOIRES si endpoint GET list existe)
# ================================================================

def test_get_all_success(
        self,
        repository: API{Resource}


Repository,
mock_api_client: Mock,
sample_
{resource}
_data: dict,
) -> None:
"""Test de récupération de tous les {resources}."""
mock_api_client.get.return_value = {
    "{resources}": [
        sample_{resource}_data,
        {
            "id": "{resource}-456",
            "name": "Another {Resource}",
        },
    ]
}

result = repository.get_all_v2()

assert isinstance(result, GetAll
{Resource}
sV2Response)
assert len(result.
{resources}) == 2
assert all(isinstance(r, {Resource}) for r in result.
{resources})
assert result.
{resources}[0].name == "Sample {Resource}"
assert result.
{resources}[1].name == "Another {Resource}"

mock_api_client.get.assert_called_once_with("/v2/{resources}/")


def test_get_all_empty(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de récupération avec liste vide."""
mock_api_client.get.return_value = {"{resources}": []}

result = repository.get_all_v2()

assert isinstance(result, GetAll
{Resource}
sV2Response)
assert result.
{resources} == []


def test_get_all_no_key(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de récupération sans clé '{resources}'."""
mock_api_client.get.return_value = {}

result = repository.get_all_v2()

assert isinstance(result, GetAll
{Resource}
sV2Response)
assert result.
{resources} == []


def test_get_all_api_exception(
        self, repository: API{Resource}


Repository, mock_api_client: Mock
) -> None:
"""Test de gestion d'erreur API pour get_all."""
mock_api_client.get.side_effect = Exception("API Error")

with pytest.raises(RuntimeError) as exc_info:
    repository.get_all_v2()

assert "Failed to retrieve {resources}" in str(exc_info.value)


# ================================================================
# TESTS GET LIST (OPTIONNELS - si méthode get_list existe)
# ================================================================

def test_get_list_success(
        self,
        repository: API{Resource}


Repository,
mock_api_client: Mock,
sample_
{resource}
_data: dict,
) -> None:
"""Test de récupération de la liste simplifiée."""
mock_api_client.get.return_value = {
    "{resources}": [
        sample_{resource}_data,
        {"id": "{resource}-456", "name": "Test"},
    ]
}

items = repository.get_list()

assert len(items) == 2
assert all(isinstance(item, {Resource}
ListItem) for item in items)

first_item = next(item for item in items if item.id == "{resource}-123")
assert first_item.display_name == "Sample {Resource}"
```

## 📋 Checklist de Tests Obligatoires

### Tests GET by_id (si endpoint existe)

- [ ] `test_get_by_id_success` - Cas nominal avec toutes relations
- [ ] `test_get_by_id_not_found_empty_list` - Liste vide
- [ ] `test_get_by_id_not_found_no_key` - Clé manquante
- [ ] `test_get_by_id_api_exception` - Erreur API
- [ ] `test_get_by_id_with_all_relations` - Toutes les entités liées
- [ ] `test_get_by_id_optional_fields` - Champs optionnels manquants

### Tests GET all (si endpoint liste existe)

- [ ] `test_get_all_success` - Cas nominal avec plusieurs éléments
- [ ] `test_get_all_empty` - Liste vide
- [ ] `test_get_all_no_key` - Clé manquante
- [ ] `test_get_all_api_exception` - Erreur API

### Tests GET list (optionnel)

- [ ] `test_get_list_success` - Cas nominal

## 🎯 Patterns de Tests selon les Endpoints

| Endpoints Disponibles | Tests à Créer |
|-----------------------|---------------|
| GET by_id uniquement | 6 tests minimum (get_by_id) |
| GET list + GET by_id | 11 tests minimum (6 + 4 + 1) |
| Avec CRUD complet | Ajouter tests create, update, delete |

## ⚠️ Règles Strictes des Tests

1. **TOUJOURS** utiliser `Mock(spec=IMangaCollecAPI)` pour le client API
2. **TOUJOURS** tester la structure normalisée V2 (listes)
3. **TOUJOURS** vérifier le type de retour (DTO Response)
4. **TOUJOURS** vérifier les types des entités (`isinstance`)
5. **TOUJOURS** tester les cas d'erreur (liste vide, clé manquante, API error)

## 🔧 Fixtures Standards

### Fixture Client API Mock
```python
@pytest.fixture
def mock_api_client(self) -> Mock:
    """Fixture pour créer un mock du client API."""
    return Mock(spec=IMangaCollecAPI)
```

### Fixture Repository
```python
@pytest.fixture
def repository(self, mock_api_client: Mock) -> API{Resource}Repository:
    """Fixture pour créer un repository avec mock API."""
    return API{Resource}Repository(mock_api_client)
```

### Fixture Données de Test
```python
@pytest.fixture
def sample_{resource}_data(self) -> dict:
    """Fixture pour créer des données de {resource} de test."""
    return {
        "id": "{resource}-123",
        "name": "Sample {Resource}",
        # Utiliser les vraies clés de l'API
    }
```

## 📊 Assertions Standards

### Vérifier le Type de Réponse
```python
assert isinstance(result, Get{Resource}ByIdV2Response)
```

### Vérifier la Liste Principale
```python
assert len(result.{resources}) == 1
resource = result.{resources}[0]
assert isinstance(resource, {Resource})
```

### Vérifier les Entités Liées
```python
assert isinstance(result.related, list)
assert len(result.related) == expected_count
assert all(isinstance(r, RelatedEntity) for r in result.related)
```

### Vérifier l'Appel API
```python
mock_api_client.get.assert_called_once_with("/v2/{resources}/{resource}-123")
```

### Vérifier les Exceptions
```python
with pytest.raises({Resource}NotFoundException) as exc_info:
    repository.get_by_id_v2("test-id")

assert "test-id" in str(exc_info.value)
```

## 🎨 Cas de Tests Spécifiques

### Test avec Champs Optionnels
```python
def test_get_by_id_optional_fields(self, repository, mock_api_client):
    """Vérifier que les champs optionnels manquants sont None."""
    resource_data = {
        "id": "test-id",
        "name": "Test",
        # Optional fields omitted
    }
    mock_api_client.get.return_value = {"{resources}": [resource_data]}

    result = repository.get_by_id_v2("test-id")
    assert result.{resources}[0].optional_field is None
```

### Test avec Multiples Relations
```python
def test_get_by_id_with_all_relations(self, repository, mock_api_client, ...):
    """Vérifier toutes les entités liées."""
    mock_api_client.get.return_value = {
        "{resources}": [...],
        "related1": [...],
        "related2": [...],
    }

    result = repository.get_by_id_v2("test-id")
    assert len(result.related1) == expected_count
    assert len(result.related2) == expected_count
```

## 📚 Exemples de Référence

- **Tests Complets** : `tests/infrastructure/repositories/api/test_api_author_repository.py`
- **Tests Simples** : `tests/infrastructure/repositories/api/test_api_edition_repository.py`

## 🚀 Commandes de Test

```bash
# Lancer tous les tests du repository
pytest tests/infrastructure/repositories/api/test_api_{resource}_repository.py -v

# Lancer un test spécifique
pytest tests/infrastructure/repositories/api/test_api_{resource}_repository.py::TestAPI{Resource}Repository::test_get_by_id_success -v

# Avec couverture
pytest tests/infrastructure/repositories/api/test_api_{resource}_repository.py --cov=src/infrastructure/repositories/api/api_{resource}_repository -v
```

## 💡 Tips

1. **Nommer les tests clairement** : `test_{methode}_{cas}` (ex: `test_get_by_id_success`)
2. **Un test = Un cas** : Ne pas tester plusieurs choses dans un seul test
3. **Mock minimal** : Seulement mocker `IMangaCollecAPI`, pas les mappers
4. **Fixtures réutilisables** : Créer des fixtures pour les données de test
5. **Vérifier les appels** : Toujours vérifier que l'API est appelée correctement

## ⚠️ Erreurs Courantes

1. **Oublier de tester les listes vides** : `{resources}: []`
2. **Oublier de tester les clés manquantes** : `{}`
3. **Oublier de tester les erreurs API** : `side_effect = Exception(...)`
4. **Ne pas vérifier les types** : Toujours utiliser `isinstance()`
5. **Oublier les champs optionnels** : Tester avec/sans champs optionnels
