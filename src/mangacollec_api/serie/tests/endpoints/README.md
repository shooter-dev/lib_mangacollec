# Tests d'endpoints Serie

Ce dossier contient les tests pour les endpoints de séries, séparés par version d'API.

## Structure

```
endpoints/
├── test_serie_endpoint_v1.py    # Tests pour l'API v1
├── test_serie_endpoint_v2.py    # Tests pour l'API v2
└── README.md                    # Ce fichier
```

## Tests API v1 (`test_serie_endpoint_v1.py`)

**Classe:** `TestSerieEndpointV1`

**Méthodes testées:**
- `get_all_series()` - Récupération de toutes les séries
- `get_series_by_id()` - Récupération d'une série par ID

**Caractéristiques v1:**
- Retourne des dictionnaires bruts
- Endpoints `/v1/series`
- Compatibilité legacy

**Tests inclus:**
- Réponses normales et vides
- Gestion d'erreurs et exceptions
- Caractères spéciaux et Unicode
- Contenu adulte et compteurs à zéro

## Tests API v2 (`test_serie_endpoint_v2.py`)

**Classe:** `TestSerieEndpointV2`

**Méthodes testées:**
- `get_all_series_v2()` - Récupération de toutes les séries (objets typés)
- `get_series_by_id_v2()` - Récupération d'une série avec données enrichies

**Caractéristiques v2:**
- Retourne des objets `Serie` et `SerieEndpointEntity`
- Endpoints `/v2/series`
- Données enrichies avec relations (auteurs, éditions, etc.)

**Tests inclus:**
- Désérialisation vers objets typés
- Données enrichies avec entités liées
- Gestion des listes vides et nulles
- Tests de performance avec grands datasets
- Validation des types de retour

## Exécution des tests

```bash
# Tests v1 uniquement
poetry run pytest src/mangacollec_api/serie/tests/endpoints/test_serie_endpoint_v1.py

# Tests v2 uniquement
poetry run pytest src/mangacollec_api/serie/tests/endpoints/test_serie_endpoint_v2.py

# Tous les tests d'endpoints
poetry run pytest src/mangacollec_api/serie/tests/endpoints/

# Avec verbose
poetry run pytest src/mangacollec_api/serie/tests/endpoints/ -v
```

## Configuration des imports

Les imports sont gérés par la configuration pytest dans `pyproject.toml` :

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["src", "tests"]
```

Cette configuration permet d'utiliser les imports absolus normaux sans configuration supplémentaire dans chaque fichier de test.

## Avantages de la séparation

1. **Clarté** : Chaque version a ses propres tests
2. **Maintenance** : Modifications v1 n'affectent pas v2
3. **Lisibilité** : Tests plus courts et focalisés
4. **Performance** : Exécution sélective par version
5. **Évolution** : Facilite la dépréciation de v1
6. **Imports** : Configuration centralisée dans pyproject.toml