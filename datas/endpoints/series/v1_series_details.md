---
resource: series
version: v1
endpoint: /v1/series/{series_id}
method: GET
description: Get series by ID with full details
---

# Endpoint GET /v1/series/{series_id}

## Description
Retourne les informations détaillées d'une série avec toutes ses éditions et volumes associés.
----------
Returns detailed information about a series with all its associated editions and volumes.

## Structure de la réponse / Response Structure

### Objet Serie / Serie Object

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique de la série |
| `title` | string | Titre de la série |
| `type_id` | string | Identifiant du type de série |
| `adult_content` | boolean | Contenu pour adultes (true/false) |
| `editions_count` | integer | Nombre d'éditions disponibles |
| `tasks_count` | integer | Nombre de tâches associées à la série |
| `editions` | array\[Edition\] | Liste des éditions de la série |

### Objet Edition / Edition Object

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique de l'édition |
| `title` | string \| null | Titre de l'édition (peut être null) |
| `series_id` | string | Identifiant de la série parente |
| `publisher_id` | string | Identifiant de l'éditeur |
| `parent_edition_id` | string \| null | Identifiant de l'édition parente |
| `volumes_count` | integer | Nombre de volumes dans l'édition |
| `last_volume_number` | integer \| null | Numéro du dernier volume publié |
| `commercial_stop` | boolean | Arrêt commercial (true/false) |
| `not_finished` | boolean | Série non terminée (true/false) |
| `follow_editions_count` | integer | Nombre de personnes qui suivent cette édition |
| `publisher` | Publisher | Objet Publisher détaillé |
| `volumes` | array\[Volume\] | Liste des volumes de l'édition |

### Objet Volume / Volume Object

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique du volume |
| `title` | string \| null | Titre du volume (peut être null) |
| `number` | integer | Numéro du volume |
| `release_date` | string \| null | Date de publication (format YYYY-MM-DD) |
| `image_url` | string \| null | URL de l'image de couverture |
| `isbn` | string \| null | ISBN du volume |
| `asin` | string \| null | ASIN Amazon du volume |
| `edition_id` | string | Identifiant de l'édition parente |
| `possessions_count` | integer \| null | Nombre de possesseurs du volume |
| `not_sold` | boolean | Plus en vente (true/false) |

## Exemple de réponse / Response Example

```json
{
    "id": "d1a38f41-2ac9-40cf-aa17-aeac9697e1c8",
    "title": "Naruto",
    "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
    "adult_content": false,
    "editions_count": 7,
    "tasks_count": 1,
    "editions": [
        {
            "id": "345b6656-93a3-43d1-aeb0-6389a269c85d",
            "title": null,
            "series_id": "d1a38f41-2ac9-40cf-aa17-aeac9697e1c8",
            "publisher_id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
            "volumes_count": 72,
            "last_volume_number": 72,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 116348,
            "volumes": [...]
        }
    ]
}
```

## Notes

- La réponse peut être très volumineuse car elle contient toute la hiérarchie des données
- Les éditions spéciales ont un `parent_edition_id` pointant vers l'édition standard
- Les volumes peuvent avoir des informations commerciales comme `not_sold` et `possessions_count`