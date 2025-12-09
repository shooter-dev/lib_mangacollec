# Template de Mapper - Pattern Standard

Ce template suit le pattern établi par `AuthorMapper` pour garantir la cohérence dans toutes les ressources.

## Structure du Mapper

```python
"""Mapper pour la conversion entre les réponses API et les entités {Resource}.

This module provides mapping functions between API responses and {Resource} entities.
"""

from mangacollec.application import (
    GetAll

{Resource}
sV2Response,
Get
{Resource}
ByIdV2Response,
)
# Importer les mappers des entités liées si nécessaire
# from src.application.mappers.related_mapper import RelatedMapper
from mangacollec.domain.entities import

{Resource}


class {Resource}Mapper:
    """Mapper pour convertir entre API et entités {Resource} du domaine."""

    @staticmethod
    def from_dict(data: dict) -> {Resource}:
        """Convertit la réponse API en entité {Resource}.

        Args:
            data: Dictionnaire contenant les données de l'API

        Returns:
            Entité {Resource}
        """
        return {Resource}(
            id=data["id"],
            # Champs obligatoires
            name=data["name"],
            # Champs optionnels avec .get()
            description=data.get("description"),
            # Champs avec valeur par défaut
            count=data.get("count", 0),
        )

    @staticmethod
    def to_dict(resource: {Resource}) -> dict:
        """Convertit l'entité {Resource} en dictionnaire.

        Args:
            resource: Entité {Resource}

        Returns:
            Dictionnaire représentant la ressource
        """
        return {
            "id": resource.id,
            "name": resource.name,
            "description": resource.description,
            "count": resource.count,
        }

    # =====================================================================
    # MÉTHODE OBLIGATOIRE si endpoint GET /v2/{resources}/ existe
    # =====================================================================
    @staticmethod
    def from_all_{resources}

    _response(response: dict) -> GetAll
    {Resource}
    sV2Response:
    """Convertit la réponse de l'API V2 pour get_all en GetAll{Resource}sV2Response.

    Args:
        response: Réponse API contenant {resources}

    Returns:
        GetAll{Resource}sV2Response contenant la liste des ressources
    """
    # Convertir les {resources}
    {resources} = [
        {Resource}Mapper.from_dict(resource_data)
    for resource_data in response.get("{resources}", [])
    ]

    return GetAll
    {Resource}
    sV2Response({resources} = {resources})

    # =====================================================================
    # MÉTHODE OBLIGATOIRE si endpoint GET /v2/{resources}/{id} retourne
    # une structure normalisée avec plusieurs types d'entités
    # =====================================================================
    @staticmethod
    def from_api_response(response: dict) -> Get{Resource}

    ByIdV2Response:
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

    # Convertir les entités liées
    # Example: tasks, jobs, series, editions, volumes, etc.
    # tasks = [TaskMapper.from_dict(task_data) for task_data in response.get("tasks", [])]
    # jobs = [JobMapper.from_dict(job_data) for job_data in response.get("jobs", [])]

    return Get
    {Resource}
    ByIdV2Response(
        {resources} = {resources},
    # tasks=tasks,
    # jobs=jobs,
    # ... autres entités liées
    )

    # =====================================================================
    # MÉTHODE OPTIONNELLE - Uniquement si nécessaire pour l'affichage
    # =====================================================================
    @staticmethod
    def to_list_item(resource: {Resource}) -> {Resource}ListItem:

    """Convertit une entité {Resource} en {Resource}ListItem.

    Args:
        resource: Entité {Resource}

    Returns:
        Entité {Resource}ListItem pour affichage en liste
    """
    return {Resource}
    ListItem(
        id=resource.id,
        display_name=f"{resource.name}",
    )
```

## Checklist de Création d'un Mapper

### 1. Analyse Préalable (OBLIGATOIRE)

- [ ] Vérifier `datas/{resource}/repository/repository.md` pour connaître les méthodes disponibles
- [ ] Lister les endpoints dans `datas/{resource}/endpoints/`
- [ ] Identifier les entités liées dans la réponse JSON

### 2. Fichiers à Créer/Vérifier

- [ ] `src/domain/entities/{resource}.py` - Entité de domaine
- [ ] `src/application/dto/responses/{resource}_responses.py` - DTOs de réponse
- [ ] `src/application/mappers/{resource}_mapper.py` - Mapper (ce fichier)

### 3. Implémentation du Mapper

#### Méthodes de Base (TOUJOURS)

- [ ] `from_dict()` - Conversion dict → Entité
- [ ] `to_dict()` - Conversion Entité → dict

#### Méthodes Conditionnelles

- [ ] `from_all_{resources}_response()` - Si endpoint GET list existe
- [ ] `from_api_response()` - Si endpoint GET by_id retourne structure normalisée
- [ ] `to_list_item()` - Si besoin d'affichage liste simplifié

### 4. Règles Strictes

1. **TOUJOURS** utiliser `.get()` pour les champs optionnels
2. **TOUJOURS** fournir des valeurs par défaut pour les compteurs (ex: `count=0`)
3. **TOUJOURS** importer les mappers des entités liées
4. **TOUJOURS** gérer les listes vides avec `response.get("key", [])`
5. **JAMAIS** créer directement une entité sans passer par le mapper

### 5. Imports Standards

```python
# DTO de réponse
from mangacollec.application import (
    GetAll

{Resource}
sV2Response,  # Si get_all existe
Get
{Resource}
ByIdV2Response,  # Si get_by_id existe
)

# Mappers des entités liées
from mangacollec.application.mappers import RelatedMapper

# Entités du domaine
from mangacollec.domain.entities import

{Resource}, RelatedEntity
```

## Exemples de Référence

- **Mapper Complet** : `src/application/mappers/author_mapper.py`
- **Mapper Simple** : `src/application/mappers/edition_mapper.py`

## Structure des DTOs de Réponse

Les DTOs doivent suivre la structure normalisée V2 :

```python
@dataclass(frozen=True)
class Get{Resource}ByIdV2Response:
    """Réponse pour Get{Resource}ByIdV2.

    Structure normalisée V2 avec des tableaux séparés pour chaque type d'entité.
    """

    {resources}: list[{Resource}]
    # Entités liées (TOUJOURS en liste, même s'il n'y a qu'un élément)
    related_entities: list[RelatedEntity]
```

## Erreurs Courantes à Éviter

❌ **Mauvais** : `publisher: Publisher` (singulier)
✅ **Correct** : `publishers: list[Publisher]` (pluriel, liste)

❌ **Mauvais** : `data["optional_field"]` (KeyError possible)
✅ **Correct** : `data.get("optional_field")` (retourne None)

❌ **Mauvais** : Créer l'entité directement depuis response
✅ **Correct** : Utiliser `{Resource}Mapper.from_dict()`

❌ **Mauvais** : Oublier d'importer les mappers liés
✅ **Correct** : Importer tous les mappers nécessaires
