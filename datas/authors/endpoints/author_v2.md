---
resource: author_detail
version: v2
endpoint: https://api.mangacollec.com/v2/authors/{author_id}
method: GET
response_brut: datas/_endpoints/_exemple/author_v2.json
description: Get author by ID with full details
authentication: false
---

# Endpoint GET /v2/authors/{author_id}

## Description
Retourne les informations détaillées d'un auteur avec toutes ses tâches, séries, éditions et volumes associés 
en structure normalisée (version V2 de l'API).

## Structure de la réponse

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, 
contrairement à V1 qui utilise des objets imbriqués.

### Structure principale

| Champ      | Type          | Description               |
|------------|---------------|---------------------------|
| `authors`  | List[Author]  | Tableau des auteurs       |
| `tasks`    | List[Task]    | Tableau des tâches        |
| `jobs`     | List[Job]     | Tableau des rôles/métiers |
| `series`   | List[Serie]   | Tableau des séries        |
| `editions` | List[Edition] | Tableau des éditions      |
| `volumes`  | List[Volume]  | Tableau des volumes       |

### Objet Author

| Champ         | Type          | Description                                 |
|---------------|---------------|---------------------------------------------|
| `id`          | str           | Identifiant uuid de l'auteur                |
| `name`        | str           | Nom de l'auteur                             |
| `first_name`  | Optional[str] | Prénom de l'auteur                          |
| `tasks_count` | int           | Nombre total de tâches associées à l'auteur |

### Objet Task

| Champ       | Type | Description                  |
|-------------|------|------------------------------|
| `id`        | str  | Identifiant uuid de la tâche |
| `job_id`    | str  | Identifiant du rôle/métier   |
| `series_id` | str  | Identifiant de la série      |
| `author_id` | str  | Identifiant de l'auteur      |

### Objet Job

| Champ   | Type | Description                                     |
|---------|------|-------------------------------------------------|
| `id`    | str  | Identifiant uuid du rôle                        |
| `title` | str  | Titre du rôle (ex: "Auteur", "Auteur original") |

### Objet Serie

| Champ            | Type  | Description                           |
|------------------|-------|---------------------------------------|
| `id`             | str   | Identifiant uuid de la série          |
| `title`          | str   | Titre de la série                     |
| `type_id`        | str   | Identifiant du type de série          |
| `adult_content`  | bool  | Contenu pour adultes                  |
| `editions_count` | int   | Nombre d'éditions disponibles         |
| `tasks_count`    | int   | Nombre de tâches associées à la série |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | str           | Identifiant uuid de l'édition                                  |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | str           | Identifiant de la série parente                                |
| `publisher_id`          | str           | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | int           | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié                                |
| `commercial_stop`       | bool          | Arrêt commercial                                               |
| `not_finished`          | bool          | Série non terminée                                             |
| `follow_editions_count` | int           | Nombre de personnes qui suivent cette édition                  |

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | str           | Identifiant uuid du volume              |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | int           | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | str           | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | bool          | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |

## Exemple de réponse

```json
{
    "authors": [],
    "tasks": [],
    "jobs": [],
    "series": [],
    "editions": [],
    "volumes": []
}
```

## Notes

- La version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs
- Contrairement à V1, les objets ne sont pas imbriqués
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
- Pour la list authors Retournera toujours une seule author. 