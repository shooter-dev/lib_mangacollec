# Guide de Prompts pour Gemini Client

Ce document contient tous vos workflows et agents Claude Code adaptés pour une utilisation avec Gemini Client.


## Vue d'ensemble

Ce projet suit une architecture **Clean Architecture / Domain-Driven Design (DDD)** avec une séparation stricte des responsabilités entre les couches.

---

## Structure du Projet

```
src/
├── domain/                          # Couche Domaine (noyau métier)
│   ├── entities/                    # Entités métier
│   │   └── {resource}_entity.py
│   ├── value_objects/               # Objets de valeur
│   │   └── {resource}_object.py
│   └── repositories/                # Interfaces des repositories
│       └── {resource}_repository.py
│
├── application/                     # Couche Application (logique métier)
│   ├── use_cases/                   # Cas d'utilisation
│   │   └── {resource}_usecase.py
│   ├── mapper/                      # Mappers (conversion entre couches)
│   │   └── {resource}_mapper.py
│   └── dto/                         # Data Transfer Objects
│       └── {resource}_dto.py
│
├── infrastructure/                  # Couche Infrastructure (implémentations)
│   ├── services/                    # Services externes
│   │   ├── mangacollec_api_interface.py  # Interface client API
│   │   └── mangacollec_api.py           # Implémentation client API
│   └── repositories/
│       ├── api/                     # Implémentations API
│       │   └── api_{resource}_repository.py
│       └── memory/                  # Implémentations In-Memory
│           └── inmemory_{resource}_repository.py
│
└── datas/                           # Documentation API et Use Cases
    ├── _endpoints/                  # Réponses JSON brutes de l'API
    │   └── {resource}/
    │       └── *_v*.json
    ├── _exemple/                    # Exemples de structure de documentation
    │   ├── endpoints/
    │   ├── repository/
    │   └── use_cases/
    ├── _templates/                  # Templates de documentation
    │   └── endpoint.md
    └── {resource}/                  # Documentation par ressource
        ├── endpoints/               # Documentation des endpoints API
        │   └── *.md
        ├── repository/              # Documentation du repository
        │   └── repository.md
        └── use_cases/               # Documentation des cas d'utilisation
            └── *.md
```

---

## Conventions de Nommage

| Type                 | Pattern                        | Exemple                                   |
|----------------------|--------------------------------|-------------------------------------------|
| Entity               | `{Resource}`                   | `Todo`, `User`, `Author`                  |
| Value Object         | `{Resource}Object`             | `TodoStatusObject`                        |
| Repository Interface | `I{Resource}Repository`        | `ITodoRepository`                         |
| API Repository       | `API{Resource}Repository`      | `APITodoRepository`                       |
| InMemory Repository  | `InMemory{Resource}Repository` | `InMemoryTodoRepository`                  |
| Use Case             | `{Action}{Resource}UseCase`    | `CreateTodoUseCase`, `GetByIdTodoUseCase` |
| DTO (création)       | `Create{Resource}`             | `CreateTodo`                              |
| DTO (recherche)      | `Search{Resource}`             | `SearchTodo`                              |
| DTO (mise à jour)    | `Update{Resource}`             | `UpdateTodo`                              |
| Mapper               | `{Resource}Mapper`             | `TodoMapper`                              |

---

## Documentation des Endpoints API

### Nouvelle Structure (CRITICAL)

**IMPORTANT** : La documentation est désormais organisée par ressource avec 3 types de fichiers :

#### 1. Documentation des Endpoints
- **Emplacement** : `datas/{resource}/endpoints/*.md`
- **Contenu** : Description technique de chaque endpoint API

#### 2. Documentation du Repository
- **Emplacement** : `datas/{resource}/repository/repository.md`
- **Contenu** : Liste des méthodes disponibles dans le repository avec leurs endpoints associés

#### 3. Documentation des Use Cases
- **Emplacement** : `datas/{resource}/use_cases/*.md`
- **Contenu** : Description métier de chaque cas d'utilisation (paramètres, retours, cas d'usage)

#### 4. Réponses JSON Brutes
- **Emplacement** : `datas/_endpoints/{resource}/*_v*.json`
- **Contenu** : Exemples de réponses réelles de l'API

