---
Resource: edition_detail
Version: v1
Endpoint: https://api.mangacollec.com/v1/editions/{edition_id}
Method: GET
Response_brut: datas/_endpoints/editions/v1_editions_details.json
Authentication: false
Description: Get edition by ID with full details
---

# Endpoint GET /v1/editions/{edition_id}

## Description
Retourne les informations détaillées d'une édition avec sa série, son éditeur et tous ses volumes associés (version V1 de l'API).
----------
Returns detailed information about an edition with its series, publisher and all its associated volumes (V1 API version).

## Structure de la réponse

### Structure principale

| Champ | Type | Description |
|-------|------|-------------|
| `edition` | Edition | Objet édition détaillé |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | string        | Identifiant unique de l'édition                                |
| `title`                 | Optional[str] | Titre de l'édition (peut être null)                            |
| `series_id`             | string        | Identifiant de la série parente                                |
| `publisher_id`          | string        | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | integer       | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | integer       | Numéro du dernier volume publié                                |
| `commercial_stop`       | boolean       | Arrêt commercial (true/false)                                  |
| `not_finished`          | boolean       | Série non terminée (true/false)                                |
| `follow_editions_count` | integer       | Nombre de personnes qui suivent cette édition                  |
| `series`                | Serie        | Objet Serie détaillé                                          |
| `publisher`             | Publisher     | Objet Publisher détaillé                                       |
| `volumes`               | List[Volume]  | Liste des volumes de l'édition                                 |

### Objet Serie / Serie Object

| Champ            | Type    | Description                           |
|------------------|---------|---------------------------------------|
| `id`             | string  | Identifiant unique de la série        |
| `title`          | string  | Titre de la série                     |
| `type_id`        | string  | Identifiant du type de série          |
| `adult_content`  | boolean | Contenu pour adultes (true/false)     |
| `editions_count` | integer | Nombre d'éditions disponibles         |
| `tasks_count`    | integer | Nombre de tâches associées à la série |
| `type`           | Type    | Objet Type détaillé                   |

### Objet Type / Type Object

| Champ        | Type    | Description                              |
|--------------|---------|------------------------------------------|
| `id`         | string  | Identifiant unique du type               |
| `title`      | string  | Titre du type (ex: "Manga")              |
| `to_display` | boolean | À afficher dans l'interface (true/false) |

### Objet Publisher / Publisher Object

| Champ            | Type    | Description                                |
|------------------|---------|--------------------------------------------|
| `id`             | string  | Identifiant unique de l'éditeur            |
| `title`          | string  | Nom de l'éditeur                           |
| `closed`         | boolean | Éditeur fermé (true/false)                 |
| `editions_count` | integer | Nombre d'éditions publiées par cet éditeur |
| `no_amazon`      | boolean | Pas de lien Amazon disponible (true/false) |

### Objet Volume / Volume Object

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | string        | Identifiant unique du volume            |
| `title`             | Optional[str] | Titre du volume (peut être null)        |
| `number`            | integer       | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `image_url`         | Optional[str] | URL de l'image de couverture            |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | string        | Identifiant de l'édition parente        |
| `possessions_count` | integer       | Nombre de possesseurs du volume         |
| `not_sold`          | boolean       | Plus en vente (true/false)              |

## Exemple de réponse

```json
{
    "id": "345b6656-93a3-43d1-aeb0-6389a269c85d",
    "title": null,
    "series_id": "d1a38f41-2ac9-40cf-aa17-aeac9697e1c8",
    "publisher_id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
    "parent_edition_id": null,
    "volumes_count": 72,
    "last_volume_number": 72,
    "commercial_stop": false,
    "not_finished": false,
    "follow_editions_count": 116366,
    "series": {
        "id": "d1a38f41-2ac9-40cf-aa17-aeac9697e1c8",
        "title": "Naruto",
        "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "adult_content": false,
        "editions_count": 7,
        "tasks_count": 1,
        "type": {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        }
    },
    "publisher": {
        "id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
        "title": "Kana",
        "closed": false,
        "editions_count": 595,
        "no_amazon": false
    },
    "volumes": [
        {
            "id": "bc088f0b-6f62-4b50-9165-a81bd00e5fa2",
            "title": null,
            "number": 72,
            "release_date": "2016-11-04",
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/61F--hubbfL.jpg",
            "isbn": "9782505065067",
            "asin": "2505065063",
            "edition_id": "345b6656-93a3-43d1-aeb0-6389a269c85d",
            "possessions_count": 32234,
            "not_sold": false
        }
    ]
}
```

## Notes

- La version V1 utilise une **structure imbriquée** avec les objets series, publisher et volumes directement dans la réponse
- L'objet `series` contient lui-même un objet `type` imbriqué
- Les champs marqués comme `Optional[]` peuvent être null
- Les éditions spéciales (jaquettes alternatives, éditions limitées) ont un `parent_edition_id` pointant vers l'édition standard
- Pour obtenir la liste complète des volumes, voir le tableau `volumes` dans la réponse
