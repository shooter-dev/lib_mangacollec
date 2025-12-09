# Guide de Démarrage Rapide - Nouvelle Ressource

Ce guide vous aide à créer une nouvelle ressource en suivant le pattern `Author`.

## 🚀 Démarrage en 5 étapes

### Étape 1 : Analyse de la Documentation (CRITICAL)

**Commandes à exécuter :**

```bash
# 1. Vérifier les endpoints disponibles
ls datas/{resource}/endpoints/

# 2. Lire la documentation du repository (SOURCE DE VÉRITÉ)
cat datas/{resource}/repository/repository.md

# 3. Vérifier les use cases documentés
ls datas/{resource}/use_cases/

# 4. Identifier les réponses JSON brutes
ls datas/_endpoints/{resource}/
```

**Questions à se poser :**

- [ ] Quels endpoints sont disponibles ?
  - [ ] GET /v2/{resources}/ (liste) ?
  - [ ] GET /v2/{resources}/{id} (détail) ?
  - [ ] POST /v2/{resources}/ (création) ?
  - [ ] PUT/PATCH /v2/{resources}/{id} (mise à jour) ?
  - [ ] DELETE /v2/{resources}/{id} (suppression) ?

- [ ] L'endpoint GET by_id retourne-t-il une structure normalisée avec plusieurs entités ?
- [ ] Quelles sont les entités liées retournées par l'API ?

### Étape 2 : Identifier le Pattern de Mapper

Selon les endpoints disponibles, choisir le pattern :

| Cas | Pattern | Exemple de Référence |
|-----|---------|----------------------|
| GET list + GET by_id (avec relations) | **Mapper Complet** | `AuthorMapper` |
| GET by_id uniquement (avec relations) | **Mapper Simple** | `EditionMapper` |
| GET simple sans relations | **Mapper Basique** | `JobMapper` |

### Étape 3 : Créer les Entités et DTOs

#### 3.1 Entité de Domaine

```bash
# Créer l'entité
touch src/domain/entities/{resource}.py
```

**Template** :

```python
from dataclasses import dataclass

@dataclass
class {Resource}:
    """Entité {Resource} du domaine."""
    id: str
    name: str
    # Autres champs...
```

#### 3.2 DTOs de Réponse

```bash
# Créer les DTOs de réponse
touch src/application/dto/responses/{resource}_responses.py
```

**Template** :

```python
from dataclasses import dataclass
from mangacollec.domain.entities import

{Resource}


@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    """Réponse pour Get{Resource}ByIdV2.

    Structure normalisée V2 avec des tableaux séparés pour chaque type d'entité.
    """
    {resources}: list[{Resource}]
    # TOUJOURS utiliser des listes, même pour une seule entité
    related_entities: list[RelatedEntity]


# Si endpoint GET list existe :
@dataclass(frozen=True)
class GetAll{Resource}sV2Response:
    """Réponse pour GetAll{Resource}sV2."""
    {resources}: list[{Resource}]
```

**⚠️ CRITICAL** : Mettre à jour `src/application/dto/responses/__init__.py`

### Étape 4 : Créer le Mapper

```bash
# Créer le mapper
touch src/application/mappers/{resource}_mapper.py
```

**📖 Consulter** : `datas/_exemple/mappers/resource_mapper_template.md`

**Méthodes à implémenter** :

| Méthode | Condition | Obligatoire |
|---------|-----------|-------------|
| `from_dict()` | Toujours | ✅ |
| `to_dict()` | Toujours | ✅ |
| `from_api_response()` | Si structure normalisée V2 | ⚠️ |
| `from_all_{resources}_response()` | Si endpoint GET list existe | ⚠️ |
| `to_list_item()` | Si besoin affichage liste | ❌ |

**Code minimal** :

```python
from mangacollec.application import Get

{Resource}
ByIdV2Response
from mangacollec.domain.entities import

{Resource}


class {Resource}Mapper:
    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        return {Resource}(
            id=data["id"],
            name=data["name"],
            optional_field=data.get("optional_field"),
            count=data.get("count", 0),
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        return {
            "id": resource.id,
            "name": resource.name,
            "optional_field": resource.optional_field,
            "count": resource.count,
        }

    @staticmethod
    def from_api_response(response: dict) -> Get{Resource}

    ByIdV2Response:
    {resources} = [
        {Resource}Mapper.from_dict(r)
    for r in response.get("{resources}", [])
    ]
    return Get
    {Resource}
    ByIdV2Response({resources} = {resources})
```

### Étape 5 : Créer les Repositories

#### 5.1 Interface Repository

```bash
touch src/domain/repositories/{resource}_repository.py
```

**Template** :

```python
from abc import ABC, abstractmethod
from mangacollec.domain.entities import

{Resource}


class I{Resource}Repository(ABC):
    """Interface du repository pour {Resource}."""

    # AJOUTER UNIQUEMENT les méthodes supportées par l'API
    @abstractmethod
    def get_by_id(self, id: str) -> {Resource} | None:
        pass
```

#### 5.2 Repository API

```bash
touch src/infrastructure/repositories/api/api_{resource}_repository.py
```

**📖 Consulter** : `datas/_exemple/repositories/api_repository_template.md`

**Template Minimal (Pattern Author)** :

