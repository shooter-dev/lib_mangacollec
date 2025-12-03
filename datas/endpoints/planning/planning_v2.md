---
resource: volume_planning
version: v2
endpoint: https://api.mangacollec.com/v2/planning/
method: GET
response_brut: datas/endpoints/planning/planning_v2.json
description: List all planning
---

# Endpoint GET /v2/planning

## Description
Retourne la liste de tous les volumes planifiés avec leurs informations de base (version V2 de l'API).

## Structure Parametre

- `month`: 2022-09-30 au format YYYY-MM-DD

## Structure de la réponse

### Objet Volume

| Champ               | Type          | Description                               |
|---------------------|---------------|-------------------------------------------|
| `id`                | str           | Identifiant unique du volume              |
| `title`             | Optional[str] | Titre du volume                           |
| `number`            | int           | Numéro du volume                          |
| `release_date`      | Optional[str] | Date de sortie au format YYYY-MM-DD       |
| `isbn`              | Optional[str] | ISBN du volume                            |
| `asin`              | Optional[str] | ASIN Amazon du volume                     |
| `edition_id`        | str           | Identifiant de l'édition                  |
| `possessions_count` | Optional[int] | Nombre d'utilisateurs possédant ce volume |
| `not_sold`          | bool          | Indique si le volume n'est plus en vente  |
| `image_url`         | Optional[str] | URL de l'image de couverture              |

### Objet Edition

| Champ                   | Type          | Description                                    |
|-------------------------|---------------|------------------------------------------------|
| `id`                    | str           | Identifiant unique de l'édition                |
| `title`                 | Optional[str] | Titre de l'édition                             |
| `series_id`             | str           | Identifiant de la série parente                |
| `publisher_id`          | str           | Identifiant de l'éditeur                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente               |
| `volumes_count`         | int           | Nombre de volumes dans l'édition               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume                       |
| `commercial_stop`       | bool          | Indique si l'édition n'est plus commercialisée |
| `not_finished`          | bool          | Indique si l'édition n'est pas terminée        |
| `follow_editions_count` | int           | Nombre d'utilisateurs suivant l'édition        |

### Objet Serie

| Champ            | Type | Description                            |
|------------------|------|----------------------------------------|
| `id`             | str  | Identifiant unique de la série         |
| `title`          | str  | Titre de la série                      |
| `type_id`        | str  | Identifiant du type de série           |
| `adult_content`  | bool | Indique si le contenu est pour adultes |
| `editions_count` | int  | Nombre d'éditions de la série          |
| `tasks_count`    | int  | Nombre de tâches associées à la série  |

### Objet Type

| Champ         | Type | Description                                      |
|---------------|------|--------------------------------------------------|
| `id`          | str  | Identifiant unique du type                       |
| `title`       | str  | Titre du type                                    |
| `to_display`  | bool | Indique si le type doit être affiché             |

### Objet Box

| Champ                   | Type          | Description                                    |
|-------------------------|---------------|------------------------------------------------|
| `id`                    | str           | Identifiant unique du coffret                  |
| `title`                 | Optional[str] | Titre du coffret (peut être null)              |
| `number`                | int           | Numéro du coffret                              |
| `release_date`          | Optional[str] | Date de sortie au format YYYY-MM-DD            |
| `isbn`                  | Optional[str] | ISBN du coffret                                |
| `asin`                  | Optional[str] | ASIN Amazon du coffret                         |
| `commercial_stop`       | bool          | Indique si le coffret n'est plus commercialisé |
| `box_edition_id`        | str           | Identifiant de l'édition du coffret            |
| `box_possessions_count` | Optional[int] | Nombre d'utilisateurs possédant ce coffret     |
| `image_url`             | Optional[str] | URL de l'image de couverture                   |

### Objet BoxEdition

| Champ                       | Type | Description                                |
|-----------------------------|------|--------------------------------------------|
| `id`                        | str  | Identifiant unique de l'édition du coffret |
| `title`                     | str  | Titre de l'édition du coffret              |
| `publisher_id`              | str  | Identifiant de l'éditeur                   |
| `boxes_count`               | int  | Nombre de coffrets dans l'édition          |
| `adult_content`             | bool | Indique si le contenu est pour adultes     |
| `box_follow_editions_count` | int  | Nombre d'utilisateurs suivant l'édition    |

## Exemple Parametre

```http request
https://api.mangacollec.com/v2/planning?month=2022-09-30
```

## Exemple de réponse

```json
{
    "volumes": [],
    "editions": [],
    "series": [],
    "types": [],
    "boxes": [],
    "box_editions": [],
    "box_volumes": []
}
```

## Notes

- Cet endpoint retourne une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs
- Contrairement à V1, les objets ne sont pas imbriqués
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
- L'endpoint accepte un paramètre `month` au format YYYY-MM-DD pour filtrer par mois
- La réponse peut être volumineuse selon la période demandée