### Format des fichiers endpoint.md
Chaque fichier markdown contient un front-matter YAML décrivant l'endpoint :

```yaml
---
resource: {resource}_{action}     # Identifiant de la ressource
version: v2                        # Version de l'API
endpoint: https://api.xxx.com/...  # URL de l'endpoint
method: GET | POST | PUT | DELETE  # Méthode HTTP
response_brut: datas/_endpoints/... # Chemin vers la réponse JSON brute
description: ...                   # Description
authentication: true | false       # Authentification requise
---
```

### Dossiers spéciaux

#### `datas/_exemple/` - Exemples de structure
- Contient des exemples de documentation bien formatée
- **Utiliser comme référence** lors de la création de nouvelle documentation
- Structure complète : endpoints/, repository/, use_cases/

### Règle fondamentale

> **⚠️ IMPORTANT : Si un fichier n'existe pas pour une action, l'API ne supporte PAS cette action.**

**CRITICAL** : Vérifier TOUJOURS `datas/{resource}/repository/repository.md` pour connaître les méthodes supportées.

| Fichier endpoint existant             | Action supportée             |
|---------------------------------------|------------------------------|
| `{resource}_v*.md` (GET single)       | `GetById{Resource}UseCase` ✅ |
| `{resources}_v*.md` (GET list)        | `GetAll{Resource}UseCase` ✅  |
| `create_{resource}_v*.md` (POST)      | `Create{Resource}UseCase` ✅  |
| `update_{resource}_v*.md` (PUT/PATCH) | `Update{Resource}UseCase` ✅  |
| `delete_{resource}_v*.md` (DELETE)    | `Delete{Resource}UseCase` ✅  |

**Exemple :** Si seuls `author_v2.md` et `authors_v2.md` existent → Lecture seule (pas de create/update/delete).

### Ressources disponibles

Les ressources suivantes sont documentées dans le dossier `datas/` :

- **authors** - Auteurs de mangas
- **editions** - Éditions de volumes
- **follow_editions** - Suivi d'éditions
- **jobs** - Métiers/rôles des auteurs
- **kinds** - Types de publications
- **offers** - Offres commerciales (Amazon, BDFugue)
- **planning** - Planning de sorties
- **possessions** - Collection personnelle
- **publishers** - Éditeurs
- **reads** - Lectures effectuées
- **series** - Séries de mangas
- **types** - Types(serie) de contenus
- **users** - Utilisateurs
- **volumes** - Volumes de mangas

**IMPORTANT** : Pour chaque ressource, **TOUJOURS** vérifier `datas/{resource}/repository/repository.md` pour connaître les méthodes disponibles.

---

## Patterns d'Implémentation

### 1. Repository Interface (Domain Layer)

```python
# src/domain/repositories/{resource}_repository.py
from abc import ABC, abstractmethod

from mangacollec.domain.entities import

{Resource}


class I{Resource}Repository(ABC):
    """Interface du repository pour {Resource}."""

    # Inclure UNIQUEMENT les méthodes supportées par l'API
    # Vérifier datas/_endpoints/{resource}/*.md

    @abstractmethod
    def get_by_id(self, id: str) -> {Resource} | None:
        """Récupère un(e) {resource} par son ID."""
        pass

    @abstractmethod
    def get_all(self) -> list[{Resource}]:
        """Récupère tous les {resource}s."""
        pass

    @abstractmethod
    def search(self, search_{resource}

    ) -> list[{Resource}] | None:
    """Récupère tous les {resource}s."""
    pass

# Ajouter create/update/delete SEULEMENT si les _endpoints existent
```

### 2. Entity (Domain Layer)

```python
# src/domain/entities/{resource}_entity.py
from dataclasses import dataclass


@dataclass
class {Resource}:
    """Entité {Resource} du domaine."""
    id: str
    # Autres attributs basés sur response_brut du endpoint
```

### 3. DTOs (Application Layer)

```python
# src/application/dto/{resource}_dto.py
from dataclasses import dataclass


@dataclass
class Create{Resource}:
    """DTO pour la création d'un(e) {resource}."""
    # Attributs requis pour la création
    name: str
    # ...


@dataclass
class Search{Resource}:
    """DTO pour la recherche de {resource}s."""
    # Tous les champs optionnels pour le filtrage
    id: str | None = None
    name: str | None = None
    # ...
```

