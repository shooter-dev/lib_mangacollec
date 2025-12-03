---
Resource: publishers
Version: v1
Endpoint: https://api.mangacollec.com/v1/publishers/
Method: GET
Response_brut: datas/endpoints/publishers/v1_publishers_list.json
Authentication: false
Description: List all publishers
---

# Endpoint GET /v1/publishers

## Description
Retourne la liste de tous les éditeurs de manga disponibles.
----------
Returns the list of all available manga publishers.

## Structure de la réponse

### Structure principale

| Champ | Type | Description |
|-------|------|-------------|
| `publishers` | List[Publisher] | Tableau des éditeurs |

### Objet Publisher

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique de l'éditeur |
| `title` | string | Nom de l'éditeur |

## Exemple de réponse

```json
[
    {
        "id": "4c9547ff-2ef6-439a-80b8-ea705a385b76",
        "title": "Kana"
    },
    {
        "id": "pika-editions",
        "title": "Pika Édition"
    },
    {
        "id": "ki-oon",
        "title": "Ki-oon"
    }
]
```

## Notes

- Cet endpoint retourne la liste complète des éditeurs disponibles
- Les éditeurs sont généralement les maisons d'édition qui publient les manga en français
- La réponse est relativement légère car elle ne contient que les informations de base
- Les éditeurs sont retournés sans ordre particulier