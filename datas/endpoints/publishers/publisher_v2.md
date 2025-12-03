---
resource: publisher_detail
version: v2
endpoint: /v2/publishers/{publisher_id}
method: GET
response_brut: datas/endpoints/publishers/publisher_v2.json
description: Get publisher by ID with full details
---

# Endpoint GET /v2/publishers/{publisher_id}

## Description
Retourne les informations détaillées d'un éditeur avec toutes ses éditions et séries associées (version V2 de l'API).

### Structure principale

| Champ          | Type             | Description              |
|----------------|------------------|--------------------------|
| `publishers`   | List[Publisher]  | Tableau des publishers   |
| `editions`     | List[Edition]    | Tableau des éditions     |
| `box_editions` | List[BoxEdition] | Tableau des box_editions |
| `series`       | List[Serie]      | Tableau des séries       |
| `types`        | List[Type]       | Tableau des types        |
| `volumes`      | List[Volume]     | Tableau des volumes      |
| `boxes`        | List[Box]        | Tableau des boxes        |

### Objet Publisher

| Champ            | Type | Description                     |
|------------------|------|---------------------------------|
| `id`             | str  | Identifiant unique de l'éditeur |
| `title`          | str  | Nom de l'éditeur                |
| `closed`         | bool | Éditeur fermé                   |
| `editions_count` | int  | Nombre d'éditions publiées      |
| `no_amazon`      | bool | Non disponible sur Amazon       |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | string        | Identifiant uuid de l'édition                                  |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | string        | Identifiant de la série parente                                |
| `publisher_id`          | string        | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | integer       | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié                                |
| `commercial_stop`       | boolean       | Arrêt commercial                                               |
| `not_finished`          | boolean       | Série non terminée                                             |
| `follow_editions_count` | integer       | Nombre de personnes qui suivent cette édition                  |

### Objet BoxEdition

| Champ                       | Type | Description                                |
|-----------------------------|------|--------------------------------------------|
| `id`                        | str  | Identifiant unique de l'édition du coffret |
| `title`                     | str  | Titre de l'édition du coffret              |
| `publisher_id`              | str  | Identifiant de l'éditeur                   |
| `boxes_count`               | int  | Nombre de coffrets dans l'édition          |
| `adult_content`             | bool | Indique si le contenu est pour adultes     |
| `box_follow_editions_count` | int  | Nombre d'utilisateurs suivant l'édition    |

### Objet Serie

| Champ            | Type    | Description                           |
|------------------|---------|---------------------------------------|
| `id`             | string  | Identifiant uuid de la série          |
| `title`          | string  | Titre de la série                     |
| `type_id`        | string  | Identifiant du type de série          |
| `adult_content`  | boolean | Contenu pour adultes                  |
| `editions_count` | integer | Nombre d'éditions disponibles         |
| `tasks_count`    | integer | Nombre de tâches associées à la série |

### Objet Type

| Champ        | Type    | Description                |
|--------------|---------|----------------------------|
| `id`         | string  | Identifiant uuid du type   |
| `title`      | string  | Nom du type                |
| `to_display` | boolean | Afficher dans l'interface  |

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | string        | Identifiant uuid du volume              |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | integer       | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | string        | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | boolean       | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |

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
| `box_possessions_count` | int           | Nombre d'utilisateurs possédant ce coffret     |
| `image_url`             | Optional[str] | URL de l'image de couverture                   |

## Exemple de réponse

```json
{
    "publishers": [],
    "editions": [],
    "box_editions": [],
    "series": [],
    "type": [],
    "volumes": [],
    "boxes": []
}
```


## Notes

- La version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs
- Contrairement à V1, les objets ne sont pas imbriqués
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
