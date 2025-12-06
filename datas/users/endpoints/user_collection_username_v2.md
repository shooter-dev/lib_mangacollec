---
resource: user_collection_username
version: v2
endpoint: https://api.mangacollec.com/v2/user/{username}/collection
method: GET
response_brut: datas/users/endpoints/user_collection_username_v2.json
description: Get public collection of a user
authentication: false
---

# Endpoint GET /v2/user/{username}/collection

## Description
Retourne la collection publique d'un utilisateur via son nom d'utilisateur (version V2 de l'API).

### Structure principale

| Champ                 | Type                   | Description                     |
|-----------------------|------------------------|---------------------------------|
| `editions`            | List[Edition]          | Tableau des éditions            |
| `series`              | List[Serie]            | Tableau des séries              |
| `types`               | List[Type]             | Tableau des types               |
| `kinds`               | List[Kind]             | Tableau des kinds               |
| `volumes`             | List[Volume]           | Tableau des volumes             |
| `box_editions`        | List[BoxEdition]       | Tableau des box_editions        |
| `boxes`               | List[Box]              | Tableau des boxes               |
| `box_volumes`         | List[BoxVolume]        | Tableau des box_volumes         |
| `follow_editions`     | List[FollowEdition]    | Tableau des follow_editions     |
| `possessions`         | List[Possession]       | Tableau des possessions         |
| `box_follow_editions` | List[BoxFollowEdition] | Tableau des box_follow_editions |
| `box_possessions`     | List[BoxPossession]    | Tableau des box_possessions     |
| `read_editions`       | List[ReadEdition]      | Tableau des read_editions       |
| `reads`               | List[Read]             | Tableau des reads               |

### Objet Edition

| Champ                   | Type          | Description                                      |
|-------------------------|---------------|--------------------------------------------------|
| `id`                    | str           | Identifiant uuid de l'édition                    |
| `title`                 | str           | Titre de l'édition                               |
| `series_id`             | str           | ID de la série associée                          |
| `publisher_id`          | str           | ID de l'éditeur                                  |
| `parent_edition_id`     | Optional[str] | ID de l'édition parente                          |
| `volumes_count`         | int           | Nombre de volumes dans l'édition                 |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume                         |
| `commercial_stop`       | bool          | Indique si l'édition est arrêtée commercialement |
| `not_finished`          | bool          | Indique si l'édition n'est pas terminée          |
| `follow_editions_count` | int           | Nombre d'utilisateurs qui suivent cette édition  |

### Objet Serie

| Champ            | Type      | Description                            |
|------------------|-----------|----------------------------------------|
| `id`             | str       | Identifiant uuid de la série           |
| `title`          | str       | Titre de la série                      |
| `type_id`        | str       | ID du type de média                    |
| `adult_content`  | bool      | Indique si le contenu est pour adultes |
| `editions_count` | int       | Nombre d'éditions de la série          |
| `tasks_count`    | int       | Nombre de tâches associées             |
| `kinds_ids`      | List[str] | Liste des IDs des kinds associés       |

### Objet Type

| Champ        | Type | Description                          |
|--------------|------|--------------------------------------|
| `id`         | str  | Identifiant unique du type           |
| `title`      | str  | Nom du type                          |
| `to_display` | bool | Indique si le type doit être affiché |

### Objet Kind

| Champ   | Type | Description                |
|---------|------|----------------------------|
| `id`    | str  | Identifiant unique du kind |
| `title` | str  | Nom du kind                |

### Objet Volume

| Champ               | Type          | Description                              |
|---------------------|---------------|------------------------------------------|
| `id`                | str           | Identifiant unique du volume             |
| `title`             | Optional[str] | Titre du volume                          |
| `number`            | int           | Numéro du volume                         |
| `release_date`      | str           | Date de sortie (format ISO 8601)         |
| `isbn`              | Optional[str] | ISBN du volume                           |
| `asin`              | Optional[str] | ASIN Amazon                              |
| `edition_id`        | str           | ID de l'édition associée                 |
| `possessions_count` | int           | Nombre de possesseurs                    |
| `not_sold`          | bool          | Indique si le volume n'est plus en vente |
| `image_url`         | Optional[str] | URL de l'image de couverture             |

### Objet BoxEdition

| Champ                       | Type          | Description                                         |
|-----------------------------|---------------|-----------------------------------------------------|
| `id`                        | str           | Identifiant uuid de la box edition                  |
| `title`                     | Optional[str] | Titre de la box edition                             |
| `publisher_id`              | str           | ID de l'éditeur                                     |
| `boxes_count`               | int           | Nombre de boxes dans cette box edition              |
| `adult_content`             | bool          | Indique si le contenu est pour adultes              |
| `box_follow_editions_count` | int           | Nombre d'utilisateurs qui suivent cette box edition |

### Objet Box

| Champ                   | Type          | Description                                      |
|-------------------------|---------------|--------------------------------------------------|
| `id`                    | str           | Identifiant unique du coffret                    |
| `title`                 | Optional[str] | Titre du coffret                                 |
| `number`                | int           | Numéro du coffret                                |
| `release_date`          | str           | Date de sortie (format ISO 8601)                 |
| `isbn`                  | Optional[str] | ISBN du coffret                                  |
| `asin`                  | Optional[str] | ASIN Amazon                                      |
| `commercial_stop`       | bool          | Indique si le coffret est arrêté commercialement |
| `box_edition_id`        | str           | ID de la box edition associée                    |
| `box_possessions_count` | int           | Nombre de possesseurs                            |
| `image_url`             | Optional[str] | URL de l'image                                   |

### Objet BoxVolume

| Champ       | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| `id`        | str  | Identifiant uuid de l'association               |
| `box_id`    | str  | ID du coffret                                   |
| `volume_id` | str  | ID du volume                                    |
| `included`  | bool | Indique si le volume est inclus dans le coffret |

### Objet FollowEdition

| Champ        | Type | Description                           |
|--------------|------|---------------------------------------|
| `id`         | str  | Identifiant unique du suivi           |
| `edition_id` | str  | ID de l'édition suivie                |
| `user_id`    | str  | ID de l'utilisateur                   |
| `following`  | bool | Indique si l'édition est suivie       |
| `created_at` | str  | Date de création (format ISO 8601)    |
| `updated_at` | str  | Date de mise à jour (format ISO 8601) |

### Objet Possession

| Champ        | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la possession |
| `volume_id`  | str  | ID du volume possédé              |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date d'ajout (format ISO 8601)    |

### Objet BoxFollowEdition

| Champ            | Type | Description                           |
|------------------|------|---------------------------------------|
| `id`             | str  | Identifiant unique du suivi           |
| `box_edition_id` | str  | ID de la box edition suivie           |
| `user_id`        | str  | ID de l'utilisateur                   |
| `following`      | bool | Indique si la box edition est suivie  |
| `created_at`     | str  | Date de création (format ISO 8601)    |
| `updated_at`     | str  | Date de mise à jour (format ISO 8601) |

### Objet BoxPossession

| Champ        | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la possession |
| `box_id`     | str  | ID du coffret possédé             |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date d'ajout (format ISO 8601)    |

### Objet ReadEdition

| Champ        | Type | Description                                  |
|--------------|------|----------------------------------------------|
| `id`         | str  | Identifiant uuid de la lecture               |
| `edition_id` | str  | ID de l'édition                              |
| `user_id`    | str  | ID de l'utilisateur                          |
| `reading`    | bool | Indique si l'édition est en cours de lecture |
| `created_at` | str  | Date de création (format ISO 8601)           |
| `updated_at` | str  | Date de mise à jour (format ISO 8601)        |

### Objet Read

| Champ        | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la lecture    |
| `volume_id`  | str  | ID du volume lu                   |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date de lecture (format ISO 8601) |

## Exemple de réponse

```json
{
    "editions": [],
    "series": [],
    "types": [],
    "kinds": [],
    "volumes": [],
    "box_editions": [],
    "boxes": [],
    "box_volumes": [],
    "follow_editions": [],
    "possessions": [],
    "box_follow_editions": [],
    "box_possessions": [],
    "read_editions": [],
    "reads": []
}
```

## Notes

- Version V2 utilise une structure normalisée avec des tableaux séparés pour chaque type d'entité
- Retourne la collection de l'utilisateur 
- Les champs marqués comme `Optional[]` peuvent être null
- Les dates suivent le format ISO 8601 (ex : "2019-03-07T15:34:48.359Z")
- Les IDs sont des chaînes de caractères au format UUID