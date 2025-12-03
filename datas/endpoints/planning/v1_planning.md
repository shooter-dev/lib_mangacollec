---
resource: planning
version: v1
endpoint: /v1/planning/
method: GET
fichier brut: v1_planning.json
description: List all planning
---

# Endpoint GET /v1/planning/

## Description
Retourne la liste de tous les volumes planifiés avec leurs informations de base.
----------
Returns the list of all scheduled volumes with their basic information.

## Structure de la réponse / Response Structure

### Objet Volume / Volume Object

| Champ               | Type          | Description                               |
|---------------------|---------------|-------------------------------------------|
| `id`                | string        | Identifiant unique du volume              |
| `title`             | Optional[str] | Titre du volume (peut être null)          |
| `number`            | integer       | Numéro du volume                          |
| `release_date`      | string        | Date de sortie au format YYYY-MM-DD       |
| `image_url`         | string        | URL de l'image de couverture              |
| `isbn`              | string        | ISBN du volume                            |
| `asin`              | string        | ASIN Amazon du volume                     |
| `edition_id`        | string        | Identifiant de l'édition                  |
| `possessions_count` | integer       | Nombre d'utilisateurs possédant ce volume |
| `not_sold`          | boolean       | Indique si le volume n'est plus en vente  |

### Objet Edition / Edition Object

| Champ                   | Type          | Description                                       |
|-------------------------|---------------|---------------------------------------------------|
| `id`                    | string        | Identifiant unique de l'édition                   |
| `title`                 | Optional[str] | Titre de l'édition (peut être null)               |
| `series_id`             | string        | Identifiant de la série parente                   |
| `publisher_id`          | string        | Identifiant de l'éditeur                          |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (peut être null) |
| `volumes_count`         | integer       | Nombre de volumes dans l'édition                  |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume (peut être null)         |
| `commercial_stop`       | boolean       | Indique si l'édition n'est plus commercialisée    |
| `not_finished`          | boolean       | Indique si l'édition n'est pas terminée           |
| `follow_editions_count` | integer       | Nombre d'utilisateurs suivant l'édition           |

### Objet Serie / Serie Object

| Champ            | Type    | Description                            |
|------------------|---------|----------------------------------------|
| `id`             | string  | Identifiant unique de la série         |
| `title`          | string  | Titre de la série                      |
| `type_id`        | string  | Identifiant du type de série           |
| `adult_content`  | boolean | Indique si le contenu est pour adultes |
| `editions_count` | integer | Nombre d'éditions de la série          |
| `tasks_count`    | integer | Nombre de tâches associées à la série  |

## Exemple de réponse / Response Example

```json
[
    {
        "id": "9cbfa618-0d67-4066-8259-1127f66d203e",
        "title": null,
        "number": 16,
        "release_date": "2022-09-01",
        "image_url": "https://m.media-amazon.com/images/I/51UYCzyYY-L.jpg",
        "isbn": "9791032711811",
        "asin": "B09XTQ9JF3",
        "edition_id": "1a39a08f-aba5-4c7f-8dc7-36eaea8f6354",
        "possessions_count": 51927,
        "not_sold": false,
        "edition": {
            "id": "1a39a08f-aba5-4c7f-8dc7-36eaea8f6354",
            "title": null,
            "series_id": "544df61b-edcf-45ec-9ae5-cdf8341a84ca",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "parent_edition_id": null,
            "volumes_count": 28,
            "last_volume_number": 30,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 145908,
            "series": {
                "id": "544df61b-edcf-45ec-9ae5-cdf8341a84ca",
                "title": "Jujutsu Kaisen",
                "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
                "adult_content": false,
                "editions_count": 6,
                "tasks_count": 1
            }
        }
    }
]
```

## Notes

- Cet endpoint retourne les volumes planifiés pour une période donnée
- L'endpoint accepte un paramètre `month` au format YYYY-MM-DD pour filtrer par mois
- Chaque volume contient des informations détaillées sur l'édition associée
- Les données incluent des statistiques comme le nombre de possessions et de followers
- La réponse peut être volumineuse selon la période demandée
- Les volumes sont retournés avec leur relation complète vers l'édition et la série