### 4. Use Cases (Application Layer)

```python
# src/application/use_cases/{resource}_usecase.py
from mangacollec.domain import I

{Resource}
Repository
from mangacollec.domain.entities import

{Resource}
from mangacollec.application import Create

{Resource}, Search
{Resource}


class GetById{Resource}UseCase:
    """Cas d'utilisation : récupérer un(e) {resource} par ID."""

    def __init__(self, repo: I{Resource}

    Repository) -> None:
    self.repo = repo


def __call__(self, id: str) -> {Resource} | None:
    return self.repo.get_by_id_v2(id)
```

```python
# src/application/use_cases/{resource}_usecase.py
from mangacollec.domain import I

{Resource}
Repository
from mangacollec.domain.entities import

{Resource}
from mangacollec.application import Create

{Resource}, Search
{Resource}


class GetAll{Resource}UseCase:
    """Cas d'utilisation : récupérer tous les {resource}s."""

    def __init__(self, repo: I{Resource}

    Repository) -> None:
    self.repo = repo


def __call__(self) -> list[{Resource}]:
    return self.repo.get_all_v2()
```

```python
# src/application/use_cases/{resource}_usecase.py
from mangacollec.domain import I

{Resource}
Repository
from mangacollec.domain.entities import

{Resource}
from mangacollec.application import Create

{Resource}, Search
{Resource}


class Search{Resource}UseCase:
    """Cas d'utilisation : rechercher des {resource}s."""

    def __init__(self, repo: I{Resource}

    Repository) -> None:
    self.repo = repo


def __call__(self, search_{Resource}: Search


{Resource}) -> list[{Resource}] | None:
all_
{Resource}
_usecase = GetAll
{Resource}
UseCase(self.repo)
all_
{Resource}
s = all_resource_usecase()
# code pour filtrer all_{Resource}s selon search_{Resource}...
return self.repo.search(criteria)

# Ajouter Create/Update/Delete SEULEMENT si supportés par l'API
```

### 5. Service API (Infrastructure Layer)

**CRITICAL**: Tous les repositories API DOIVENT utiliser le service MangaCollecAPI pour les appels HTTP.

```python
# src/infrastructure/services/mangacollec_api_interface.py
from abc import ABC, abstractmethod

class IMangaCollecAPI(ABC):
    """Interface pour le client MangaCollec API."""

    BASE_URL: str = "https://api.mangacollec.com/"
    TOKEN_URL: str = f"{BASE_URL}oauth/token/"

    # Authentification automatique via OAuth2
    # Support: client_credentials et password grant
    def __init__(self, client: ClientMangaCollec, proxy: dict[str, str] | None = None)

    @abstractmethod
    def get(self, endpoint: str, params: dict | None = None) -> dict | list:
        """Effectue une requête GET authentifiée."""
        pass

    @abstractmethod
    def post(self, endpoint: str, data: dict | None = None) -> dict | list:
        """Effectue une requête POST authentifiée."""
        pass
```

```python
# src/infrastructure/services/mangacollec_api.py
class MangaCollecAPI(IMangaCollecAPI):
    """Implémentation du client MangaCollec API avec authentification OAuth2."""

    # GESTION AUTOMATIQUE DES TOKENS:
    # - Authentification initiale
    # - Rafraîchissement automatique du token
    # - Gestion des erreurs 401/403

    def get(self, endpoint: str, params: dict | None = None) -> dict | list:
        # Ajoute automatiquement: Authorization: Bearer {token}
        # Gère le rafraîchissement si token expiré
        # Timeout: 30 secondes
        return self._call_request("GET", endpoint, params=params)
```

### 6. Mapper (Application Layer)

**OBLIGATOIRE**: Utiliser des mappers pour convertir entre les réponses API et les entités du domaine.

**CRITICAL**: TOUS les mappers DOIVENT suivre le pattern établi par `AuthorMapper`.

#### Template de Référence

📖 **Voir** : `datas/_exemple/mappers/resource_mapper_template.md` pour le template complet avec checklist.

#### Méthodes Obligatoires

Chaque mapper DOIT implémenter au minimum :

