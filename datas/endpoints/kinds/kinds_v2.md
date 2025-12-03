---
resource: kind_list
version: v2
endpoint: https://api.mangacollec.com/v2/kinds/
method: GET
response_brut: datas/endpoints/kinds/kinds_v2.json
description: List all kinds
---

# Endpoint GET /v2/kinds/

## Description
Retourne la liste de tous les kinds disponibles avec leurs informations de base (version V2 de l'API).

### Structure principale

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, contrairement 
à V1 qui utilise des objets imbriqués.

| Champ   | Type       | Description       |
|---------|------------|-------------------|
| `kinds` | List[Kind] | Tableau des kinds |

### Objet Kind

| Champ        | Type         | Description                                |
|--------------|--------------|--------------------------------------------|
| `id`         | string       | Identifiant uuid du kind                   |
| `title`      | string       | Titre du kind                              |
| `series_ids` | List[string] | Liste des IDs `uuid` des séries de ce kind |

## Exemple de réponse

```json
{
    "kinds": [
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
}
```

## Notes

- Cet endpoint retourne uniquement la liste des kinds
- La version V2 utilise une structure avec un tableau "kinds" contenant les objets
- La réponse peut être très volumineuse, car elle contient tous les kinds
- Les kinds sont retournés sans ordre particulier
- Chaque kind contient une liste des IDs des séries associées à cette catégorie
