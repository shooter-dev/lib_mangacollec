---
Resource: type_list
Version: V1
Endpoint: https://api.mangacollec.com/v1/types/
Method: GET
Response_brut: datas/types/endpoints/types_v1.json
Description: List all series and types for series
Authentication: false
---

# Endpoint GET /v1/types

## Description
Retourne la liste de tous les types de séries disponibles.

## Structure de la réponse

### Objet Type

| Champ   | Type   | Description                |
|---------|--------|----------------------------|
| `id`    | string | Identifiant unique du type |
| `title` | string | Titre du type de série     |

## Exemple de réponse

```json
[
    {
        "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
        "title": "Manga",
        "to_display": false
    }
]
```

## Notes

- Cet endpoint retourne uniquement les informations de base des types des series
- La réponse peut être très volumineuse, car elle contient tous les types
- Les types sont retournés sans ordre particulier