```python
# src/application/mappers/{resource}_mapper.py
from mangacollec.application import Get

{Resource}
ByIdV2Response
from mangacollec.domain.entities import

{Resource}


class {Resource}Mapper:
    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        """Convertit la réponse API en entité du domaine."""
        return {Resource}(
            id=data["id"],  # Champs obligatoires sans .get()
            name=data["name"],
            # Gérer les champs optionnels avec .get()
            first_name=data.get("first_name"),
            # Valeurs par défaut pour les champs manquants
            tasks_count=data.get("tasks_count", 0),
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        """Convertit l'entité du domaine en dictionnaire."""
        return {
            "id": resource.id,
            "name": resource.name,
            "first_name": resource.first_name,
            "tasks_count": resource.tasks_count,
        }
```

#### Méthodes Conditionnelles

**OBLIGATOIRE** si endpoint GET /v2/{resources}/{id} retourne une structure normalisée :

```python
    @staticmethod
    def from_api_response(response: dict) -> Get{Resource}ByIdV2Response:
        """Convertit la réponse complète de l'API V2 en Get{Resource}ByIdV2Response.

        Args:
            response: Réponse API contenant {resources} et entités liées

        Returns:
            Get{Resource}ByIdV2Response contenant toutes les entités converties
        """
        # Convertir les {resources} (liste)
        {resources} = [
            {Resource}Mapper.from_dict(resource_data)
            for resource_data in response.get("{resources}", [])
        ]

        # Convertir les entités liées via leurs mappers
        related = [
            RelatedMapper.from_dict(related_data)
            for related_data in response.get("related", [])
        ]

        return Get{Resource}ByIdV2Response(
            {resources}={resources},
            related=related,
        )
```

**OBLIGATOIRE** si endpoint GET /v2/{resources}/ existe :

```python
    @staticmethod
    def from_all_{resources}_response(response: dict) -> GetAll{Resource}sV2Response:
        """Convertit la réponse de l'API V2 pour get_all."""
        {resources} = [
            {Resource}Mapper.from_dict(resource_data)
            for resource_data in response.get("{resources}", [])
        ]
        return GetAll{Resource}sV2Response({resources}={resources})
```

#### Règles Strictes des Mappers

15. **Structure des DTOs de Réponse**
    - **TOUJOURS** utiliser des listes pour les entités, même s'il n'y a qu'un élément
    - **JAMAIS** utiliser le singulier pour les entités (ex: `publisher: Publisher`)
    - **TOUJOURS** utiliser le pluriel (ex: `publishers: list[Publisher]`)

16. **Gestion des champs**
    - **TOUJOURS** utiliser `data["field"]` pour les champs obligatoires
    - **TOUJOURS** utiliser `data.get("field")` pour les champs optionnels
    - **TOUJOURS** fournir une valeur par défaut pour les compteurs (ex: `count=0`)

17. **Imports des mappers liés**
    - **TOUJOURS** importer les mappers des entités liées
    - **TOUJOURS** utiliser ces mappers pour la conversion
    - **JAMAIS** créer directement une entité sans passer par son mapper

18. **Gestion des listes vides**
    - **TOUJOURS** utiliser `response.get("key", [])` pour les listes
    - **JAMAIS** supposer qu'une clé existe dans la réponse

#### Exemples de Référence

- **Mapper Complet avec relations** : `src/application/mappers/author_mapper.py`
- **Mapper Simple** : `src/application/mappers/edition_mapper.py`
- **Template** : `datas/_exemple/mappers/resource_mapper_template.md`

### 7. API Repository (Infrastructure Layer)

**CRITICAL**: Les repositories API DOIVENT suivre le pattern établi par `APIAuthorRepository`.

#### Template de Référence

📖 **Voir** : `datas/_exemple/repositories/api_repository_template.md` pour le template complet.

#### Structure Standard

