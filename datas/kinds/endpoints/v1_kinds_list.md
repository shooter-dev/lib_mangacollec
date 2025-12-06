---
Resource: kinds
Version: v1
Endpoint: https://api.mangacollec.com/v1/kinds/
Method: GET
Response_brut: datas/_endpoints/kinds/v1_kinds_list.json
Authentication: false
Description: List all kinds
---

# Endpoint GET /v1/kinds/

## Description
Retourne la liste de tous les kinds disponibles avec leurs informations de base.
----------
Returns the list of all available kinds with their basic information.

## Structure de la réponse

### Structure principale

| Champ | Type | Description |
|-------|------|-------------|
| `kinds` | List[Kind] | Tableau des kinds |

### Objet Kind

| Champ        | Type         | Description                         |
|--------------|--------------|-------------------------------------|
| `id`         | string       | Identifiant unique du kind          |
| `title`      | string       | Titre du kind                       |
| `series_ids` | List[string] | Liste des IDs des séries de ce kind |

## Exemple de réponse

```json
[
    {
        "id": "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
        "title": "Action",
        "series_ids": [
            "ccff3d09-7619-4f3e-834e-7682b92023c0",
            "51287cee-3dcf-4c01-980f-5b0d23b63a0d",
            "2ecd1eb4-bbae-4cdc-b9a7-b9533724df45"
        ]
    }
]
```

## Notes

- Cet endpoint retourne uniquement les informations de base des kinds
- La réponse peut être très volumineuse, car elle contient tous les kinds
- Les kinds sont retournés sans ordre particulier
- Chaque kind contient une liste des IDs des séries associées à cette catégorie