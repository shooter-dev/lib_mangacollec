# Template de Repository API - Pattern Standard

Ce template suit le pattern établi par `APIAuthorRepository` pour garantir la cohérence dans tous les repositories API.

## 🎯 Règles Fondamentales

1. **TOUJOURS** utiliser `IMangaCollecAPI` (jamais `requests`)
2. **TOUJOURS** utiliser les mappers pour les conversions
3. **JAMAIS** faire de conversion manuelle dans le repository
4. **TOUJOURS** déléguer la conversion au mapper via `from_api_response()`

## Structure du Repository API

```python
"""Implémentation du repository {Resource} via l'API MangaCollec.

This module provides the API implementation of the {Resource} repository.
"""

from mangacollec.application import (
    GetAll

{Resource}
sV2Response,  # Si endpoint GET list existe
Get
{Resource}
ByIdV2Response,  # Si endpoint GET by_id existe
)
from mangacollec.application import IMangaCollecAPI
from mangacollec.application.mappers

{resource}
_mapper
import

{Resource}
Mapper
from mangacollec.domain.entities import

{Resource}
ListItem  # Si méthode get_list existe
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

    # =====================================================================
    # MÉTHODE OBLIGATOIRE si endpoint GET /v2/{resources}/{id} existe
    # =====================================================================
    def get_by_id_v2(self, {resource}_id: str) -> Get{Resource}

    ByIdV2Response:
    """Récupère un(e) {resource} par son ID avec toutes ses relations via l'API.

    Args:
        {resource}_id: UUID du/de la {resource}

    Returns:
        Get{Resource}ByIdV2Response contenant:
            - {resources}: Liste des {resources}
            - [autres entités liées selon l'API]

    Raises:
        {Resource}NotFoundException: Si le/la {resource} n'existe pas
    """
    try:
        response = self.client_api.get(f"/v2/{resources}/{{{resource}_id}}")

        if not response.get("{resources}") or len(response["{resources}"]) == 0:
            raise {Resource}
            NotFoundException({resource}
            _id)

            # ✅ CORRECT : Utiliser le mapper pour convertir toute la réponse API
            return {Resource}
            Mapper.from_api_response(response)

        except Exception as e:
        if isinstance(e, {Resource}NotFoundException):
            raise
        raise {Resource}
        NotFoundException({resource}
        _id) from e


# =====================================================================
# MÉTHODE OBLIGATOIRE si endpoint GET /v2/{resources}/ existe
# =====================================================================
def get_all_v2(self) -> GetAll{Resource}


sV2Response:
"""Récupère tous les {resources} via l'API.

Returns:
    GetAll{Resource}sV2Response contenant la liste des {resources}
"""
try:
    response = self.client_api.get("/v2/{resources}/")

    # ✅ CORRECT : Utiliser le mapper pour convertir la réponse
    return {Resource}
    Mapper.from_all_
    {resources}
    _response(response)

except Exception as e:
    raise RuntimeError(f"Failed to retrieve {resources}: {{e}}") from e


# =====================================================================
# MÉTHODE OPTIONNELLE - Liste simplifiée pour affichage
# =====================================================================
def get_list(self) -> list[{Resource}ListItem

]:
"""Récupère la liste simplifiée des {resources} (id + display_name).

Returns:
    Liste des entités {Resource}ListItem
"""
all_
{resources}
_response = self.get_all_v2()
return [{Resource}Mapper.to_list_item({resource})
for {resource} in all_{resources}_response.{resources}]


# =====================================================================
# MÉTHODE OPTIONNELLE si endpoint POST /v2/{resources}/ existe
# =====================================================================
def create(self, {resource}_data: Create{Resource}) -> {Resource}:
    """Crée un nouveau/une nouvelle {resource}.

    Args:
        {resource}_data: Données de création

    Returns:
        Entité {Resource} créée
    """
    try:
        # Convertir le DTO en dictionnaire via le mapper
        data = {Resource}
        Mapper.to_dict({resource}
        _data)

        response = self.client_api.post("/v2/{resources}/", data=data)

        # Convertir la réponse via le mapper
        return {Resource}
        Mapper.from_dict(response["{resource}"])

    except Exception as e:
        raise RuntimeError(f"Failed to create {resource}: {{e}}") from e


# =====================================================================
# MÉTHODE OPTIONNELLE si endpoint PUT/PATCH /v2/{resources}/{id} existe
# =====================================================================
def update(self, {resource}_id: str, {resource}_data: Update{Resource}) -> {Resource}:
    """Met à jour un(e) {resource}.

    Args:
        {resource}_id: UUID du/de la {resource}
        {resource}_data: Données de mise à jour

    Returns:
        Entité {Resource} mise à jour
    """
    try:
        data = {Resource}
        Mapper.to_dict({resource}
        _data)

        response = self.client_api.put(f"/v2/{resources}/{{{resource}_id}}", data=data)

        return {Resource}
        Mapper.from_dict(response["{resource}"])

    except Exception as e:
        raise RuntimeError(f"Failed to update {resource}: {{e}}") from e


# =====================================================================
# MÉTHODE OPTIONNELLE si endpoint DELETE /v2/{resources}/{id} existe
# =====================================================================
def delete(self, {resource}_id: str) -> None:
    """Supprime un(e) {resource}.

    Args:
        {resource}_id: UUID du/de la {resource}
    """
    try:
        self.client_api.delete(f"/v2/{resources}/{{{resource}_id}}")

    except Exception as e:
        raise RuntimeError(f"Failed to delete {resource}: {{e}}") from e
```