```python
# src/infrastructure/repositories/api/api_{resource}_repository.py
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
        """Initialise le repository avec un client API authentifié.

        Args:
            client_api: Instance de MangaCollecAPI déjà authentifiée
        """
        self.client_api = client_api

    def get_by_id_v2(self, {resource}_id: str) -> Get{Resource}

    ByIdV2Response:
    """Récupère un(e) {resource} par son ID avec toutes ses relations via l'API.

    Args:
        {resource}_id: UUID du/de la {resource}

    Returns:
        Get{Resource}ByIdV2Response contenant toutes les entités

    Raises:
        {Resource}NotFoundException: Si le/la {resource} n'existe pas
    """
    try:
        response = self.client_api.get(f"/v2/{resources}/{{{resource}_id}}")

        if not response.get("{resources}") or len(response["{resources}"]) == 0:
            raise {Resource}
            NotFoundException({resource}
            _id)

            # ✅ CORRECT : Déléguer au mapper
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
"""Récupère tous les {resources} via l'API.

Returns:
    GetAll{Resource}sV2Response contenant la liste des {resources}
"""
try:
    response = self.client_api.get("/v2/{resources}/")

    # ✅ CORRECT : Déléguer au mapper
    return {Resource}
    Mapper.from_all_
    {resources}
    _response(response)

except Exception as e:
    raise RuntimeError(f"Failed to retrieve {resources}: {{e}}") from e
```

#### Règles Strictes des Repositories

19. **Utilisation du Service API**
    - **TOUJOURS** utiliser `IMangaCollecAPI` injecté dans le constructeur
    - **JAMAIS** utiliser `requests` directement
    - **JAMAIS** gérer l'authentification manuellement

20. **Conversion via Mappers**
    - **TOUJOURS** déléguer la conversion au mapper
    - **TOUJOURS** utiliser `{Resource}Mapper.from_api_response()` pour get_by_id
    - **TOUJOURS** utiliser `{Resource}Mapper.from_all_{resources}_response()` pour get_all
    - **JAMAIS** faire de conversion manuelle dans le repository

21. **Gestion des Erreurs**
    - **TOUJOURS** vérifier que la réponse contient des données
    - **TOUJOURS** convertir les erreurs API en exceptions de domaine
    - **TOUJOURS** utiliser `{Resource}NotFoundException` pour les 404
    - **JAMAIS** laisser remonter des exceptions HTTP brutes

22. **Simplicité du Code**
    - Chaque méthode doit faire **3-5 lignes maximum**
    - **AUCUNE logique métier** dans le repository
    - **AUCUNE conversion manuelle** (déléguer au mapper)
    - **UNE méthode = UN appel API + UN appel mapper**

#### Exemples de Référence

- **Repository Complet** : `src/infrastructure/repositories/api/api_author_repository.py`
- **Repository Simple** : `src/infrastructure/repositories/api/api_edition_repository.py`
- **Template** : `datas/_exemple/repositories/api_repository_template.md`

#### Comparaison : Incorrect vs Correct

**❌ INCORRECT** : Conversion manuelle (EditionRepository ancien)

```python
def get_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
    response = self.client_api.get(f"/v2/editions/{edition_id}")

    # ❌ Conversion manuelle (25 lignes)
    editions = [EditionMapper.from_dict(e) for e in response["editions"]]
    publishers = [PublisherMapper.from_dict(p) for p in response["publishers"]]
    series = [SerieMapper.from_dict(s) for s in response["series"]]
    types = [TypeSerieMapper.from_dict(t) for t in response["types"]]
    volumes = [VolumeMapper.from_dict(v) for v in response["volumes"]]

    return GetEditionByIdV2Response(
        editions=editions,
        publishers=publishers,
        series=series,
        types=types,
        volumes=volumes,
    )
```

**✅ CORRECT** : Délégation au mapper (AuthorRepository / EditionRepository nouveau)

```python
def get_by_id_v2(self, edition_id: str) -> GetEditionByIdV2Response:
    response = self.client_api.get(f"/v2/editions/{edition_id}")

    if not response.get("editions") or len(response["editions"]) == 0:
        raise EditionNotFoundException(edition_id)

    # ✅ Délégation au mapper (3 lignes)
    return EditionMapper.from_api_response(response)
```

### 8. InMemory Repository (Infrastructure Layer)

