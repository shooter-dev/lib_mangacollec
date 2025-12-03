---
resource: volume_detail
version: v2
endpoint: https://api.mangacollec.com/v2/volumes/{volume_id}
method: GET
response_brut: datas/endpoints/volumes/volume_v2.json
description: Get volume by ID with full details
authentication: false
---

# Endpoint GET /v2/volumes/{volume_id}

## Description
Retourne les informations détaillées d'un volume avec toutes ses entités associées
en structure normalisée (version V2 de l'API).

## Structure de la réponse

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité,
contrairement à V1 qui utilise des objets imbriqués.

### Structure principale

| Champ          | Type             | Description                               |
|----------------|------------------|-------------------------------------------|
| `volumes`      | List[Volume]     | Tableau des volumes                       |
| `editions`     | List[Edition]    | Tableau des éditions                      |
| `publishers`   | List[Publisher]  | Tableau des éditeurs                      |
| `series`       | List[Serie]      | Tableau des séries                        |
| `types`        | List[Type]       | Tableau des types de séries               |
| `box_volumes`  | List[BoxVolume]  | Tableau des associations volumes-coffrets |
| `boxes`        | List[Box]        | Tableau des coffrets                      |
| `box_editions` | List[BoxEdition] | Tableau des éditions de coffrets          |

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
| `nb_pages`          | Optional[int] | Nombre de pages du volume               |
| `content`           | Optional[str] | Contenu/description du volume           |

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

### Objet Publisher

| Champ            | Type | Description                    |
|------------------|------|--------------------------------|
| `id`             | str  | Identifiant uuid de l'éditeur  |
| `title`          | str  | Nom de l'éditeur               |
| `closed`         | bool | Éditeur fermé                  |
| `editions_count` | int  | Nombre d'éditions de l'éditeur |
| `no_amazon`      | bool | Pas de vente sur Amazon        |

### Objet Serie

| Champ            | Type  | Description                           |
|------------------|-------|---------------------------------------|
| `id`             | str   | Identifiant uuid de la série          |
| `title`          | str   | Titre de la série                     |
| `type_id`        | str   | Identifiant du type de série          |
| `adult_content`  | bool  | Contenu pour adultes                  |
| `editions_count` | int   | Nombre d'éditions disponibles         |
| `tasks_count`    | int   | Nombre de tâches associées à la série |

### Objet Type

| Champ        | Type | Description                          |
|--------------|------|--------------------------------------|
| `id`         | str  | Identifiant unique du type           |
| `title`      | str  | Nom du type                          |
| `to_display` | bool | Indique si le type doit être affiché |

### Objet BoxVolume

| Champ       | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| `id`        | str  | Identifiant uuid de l'association               |
| `box_id`    | str  | ID du coffret                                   |
| `volume_id` | str  | ID du volume                                    |
| `included`  | bool | Indique si le volume est inclus dans le coffret |

### Objet Box

| Champ                   | Type          | Description                                      |
|-------------------------|---------------|--------------------------------------------------|
| `id`                    | str           | Identifiant unique du coffret                    |
| `title`                 | Optional[str] | Titre du coffret                                 |
| `number`                | int           | Numéro du coffret                                |
| `release_date`          | Optional[str] | Date de sortie (format ISO 8601)                 |
| `isbn`                  | Optional[str] | ISBN du coffret                                  |
| `asin`                  | Optional[str] | ASIN Amazon                                      |
| `commercial_stop`       | bool          | Indique si le coffret est arrêté commercialement |
| `box_edition_id`        | str           | ID de la box edition associée                    |
| `box_possessions_count` | Optional[int] | Nombre de possesseurs                            |
| `image_url`             | Optional[str] | URL de l'image                                   |

### Objet BoxEdition

| Champ                       | Type          | Description                                         |
|-----------------------------|---------------|-----------------------------------------------------|
| `id`                        | str           | Identifiant uuid de la box edition                  |
| `title`                     | Optional[str] | Titre de la box edition                             |
| `publisher_id`              | str           | ID de l'éditeur                                     |
| `boxes_count`               | int           | Nombre de boxes dans cette box edition              |
| `adult_content`             | bool          | Indique si le contenu est pour adultes              |
| `box_follow_editions_count` | int           | Nombre d'utilisateurs qui suivent cette box edition |

## Exemple de réponse

```json
{
    "volumes": [],
    "editions": [],
    "publishers": [],
    "series": [],
    "types": [],
    "box_volumes": [],
    "boxes": [],
    "box_editions": []
}
```

## Notes

- La version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs (edition_id, series_id, publisher_id, etc.)
- Contrairement à V1, les objets ne sont pas imbriqués
- Cette structure facilite la manipulation et la mise en cache des données côté client
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
- Pour la liste volumes Retournera toujours un seul volume.