```python
from mangacollec.application import Get

{Resource}
ByIdV2Response
from mangacollec.application import IMangaCollecAPI
from mangacollec.application.mappers

{resource}
_mapper
import

{Resource}
Mapper
from mangacollec.domain.exceptions

{resource}
_exceptions
import

{Resource}
NotFoundException
from mangacollec.domain.repositories

{resource}
_repository
import I

{Resource}
Repository


class API{Resource}Repository(I{Resource}Repository):
    """Implémentation du repository {Resource} via MangaCollecAPI V2."""

    def __init__(self, client_api: IMangaCollecAPI) -> None:
        self.client_api = client_api

    def get_by_id_v2(self, {resource}_id: str) -> Get{Resource}

    ByIdV2Response:
    """Récupère un(e) {resource} par son ID avec toutes ses relations."""
    try:
        response = self.client_api.get(f"/v2/{resources}/{{{resource}_id}}")

        if not response.get("{resources}") or len(response["{resources}"]) == 0:
            raise {Resource}
            NotFoundException({resource}
            _id)

            # ✅ CRITICAL : Déléguer au mapper (3 lignes max)
            return {Resource}
            Mapper.from_api_response(response)

        except Exception as e:
        if isinstance(e, {Resource}NotFoundException):
            raise
        raise {Resource}
        NotFoundException({resource}
        _id) from e


def get_all_v2(self) -> GetAll{Resource}


sV2Response:
"""Récupère tous les {resources} via l'API."""
try:
    response = self.client_api.get("/v2/{resources}/")
    # ✅ CRITICAL : Déléguer au mapper
    return {Resource}
    Mapper.from_all_
    {resources}
    _response(response)
except Exception as e:
    raise RuntimeError(f"Failed to retrieve {resources}: {{e}}") from e
```

**⚠️ Règles Critiques pour les Repositories** :

1. **TOUJOURS** déléguer la conversion au mapper
   - ✅ `return {Resource}Mapper.from_api_response(response)`
   - ❌ Conversion manuelle ligne par ligne

2. **TOUJOURS** utiliser `IMangaCollecAPI`
   - ✅ `self.client_api.get(...)`
   - ❌ `requests.get(...)`

3. **Chaque méthode = 3-5 lignes maximum**
   - Appel API + Vérification + Délégation mapper

4. **AUCUNE logique métier** dans le repository

## ✅ Checklist de Validation

Avant de considérer la ressource terminée :

- [ ] **Mapper conforme au pattern Author**
  - [ ] `from_dict()` et `to_dict()` implémentés
  - [ ] `from_api_response()` si structure normalisée
  - [ ] `from_all_{resources}_response()` si endpoint GET list existe
  - [ ] Imports des mappers liés corrects
  - [ ] DTOs utilisent des listes (pluriel)
  - [ ] Aucune conversion manuelle dans le repository

- [ ] **Repository conforme au pattern Author**
  - [ ] Injection de `IMangaCollecAPI` dans le constructeur
  - [ ] Aucune utilisation de `requests`
  - [ ] Délégation systématique au mapper (via `from_api_response()`)
  - [ ] Méthodes courtes (3-5 lignes max)
  - [ ] Gestion des erreurs avec exceptions de domaine
  - [ ] Vérification que la réponse contient des données

- [ ] **Tests créés**
  - [ ] Tests du mapper
  - [ ] Tests du repository API
  - [ ] Tests du repository InMemory
  - [ ] Couverture ≥ 90%

- [ ] **Code de qualité**
  - [ ] `ruff format` exécuté
  - [ ] `ruff check` sans erreurs
  - [ ] Type hints partout
  - [ ] Docstrings Google

## 📚 Ressources

### Templates
- **Template Mapper Complet** : `datas/_exemple/mappers/resource_mapper_template.md`
- **Template Repository API** : `datas/_exemple/repositories/api_repository_template.md`
- **Guide des Patterns Mapper** : `datas/_exemple/mappers/MAPPER_PATTERNS.md`

### Exemples de Référence
- **Mapper Complet** : `src/application/mappers/author_mapper.py`
- **Mapper Simple** : `src/application/mappers/edition_mapper.py`
- **Repository Complet** : `src/infrastructure/repositories/api/api_author_repository.py`
- **Repository Simple** : `src/infrastructure/repositories/api/api_edition_repository.py`

### Documentation
- **Documentation Complète** : `CLAUDE.md`

## 🎯 Commandes Utiles

```bash
# Vérifier la syntaxe
python -m py_compile src/application/mappers/{resource}_mapper.py

# Tester l'import
python -c "from src.application.mappers.{resource}_mapper import {Resource}Mapper; print('OK')"

# Formater le code
ruff format src/

# Vérifier le linting
ruff check src/

# Lancer les tests
pytest tests/ -v
```

## ⚠️ Erreurs Courantes à Éviter

### Mappers

1. **DTO avec entité au singulier** :
   - ❌ `publisher: Publisher`
   - ✅ `publishers: list[Publisher]`

2. **Champs optionnels sans .get()** :
   - ❌ `data["optional_field"]`
   - ✅ `data.get("optional_field")`

3. **Mapper sans import des mappers liés** :
   - ❌ Créer l'entité directement
   - ✅ `RelatedMapper.from_dict(data)`

### Repositories

4. **Conversion manuelle dans le repository** (ERREUR CRITIQUE) :
   - ❌ Faire la conversion ligne par ligne (25 lignes)
   - ✅ Déléguer au mapper : `{Resource}Mapper.from_api_response(response)` (1 ligne)

5. **Repository sans MangaCollecAPI** :
   - ❌ `requests.get(...)`
   - ✅ `self.client_api.get(...)`

6. **Repository avec logique métier** :
   - ❌ Filtrage, validation, transformation dans le repository
   - ✅ Repository = Appel API + Délégation mapper uniquement

## 🚨 Règle d'Or

> **Si un endpoint n'existe pas dans `datas/{resource}/repository/repository.md`,
> alors l'API ne supporte PAS cette action. Ne PAS l'implémenter.**