```python
# src/infrastructure/repositories/memory/inmemory_{resource}_repository.py
from mangacollec.domain

{resource}
_entity
import

{Resource}
from mangacollec.domain.repositories

{resource}
_repository
import I

{Resource}
Repository


class InMemory{Resource}Repository(I{Resource}Repository):
    """Implémentation en mémoire du repository {Resource} (tests/dev)."""

    def __init__(self) -> None:
        self._data: dict[str, {Resource}] = {}

    def get_by_id(self, id: str) -> {Resource} | None:
        return self._data.get(id)

    def get_all(self) -> list[{Resource}]:
        return list(self._data.values())

    # InMemory peut implémenter TOUTES les méthodes pour les tests
    # même si l'API ne les supporte pas
```

---

## Workflow de Développement

## Service API et Authentification

### Utilisation de MangaCollecAPI

**CRITICAL**: TOUS les repositories API doivent utiliser le service MangaCollecAPI pour la communication avec l'API externe.

#### Initialisation du client API

```python
from mangacollec.infrastructure.services import MangaCollecAPI
from mangacollec.domain.entities import ClientMangaCollec

# Création du client avec credentials
client = ClientMangaCollec(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="optional_username",  # Optionnel
    password="optional_password"  # Optionnel
)

# Initialisation du service API (authentification automatique)
api_service = MangaCollecAPI(client=client)

# Utilisation dans un repository
repository = APIAuthorRepository(api_service)
```

#### Types d'authentification supportés

1. **Client Credentials** (par défaut):
   - Utilise `client_id` et `client_secret`
   - Pour accès public/applicatif

2. **Password Grant** (optionnel):
   - Utilise `username` et `password` en plus des credentials
   - Pour accès utilisateur spécifique
   - Permet le rafraîchissement automatique via `refresh_token`

#### Fonctionnalités automatiques

- **Gestion des tokens**: Authentification et rafraîchissement automatiques
- **Timeout**: 30 secondes pour toutes les requêtes
- **Retry**: Tentative de rafraîchissement si token expiré
- **Headers**: Ajout automatique de `Authorization: Bearer {token}`
- **Proxy**: Support optionnel via paramètre `proxy`

---

## Workflow de Développement

### Ajout d'une nouvelle ressource

1. **CRITICAL - Analyser la documentation disponible**

   **TOUJOURS vérifier les 3 sources de documentation dans cet ordre :**

   a. **Endpoints disponibles** :
   ```bash
   ls datas/{resource}/endpoints/
   ```

   b. **Repository documentation** :
   ```bash
   cat datas/{resource}/repository/repository.md
   ```
   Liste TOUTES les méthodes disponibles dans le repository avec leurs endpoints

   c. **Use Cases disponibles** :
   ```bash
   ls datas/{resource}/use_cases/
   ```
   Description métier de chaque cas d'utilisation

   d. **Réponses JSON brutes** (pour la structure des données) :
   ```bash
   ls datas/_endpoints/{resource}/
   ```

2. **Identifier les actions supportées**
   - Lire `datas/{resource}/repository/repository.md` pour connaître TOUTES les méthodes disponibles
   - Vérifier les fichiers `.md` dans `datas/{resource}/endpoints/` pour les détails techniques
   - Consulter `datas/{resource}/use_cases/*.md` pour comprendre le contexte métier

3. **Identifier les méthodes du mapper à implémenter**

   Selon les endpoints disponibles, déterminer quelles méthodes du mapper sont nécessaires :

   | Endpoint disponible | Méthode mapper à implémenter |
   |---------------------|------------------------------|
   | GET /v2/{resources}/ | `from_all_{resources}_response()` |
   | GET /v2/{resources}/{id} (avec relations) | `from_api_response()` |
   | GET /v2/{resources}/{id} (simple) | Uniquement `from_dict()` |
   | Besoin d'affichage liste | `to_list_item()` |