## ⚠️ Erreurs Courantes à Éviter

### ❌ Conversion Manuelle (INCORRECT)

```python
def get_by_id_v2(self, resource_id: str) -> Get{Resource}ByIdV2Response:
    response = self.client_api.get(f"/v2/{resources}/{resource_id}")

    # ❌ INCORRECT : Conversion manuelle
    resources = [
        {Resource}Mapper.from_dict(resource_data)
        for resource_data in response.get("{resources}", [])
    ]

    related = [
        RelatedMapper.from_dict(related_data)
        for related_data in response.get("related", [])
    ]

    return Get{Resource}ByIdV2Response(
        resources=resources,
        related=related,
    )
```

### ✅ Utilisation du Mapper (CORRECT)

```python
def get_by_id_v2(self, resource_id: str) -> Get{Resource}ByIdV2Response:
    response = self.client_api.get(f"/v2/{resources}/{resource_id}")

    # ✅ CORRECT : Déléguer au mapper
    return {Resource}Mapper.from_api_response(response)
```

---

### ❌ Utilisation de requests (INCORRECT)

```python
import requests

def get_by_id_v2(self, resource_id: str) -> Get{Resource}ByIdV2Response:
    # ❌ INCORRECT : Utilisation directe de requests
    response = requests.get(f"https://api.mangacollec.com/v2/{resources}/{resource_id}")
    data = response.json()
    return {Resource}Mapper.from_api_response(data)
```

### ✅ Utilisation de IMangaCollecAPI (CORRECT)

```python
def get_by_id_v2(self, resource_id: str) -> Get{Resource}ByIdV2Response:
    # ✅ CORRECT : Utilisation du service API
    response = self.client_api.get(f"/v2/{resources}/{resource_id}")
    return {Resource}Mapper.from_api_response(response)
```

---

## 📊 Patterns de Repository selon les Endpoints

| Endpoints Disponibles | Méthodes à Implémenter | Exemple |
|-----------------------|------------------------|---------|
| GET list + GET by_id | `get_all_v2()`, `get_by_id_v2()`, `get_list()` | `APIAuthorRepository` |
| GET by_id uniquement | `get_by_id_v2()` | `APIEditionRepository` |
| Avec CRUD complet | Ajouter `create()`, `update()`, `delete()` | (À venir) |

## 🎯 Checklist de Création

### Analyse Préalable

- [ ] Vérifier `datas/{resource}/repository/repository.md` pour les méthodes disponibles
- [ ] Identifier les endpoints dans `datas/{resource}/endpoints/`
- [ ] Vérifier que les mappers correspondants existent

### Implémentation

- [ ] Injection de `IMangaCollecAPI` dans le constructeur
- [ ] Méthode `get_by_id_v2()` si endpoint existe
  - [ ] Utilise `{Resource}Mapper.from_api_response()`
  - [ ] Gère `{Resource}NotFoundException`
  - [ ] Vérifie que la réponse contient des données

- [ ] Méthode `get_all_v2()` si endpoint existe
  - [ ] Utilise `{Resource}Mapper.from_all_{resources}_response()`
  - [ ] Gère les erreurs avec RuntimeError

- [ ] Méthode `get_list()` si nécessaire
  - [ ] Appelle `get_all_v2()`
  - [ ] Utilise `{Resource}Mapper.to_list_item()`

- [ ] Méthodes CRUD si supportées
  - [ ] `create()` avec `Create{Resource}` DTO
  - [ ] `update()` avec `Update{Resource}` DTO
  - [ ] `delete()` simple

### Validation

- [ ] Aucune conversion manuelle dans le repository
- [ ] Tous les appels API via `self.client_api`
- [ ] Toutes les conversions via les mappers
- [ ] Gestion des erreurs appropriée
- [ ] Type hints partout
- [ ] Docstrings au format Google

## 📚 Exemples de Référence

- **Repository Complet** : `src/infrastructure/repositories/api/api_author_repository.py`
- **Repository Simple** : `src/infrastructure/repositories/api/api_edition_repository.py`

## 🚨 Règles Strictes

1. **JAMAIS de conversion manuelle** : Toujours déléguer au mapper
2. **JAMAIS de requests direct** : Toujours utiliser `IMangaCollecAPI`
3. **TOUJOURS vérifier les données** : Checker que la réponse contient des données
4. **TOUJOURS gérer les exceptions** : Convertir en exceptions de domaine
5. **UN repository = UNE ressource** : Pas de logique métier complexe

## 💡 Avantages du Pattern

| Avantage | Description |
|----------|-------------|
| **Simplicité** | Méthodes courtes (3-5 lignes) |
| **Maintenabilité** | Logique de conversion centralisée dans les mappers |
| **Testabilité** | Facile à mocker `IMangaCollecAPI` |
| **Cohérence** | Même structure partout |
| **DRY** | Pas de duplication de code |

## 🔧 Commandes de Vérification

```bash
# Vérifier la syntaxe
python -m py_compile src/infrastructure/repositories/api/api_{resource}_repository.py

# Tester l'import
python -c "from src.infrastructure.repositories.api.api_{resource}_repository import API{Resource}Repository; print('OK')"

# Lancer les tests
pytest tests/infrastructure/repositories/api/test_api_{resource}_repository.py -v
```

## 📖 Documentation Complète

Pour plus de détails, consulter :
- `CLAUDE.md` - Section "7. API Repository (Infrastructure Layer)"
- `datas/_exemple/QUICK_START.md` - Guide de démarrage
