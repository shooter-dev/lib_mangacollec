---
Resource: series
Version: v1
Endpoint: https://api.mangacollec.com/v1/series/
Method: GET
Response_brut: datas/endpoints/series/v1_series_list.json
Authentication: false
Description: List all series
---

# Endpoint GET /v1/series

## Description
Retourne la liste de toutes les séries de manga disponibles avec leurs informations de base.
----------
Returns the list of all available manga series with their basic information.

## Structure de la réponse

### Structure principale

| Champ    | Type        | Description        |
|----------|-------------|--------------------|
| `series` | List[Serie] | Tableau des séries |

### Objet Serie

| Champ            | Type           | Description                           |
|------------------|----------------|---------------------------------------|
| `id`             | string         | Identifiant unique de la série        |
| `title`          | string         | Titre de la série                     |
| `type_id`        | string \| null | Identifiant du type de série          |
| `adult_content`  | boolean        | Contenu pour adultes (true/false)     |
| `editions_count` | integer        | Nombre d'éditions disponibles         |
| `tasks_count`    | integer        | Nombre de tâches associées à la série |

## Exemple de réponse

```json
[
    {
        "id": "d1a38f41-2ac9-40cf-aa17-aeac9697e1c8",
        "title": "Naruto",
        "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "adult_content": false,
        "editions_count": 7,
        "tasks_count": 1
    },
    {
        "id": "36d208b5-a92c-4028-8f63-85be903b93b4",
        "title": "Boruto : Naruto Next Generations",
        "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "adult_content": false,
        "editions_count": 5,
        "tasks_count": 3
    }
]
```

## Notes

- Cet endpoint retourne uniquement les informations de base des séries
- Pour obtenir les détails complets (éditions, volumes), utiliser `/v1/series/{series_id}`
- La réponse peut être très volumineuse car elle contient toutes les séries
- Les séries sont retournées sans ordre particulier