4. **Créer les fichiers dans l'ordre :**

   **📖 Pattern de Référence** : `AuthorMapper` (mapper complet avec relations)

   #### Phase 1 : Domain Layer
   - [ ] `tests/domain/entities/test_{resource}_entity.py`
   - [ ] `src/domain/entities/{resource}.py` (Entity)
   - [ ] `src/domain/repositories/{resource}_repository.py` (Interface Repository)

   #### Phase 2 : Application Layer - DTOs
   - [ ] `tests/application/dto/responses/test_{resource}_responses.py`
   - [ ] `src/application/dto/responses/{resource}_responses.py`
     - [ ] `Get{Resource}ByIdV2Response` (si endpoint get_by_id existe)
     - [ ] `GetAll{Resource}sV2Response` (si endpoint get_all existe)

   #### Phase 3 : Application Layer - Mapper
   - [ ] `tests/application/mappers/test_{resource}_mapper.py`
   - [ ] `src/application/mappers/{resource}_mapper.py`
     - [ ] Méthode `from_dict()` (OBLIGATOIRE)
     - [ ] Méthode `to_dict()` (OBLIGATOIRE)
     - [ ] Méthode `from_api_response()` (si structure normalisée)
     - [ ] Méthode `from_all_{resources}_response()` (si endpoint get_all existe)
     - [ ] Méthode `to_list_item()` (optionnel)

   **CRITICAL** : Consulter `datas/_exemple/mappers/resource_mapper_template.md` pour le pattern exact.

   #### Phase 4 : Application Layer - Use Cases
   - [ ] `src/application/use_cases/{resource}_usecase.py`
     - [ ] `Get{Resource}ByIdUseCase` (si supporté)
     - [ ] `GetAll{Resource}sUseCase` (si supporté)
     - [ ] `Search{Resource}UseCase` (optionnel, filtrage en mémoire)
     - [ ] `Create{Resource}UseCase` (si supporté)
     - [ ] `Update{Resource}UseCase` (si supporté)
     - [ ] `Delete{Resource}UseCase` (si supporté)

   #### Phase 5 : Infrastructure Layer
   - [ ] `tests/infrastructure/repositories/test_api_{resource}_repository.py`
   - [ ] `src/infrastructure/repositories/api/api_{resource}_repository.py`
     - [ ] Injection de `IMangaCollecAPI` dans le constructeur
     - [ ] Utilisation de `{Resource}Mapper.from_api_response()` pour les conversions
   - [ ] `tests/infrastructure/repositories/test_inmemory_{resource}_repository.py`
   - [ ] `src/infrastructure/repositories/memory/inmemory_{resource}_repository.py`

5. **Valider** que seules les méthodes supportées sont dans l'interface

### Checklist de Validation Finale

Avant de considérer la ressource comme complète, vérifier :

- [ ] **Documentation vérifiée**
  - [ ] `datas/{resource}/repository/repository.md` existe et documente les méthodes
  - [ ] Tous les endpoints ont leur fichier `.md` dans `datas/{resource}/endpoints/`
  - [ ] Les use cases sont documentés dans `datas/{resource}/use_cases/`

- [ ] **Mapper conforme au pattern**
  - [ ] Toutes les méthodes obligatoires sont implémentées
  - [ ] Les imports des mappers liés sont corrects
  - [ ] Les DTOs utilisent des listes (pluriel) et non des entités uniques
  - [ ] Gestion correcte des champs optionnels avec `.get()`

- [ ] **Repository API conforme**
  - [ ] Utilise `IMangaCollecAPI` (pas `requests`)
  - [ ] Utilise les mappers pour toutes les conversions
  - [ ] Gère les erreurs avec des exceptions de domaine

- [ ] **Tests**
  - [ ] Couverture ≥ 90%
  - [ ] Tests unitaires utilisent `InMemory{Resource}Repository`
  - [ ] Tests d'intégration pour le repository API (optionnel)

- [ ] **Qualité du code**
  - [ ] Formatage avec `ruff format`
  - [ ] Linting avec `ruff check`
  - [ ] Type hints partout
  - [ ] Docstrings au format Google

---

## Règles Strictes

1. **Ne jamais ajouter de méthode non supportée par l'API** dans `I{Resource}Repository`
2. **CRITICAL - Toujours vérifier la documentation dans cet ordre** :
   - `datas/{resource}/repository/repository.md` (source de vérité pour les méthodes disponibles)
   - `datas/{resource}/endpoints/*.md` (détails techniques)
   - `datas/{resource}/use_cases/*.md` (contexte métier)
