---
resource: serie_detail
version: v2
endpoint: https://api.mangacollec.com/v2/series/{series_id}
method: GET
response_brut: datas/_endpoints/series/serie_v2.json
description: Get serie by ID with full details
---

# Endpoint GET /v2/series/{series_id}

## Description
Retourne les informations détaillées d'une série avec toutes ses relations en structure normalisée (version V2 de l'API).

## Structure de la réponse

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, contrairement à V1 qui utilise des objets imbriqués.

### Structure principale

| Champ          | Type             | Description               |
|----------------|------------------|---------------------------|
| `series`       | List[Serie]      | Tableau des séries        |
| `types`        | List[Type]       | Tableau des type          |
| `kinds`        | List[Kind]       | Tableau des genres        |
| `tasks`        | List[Task]       | Tableau des tâches        |
| `jobs`         | List[Job]        | Tableau des rôles/métiers |
| `authors`      | List[Author]     | Tableau des auteurs       |
| `editions`     | List[Edition]    | Tableau des éditions      |
| `publishers`   | List[Publisher]  | Tableau des éditeurs      |
| `volumes`      | List[Volume]     | Tableau des volumes       |
| `box_editions` | List[BoxEdition] | Tableau des box_editions  |
| `boxes`        | List[Box]        | Tableau des coffrets      |
| `box_volumes`  | List[BoxVolume]  | Tableau des box_volumes   |

### Objet Serie

| Champ            | Type        | Description                                  |
|------------------|-------------|----------------------------------------------|
| `id`             | str         | Identifiant unique de la série               |
| `title`          | str         | Titre de la série                            |
| `type_id`        | str         | Identifiant du type de série                 |
| `adult_content`  | bool        | Contenu pour adultes                         |
| `editions_count` | int         | Nombre d'éditions disponibles                |
| `tasks_count`    | int         | Nombre de tâches associées à la série        |
| `kinds_ids`      | List[str]   | Liste des IDs des genres associés à la série |

### Objet Type

| Champ        | Type | Description                          |
|--------------|------|--------------------------------------|
| `id`         | str  | Identifiant unique du type           |
| `title`      | str  | Titre du type                        |
| `to_display` | bool | Indique si le type doit être affiché |

### Objet Kind

| Champ        | Type      | Description                          |
|--------------|-----------|--------------------------------------|
| `id`         | str       | Identifiant unique du genre          |
| `title`      | str       | Titre du genre                       |

### Objet Task

| Champ       | Type | Description                    |
|-------------|------|--------------------------------|
| `id`        | str  | Identifiant unique de la tâche |
| `job_id`    | str  | Identifiant du rôle/métier     |
| `series_id` | str  | Identifiant de la série        |
| `author_id` | str  | Identifiant de l'auteur        |

### Objet Job

| Champ   | Type | Description                                       |
|---------|------|---------------------------------------------------|
| `id`    | str  | Identifiant unique du rôle                        |
| `title` | str  | Titre du rôle (ex: "Auteur", "Auteur original")   |

### Objet Author

| Champ         | Type          | Description                                 |
|---------------|---------------|---------------------------------------------|
| `id`          | str           | Identifiant unique de l'auteur              |
| `name`        | str           | Nom de l'auteur                             |
| `first_name`  | Optional[str] | Prénom de l'auteur                          |
| `tasks_count` | int           | Nombre total de tâches associées à l'auteur |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | str           | Identifiant unique de l'édition                                |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | str           | Identifiant de la série parente                                |
| `publisher_id`          | str           | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | int           | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié                                |
| `commercial_stop`       | bool          | Arrêt commercial                                               |
| `not_finished`          | bool          | Série non terminée                                             |
| `follow_editions_count` | int           | Nombre de personnes qui suivent cette édition                  |

### Objet Publisher
| Champ            | Type | Description                     |
|------------------|------|---------------------------------|
| `id`             | str  | Identifiant unique de l'éditeur |
| `title`          | str  | Nom de l'éditeur                |
| `closed`         | bool | Éditeur fermé                   |
| `editions_count` | int  | Nombre d'éditions publiées      |
| `no_amazon`      | bool | Non disponible sur Amazon       |

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | str           | Identifiant unique du volume            |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | int           | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | str           | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | bool          | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |

### Objet BoxEdition

| Champ                       | Type          | Description                                    |
|-----------------------------|---------------|------------------------------------------------|
| `id`                        | str           | Identifiant unique de la box édition           |
| `title`                     | Optional[str] | Titre de la box édition                        |
| `publisher_id`              | str           | Identifiant de l'éditeur                       |
| `boxes_count`               | int           | Nombre de coffrets dans la box édition         |
| `adult_content`             | bool          | Contenu pour adultes                           |
| `box_follow_editions_count` | int           | Nombre de personnes qui suivent la box édition |

### Objet Box

| Champ                   | Type          | Description                             |
|-------------------------|---------------|-----------------------------------------|
| `id`                    | str           | Identifiant unique du coffret           |
| `title`                 | Optional[str] | Titre du coffret                        |
| `number`                | int           | Numéro du coffret                       |
| `release_date`          | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`                  | Optional[str] | ISBN du coffret                         |
| `asin`                  | Optional[str] | ASIN Amazon du coffret                  |
| `commercial_stop`       | bool          | Arrêt commercial                        |
| `box_edition_id`        | str           | Identifiant de la box édition parente   |
| `box_possessions_count` | Optional[int] | Nombre de possesseurs du coffret        |
| `image_url`             | Optional[str] | URL de l'image de couverture            |

### Objet BoxVolume

| Champ       | Type | Description                               |
|-------------|------|-------------------------------------------|
| `id`        | str  | Identifiant unique du volume dans coffret |
| `box_id`    | str  | Identifiant du coffret parent             |
| `volume_id` | str  | Identifiant du volume                     |
| `number`    | int  | Numéro du volume dans le coffret          |

## Exemple de réponse / Response Example

```json
{
    "series": [],
    "types": [],
    "kinds": [],
    "tasks": [],
    "jobs": [],
    "authors": [],
    "editions": [],
    "publishers": [],
    "volumes": [],
    "box_editions": [],
    "boxes": [],
    "box_volumes": []
}
```

## Notes

- La version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs (job_id, series_id, author_id, etc.)
- Contrairement à V1, les objets ne sont pas imbriqués
- Cette structure facilite la manipulation et la mise en cache des données côté client
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
- L'objet Serie inclut maintenant un champ `kinds_ids` qui est une liste d'IDs de genres
- Les entités de type coffret (BoxEdition, Box, BoxVolume) sont disponibles pour gérer les produits spéciaux
