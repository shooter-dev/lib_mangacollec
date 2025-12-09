# Patterns de Mapper - Guide de Sélection

Ce document vous aide à choisir le bon pattern de mapper selon les endpoints disponibles pour votre ressource.

## 📊 Tableau de Décision

| Endpoint Disponible | Pattern | Exemple | Méthodes à Implémenter |
|---------------------|---------|---------|------------------------|
| GET list + GET by_id (avec relations) | **Complet** | `AuthorMapper` | `from_dict()`, `to_dict()`, `from_api_response()`, `from_all_{resources}_response()` |
| GET by_id uniquement (avec relations) | **Simple** | `EditionMapper` | `from_dict()`, `to_dict()`, `from_api_response()` |
| GET simple sans relations | **Basique** | `JobMapper`, `PublisherMapper` | `from_dict()`, `to_dict()` |
| Besoin d'affichage liste simplifié | **Avec ListItem** | `AuthorMapper` | Ajouter `to_list_item()` |

## 🎯 Pattern Complet (Author)

### Cas d'Usage

- ✅ Endpoint GET /v2/{resources}/ existe
- ✅ Endpoint GET /v2/{resources}/{id} retourne une structure normalisée avec plusieurs entités
- ✅ Besoin d'un affichage liste simplifié (optionnel)

### Structure du Fichier

```python
from mangacollec.application import (
    GetAll

{Resource}
sV2Response,
Get
{Resource}
ByIdV2Response,
)
from mangacollec.application.mappers import Related1Mapper
from mangacollec.application.mappers import Related2Mapper
from mangacollec.domain.entities import

{Resource}, {Resource}
ListItem, Related1, Related2


class {Resource}Mapper:
    """Mapper pour convertir entre API et entités du domaine."""

    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        """Convertit la réponse API en entité {Resource}."""
        return {Resource}(
            id=data["id"],
            name=data["name"],
            first_name=data.get("first_name"),
            tasks_count=data.get("tasks_count", 0),
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        """Convertit l'entité {Resource} en dictionnaire."""
        return {
            "id": resource.id,
            "name": resource.name,
            "first_name": resource.first_name,
            "tasks_count": resource.tasks_count,
        }

    @staticmethod
    def to_list_item(resource: {Resource}) -> {Resource}ListItem:

    """Convertit une entité {Resource} en {Resource}ListItem."""
    first_name = resource.first_name if resource.first_name else ""
    full_name = f"{first_name} {resource.name}".strip()

    return {Resource}
    ListItem(
        id=resource.id,
        full_name=full_name,
    )


@staticmethod
def from_all_{resources}


_response(response: dict) -> GetAll
{Resource}
sV2Response:
"""Convertit la réponse de l'API V2 pour get_all."""
{resources} = [
    {Resource}Mapper.from_dict(resource_data)
for resource_data in response.get("{resources}", [])
]
return GetAll
{Resource}
sV2Response({resources} = {resources})

@staticmethod
def from_api_response(response: dict) -> Get{Resource}


ByIdV2Response:
"""Convertit la réponse complète de l'API V2."""
# Convertir les {resources} (liste)
{resources} = [
    {Resource}Mapper.from_dict(resource_data)
for resource_data in response.get("{resources}", [])
]

# Convertir les entités liées
related1 = [
    Related1Mapper.from_dict(r1_data)
    for r1_data in response.get("related1", [])
]

related2 = [
    Related2Mapper.from_dict(r2_data)
    for r2_data in response.get("related2", [])
]

return Get
{Resource}
ByIdV2Response(
    {resources} = {resources},
related1 = related1,
related2 = related2,
)
```

### DTOs Nécessaires

```python
@dataclass(frozen=True)
class GetAll{Resource}sV2Response:
    """Réponse pour GetAll{Resource}sV2."""
    {resources}: list[{Resource}]

@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    """Réponse pour Get{Resource}ByIdV2."""
    {resources}: list[{Resource}]
    related1: list[Related1]
    related2: list[Related2]
```

### Référence Complète

📖 **Fichier** : `src/application/mappers/author_mapper.py`