3. **Les Use Cases dépendent UNIQUEMENT des interfaces**, jamais des implémentations
4. **Un Use Case = Une responsabilité** (Single Responsibility)
5. **Les DTOs sont immuables** (utiliser `@dataclass(frozen=True)` si nécessaire)
6. **Les Entities du domaine ne dépendent de rien d'externe**
7. **Utiliser des mappers** pour convertir entre Entities et DTOs
8. **Les tests unitaires doivent utiliser `InMemory{Resource}Repository`**
9. **Le code doit respecter les règles ruff** (formatage, linting, typage)**
10. **Les tests doivent couvrir au moins 90% du code et doivent être pertinents**
### Règles pour les repositories API
**CRITICAL**: Ces règles sont OBLIGATOIRES pour tous les repositories API.

11. **TOUJOURS utiliser MangaCollecAPI** pour les appels HTTP
    - **NEVER** utiliser `requests` directement dans un repository
    - **NEVER** gérer l'authentification manuellement
    - **TOUJOURS** injecter `IMangaCollecAPI` dans le constructeur

12. **TOUJOURS utiliser les mappers** pour la conversion
    - **TOUJOURS** utiliser `{Resource}Mapper.from_dict()` pour convertir API → Entité
    - **TOUJOURS** utiliser `{Resource}Mapper.to_dict()` pour convertir Entité → API
    - **NEVER** créer directement les entités depuis les réponses API

13. **Gestion des erreurs**
    - **TOUJOURS** convertir les erreurs API en exceptions de domaine
    - **TOUJOURS** utiliser `AuthorNotFoundException` pour les 404
    - **NEVER** laisser remonter des exceptions HTTP brutes

14. **Format des réponses API V2**
    - Les réponses sont normalisées: `{"resource_name": [data...]}`
    - **TOUJOURS** accéder aux données via `response['{resource}s'][0]` pour get_by_id
    - **TOUJOURS** itérer sur `response['{resource}s']` pour get_all

### Exemple d'implémentation correcte

```python
# ✅ CORRECT - Utilisation du service API et mapper
class APIAuthorRepository(IAuthorRepository):
    def __init__(self, client_api: IMangaCollecAPI) -> None:
        self.client_api = client_api

    def get_by_id(self, author_id: str) -> Author:
        response = self.client_api.get(f'/v2/_exemple/{author_id}')
        author_data = response['_exemple'][0]
        return AuthorMapper.from_dict(author_data)

# ❌ INCORRECT - Utilisation directe de requests
class APIAuthorRepository(IAuthorRepository):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url  # ❌ Pas de gestion d'authentification

    def get_by_id(self, author_id: str) -> Author:
        response = requests.get(f"{self.base_url}/v2/_exemple/{author_id}")  # ❌ Mauvais
        return Author(...)  # ❌ Pas de mapper
```---

## Exemple Complet : Resource "Author"

### Vérification de la documentation

```bash
# 1. Repository (source de vérité)
$ cat datas/authors/repository/repository.md
# APIAuthorRepository
# Méthodes Disponibles:
# - get_all_authors_v2() -> GET /v2/authors
# - get_author_by_id_v2(author_id: str) -> GET /v2/authors/{author_id}

# 2. Endpoints disponibles
$ ls datas/authors/endpoints/
author_v2.md    # GET /v2/authors/{id} ✅
authors_v2.md   # GET /v2/authors/ ✅

# 3. Use Cases disponibles
$ ls datas/authors/use_cases/
get_all_v2.md   # GetAllAuthorsV2 ✅
get_by_id_v2.md # GetByIdAuthorV2 ✅

# Conclusion: Lecture seule (pas de create/update/delete)
```

### Interface Repository
```python
class IAuthorRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Author | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Author]:
        pass

    # PAS de create/update/delete car non supportés
```

### Use Cases disponibles
- `GetByIdAuthorUseCase` ✅
- `GetAllAuthorUseCase` ✅
- `SearchAuthorUseCase` ✅ (filtrage en mémoire sur get_all)
- ~~`CreateAuthorUseCase`~~ ❌
- ~~`UpdateAuthorUseCase`~~ ❌
- ~~`DeleteAuthorUseCase`~~ ❌

---

## Notes Techniques

- **Python version** : 3.10+
- **Type hints** : Obligatoires partout
- **Docstrings** : Format Google style
- **Tests** : Utiliser `InMemory*Repository` pour les tests unitaires