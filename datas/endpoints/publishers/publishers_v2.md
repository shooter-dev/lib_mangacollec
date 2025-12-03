---
resource: publisher_list
version: v2
endpoint: https://api.mangacollec.com/v2/publishers/
method: GET
response_brut: datas/endpoints/publishers/publishers_v2.json
description: List all publishers
---

# Endpoint GET /v2/publishers

## Description
Retourne la liste de tous les éditeurs de manga disponibles (version V2 de l'API).

### Structure principale

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, contrairement 
à V1 qui utilise des objets imbriqués.

| Champ        | Type            | Description           |
|--------------|-----------------|-----------------------|
| `publishers` | List[Publisher] | Tableau des publisher |

### Objet Publisher

| Champ            | Type | Description                     |
|------------------|------|---------------------------------|
| `id`             | str  | Identifiant unique de l'éditeur |
| `title`          | str  | Nom de l'éditeur                |
| `closed`         | bool |                                 |
| `editions_count` | int  | Nombre d'éditions publiées      |
| `no_amazon`      | bool |                                 |

## Exemple de réponse

```json
{
    "publishers": [
        {
            "id": "bdef8c9e-7395-465d-8175-a1b985d4aa92",
            "title": "Pika",
            "closed": false,
            "editions_count": 691,
            "no_amazon": false
        }
    ]
}
```

## Notes

- Cet endpoint retourne uniquement la liste des publishers
- La version V2 utilise une structure avec un tableau "publishers" contenant les objets
- Pour obtenir les détails complets, utiliser la resource `publisher_detail`
- La réponse peut être très volumineuse, car elle contient tous les publishers