---

## 🔧 Pattern Simple (Edition)

### Cas d'Usage

- ❌ Pas d'endpoint GET /v2/{resources}/ (pas de liste)
- ✅ Endpoint GET /v2/{resources}/{id} retourne une structure normalisée avec plusieurs entités

### Structure du Fichier

```python
from mangacollec.application import Get

{Resource}
ByIdV2Response
from mangacollec.application.mappers import Related1Mapper
from mangacollec.application.mappers import Related2Mapper
from mangacollec.domain.entities import

{Resource}


class {Resource}Mapper:
    """Mapper pour convertir entre API et entités {Resource} du domaine."""

    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        """Convertit la réponse API en entité {Resource}."""
        return {Resource}(
            id=data["id"],
            title=data.get("title"),
            series_id=data["series_id"],
            volumes_count=data["volumes_count"],
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        """Convertit l'entité {Resource} en dictionnaire."""
        return {
            "id": resource.id,
            "title": resource.title,
            "series_id": resource.series_id,
            "volumes_count": resource.volumes_count,
        }

    @staticmethod
    def from_api_response(response: dict) -> Get{Resource}

    ByIdV2Response:
    """Convertit la réponse complète de l'API V2."""
    # Convertir les {resources} (liste)
    {resources} = [
        {Resource}Mapper.from_dict(resource_data)
    for resource_data in response.get("{resources}", [])
    ]

    # Convertir les entités liées
    related1 = [
        Related1Mapper.from_dict(r1_data)
        for r1_data in response.get("related1", [])
    ]

    return Get
    {Resource}
    ByIdV2Response(
        {resources} = {resources},
    related1 = related1,
    )
```

### DTOs Nécessaires

```python
@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    """Réponse pour Get{Resource}ByIdV2."""
    {resources}: list[{Resource}]
    related1: list[Related1]
```

### Référence Complète

📖 **Fichier** : `src/application/mappers/edition_mapper.py`

---

## ⚡ Pattern Basique (Job, Publisher, Serie)

### Cas d'Usage

- ❌ Pas d'endpoint GET list
- ✅ Endpoint GET by_id retourne UNIQUEMENT l'entité, sans relations
- ❌ Pas de structure normalisée V2

### Structure du Fichier

```python
from mangacollec.domain.entities import

{Resource}


class {Resource}Mapper:
    """Mapper pour convertir entre API et entités {Resource} du domaine."""

    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        """Convertit la réponse API en entité {Resource}."""
        return {Resource}(
            id=data["id"],
            title=data["title"],
            count=data.get("count", 0),
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        """Convertit l'entité {Resource} en dictionnaire."""
        return {
            "id": resource.id,
            "title": resource.title,
            "count": resource.count,
        }
```

### DTOs Nécessaires

Aucun DTO de réponse spécifique nécessaire si la ressource est utilisée uniquement comme entité liée.

### Références

📖 **Fichiers** :
- `src/application/mappers/job_mapper.py`
- `src/application/mappers/publisher_mapper.py`
- `src/application/mappers/serie_mapper.py`

---

## 🎨 Pattern Avec ListItem

### Cas d'Usage

- Besoin d'un affichage liste simplifié (ex: autocomplete, dropdown)
- Combinaison de plusieurs champs pour créer un nom d'affichage

### Méthode Supplémentaire

```python
@dataclass
class {Resource}ListItem:
    """Entité simplifiée pour affichage en liste."""
    id: str
    display_name: str

class {Resource}Mapper:
    # ... autres méthodes ...

    @staticmethod
    def to_list_item(resource: {Resource}) -> {Resource}ListItem:
        """Convertit une entité {Resource} en {Resource}ListItem."""
        # Exemple : combiner first_name et name
        first_name = resource.first_name if resource.first_name else ""
        display_name = f"{first_name} {resource.name}".strip()

        return {Resource}ListItem(
            id=resource.id,
            display_name=display_name,
        )
```

### Exemple d'Utilisation

