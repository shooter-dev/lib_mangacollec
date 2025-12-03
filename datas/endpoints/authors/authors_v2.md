---
resource: author_list
version: v2
endpoint: https://api.mangacollec.com/v2/authors/
method: GET
response_brut: datas/endpoints/authors/authors_v2.json
description: List all authors
authentication: false
---

# Endpoint GET /v2/authors

## Description
Retourne la liste de tous les auteurs disponibles avec leurs informations de base (version V2 de l'API).

### Structure principale

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, contrairement 
à V1 qui utilise des objets imbriqués.

| Champ      | Type           | Description                           |
|------------|----------------|---------------------------------------|
| `authors`  | List[Author]   | Tableau des auteurs                   |


### Objet Auteur

| Champ         | Type          | Description                                 |
|---------------|---------------|---------------------------------------------|
| `id`          | str           | Identifiant uuid de l'auteur                |
| `name`        | str           | Nom de l'auteur                             |
| `first_name`  | Optional[str] | Prénom de l'auteur                          |
| `tasks_count` | int           | Nombre total de tâches associées à l'auteur |

## Exemple de réponse

```json
{
    "authors": [
        {
            "id": "370ac96c-49e0-4f09-b7c4-662cb1374b21",
            "name": "Kishimoto",
            "first_name": "Masashi",
            "tasks_count": 32
        }
    ]
}
```

## Notes

- Cet endpoint retourne uniquement la liste des auteurs
- La version V2 utilise une structure avec un tableau "authors" contenant les objets
- Pour obtenir les détails complets, utiliser la resource `author_detail`
- La réponse peut être très volumineuse, car elle contient tous les auteurs
- Les champs marqués comme `Optional[]` peuvent être null