```python
# Récupérer tous les auteurs
authors = author_repository.get_all()

# Convertir en liste pour affichage
author_list_items = [AuthorMapper.to_list_item(author) for author in authors]

# Affichage dans un dropdown
for item in author_list_items:
    print(f"{item.id}: {item.display_name}")
```

---

## 🔍 Comment Choisir le Pattern ?

### Étape 1 : Vérifier les Endpoints Disponibles

```bash
# Source de vérité
cat datas/{resource}/repository/repository.md
```

### Étape 2 : Répondre aux Questions

1. **Y a-t-il un endpoint GET /v2/{resources}/ ?**
   - ✅ Oui → Pattern Complet
   - ❌ Non → Question suivante

2. **L'endpoint GET by_id retourne-t-il une structure normalisée avec plusieurs types d'entités ?**
   - ✅ Oui → Pattern Simple
   - ❌ Non → Pattern Basique

3. **Y a-t-il besoin d'un affichage liste simplifié ?**
   - ✅ Oui → Ajouter `to_list_item()`
   - ❌ Non → Pattern de base suffit

### Étape 3 : Consulter l'Exemple de Référence

| Pattern | Référence |
|---------|-----------|
| Complet | `src/application/mappers/author_mapper.py` |
| Simple | `src/application/mappers/edition_mapper.py` |
| Basique | `src/application/mappers/job_mapper.py` |

---

## ⚠️ Règles Communes à Tous les Patterns

### 1. Structure des DTOs

- **TOUJOURS** utiliser des listes (pluriel)
- **JAMAIS** utiliser le singulier

```python
# ❌ INCORRECT
@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    resource: {Resource}  # Singulier
    related: RelatedEntity  # Singulier

# ✅ CORRECT
@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    resources: list[{Resource}]  # Pluriel, liste
    related: list[RelatedEntity]  # Pluriel, liste
```

### 2. Gestion des Champs

```python
# Champs obligatoires : sans .get()
id=data["id"]
name=data["name"]

# Champs optionnels : avec .get()
first_name=data.get("first_name")
description=data.get("description")

# Compteurs : avec valeur par défaut
count=data.get("count", 0)
tasks_count=data.get("tasks_count", 0)
```

### 3. Imports des Mappers Liés

```python
# TOUJOURS importer les mappers des entités liées
from mangacollec.application.mappers import RelatedMapper

# TOUJOURS utiliser ces mappers pour la conversion
related = [
    RelatedMapper.from_dict(related_data)
    for related_data in response.get("related", [])
]

# JAMAIS créer directement l'entité
# ❌ related = [RelatedEntity(**r) for r in response.get("related", [])]
```

### 4. Gestion des Listes Vides

```python
# TOUJOURS utiliser .get() avec [] comme défaut
response.get("related", [])

# JAMAIS supposer qu'une clé existe
# ❌ response["related"]
```

---

## 📚 Ressources Complémentaires

- **Template Complet** : `datas/_exemple/mappers/resource_mapper_template.md`
- **Guide de Démarrage** : `datas/_exemple/QUICK_START.md`
- **Documentation** : `CLAUDE.md`

---

## 🎯 Checklist de Validation

Avant de considérer votre mapper comme conforme au pattern Author :

- [ ] **Pattern correctement identifié**
  - [ ] Endpoints disponibles vérifiés dans `repository.md`
  - [ ] Pattern choisi selon les critères

- [ ] **Méthodes implémentées**
  - [ ] `from_dict()` et `to_dict()` (obligatoires)
  - [ ] `from_api_response()` si structure normalisée
  - [ ] `from_all_{resources}_response()` si endpoint GET list existe
  - [ ] `to_list_item()` si besoin d'affichage liste

- [ ] **DTOs conformes**
  - [ ] Tous les champs sont des listes (pluriel)
  - [ ] `@dataclass(frozen=True)` utilisé
  - [ ] Docstring présente

- [ ] **Imports corrects**
  - [ ] Imports des mappers liés
  - [ ] Imports des DTOs de réponse
  - [ ] Imports des entités du domaine

- [ ] **Code de qualité**
  - [ ] Type hints partout
  - [ ] Docstrings Google
  - [ ] Gestion correcte des champs optionnels
