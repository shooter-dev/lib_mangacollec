---
resource: user_me_recommendation
version: v1
endpoint: https://api.mangacollec.com/v1/users/me/recommendation
method: GET
response_brut: datas/users/endpoints/user_me_recommendation_v1.json
description: Get personalized recommendations for authenticated user
authentication: true
---

# Endpoint GET /v1/users/me/recommendation

## Description
Retourne des recommandations personnalisées de mangas pour l'utilisateur authentifié basées sur sa collection et ses préférences. Chaque recommandation est un volume spécifique avec ses détails complets.

## Structure de la réponse / Response Structure

La réponse est un tableau d'objets Volume, chacun contenant des détails complets sur le volume recommandé, son édition, sa série et les auteurs associés.

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | string        | Identifiant unique du volume            |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | integer       | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `image_url`         | Optional[str] | URL de l'image de couverture            |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | string        | Identifiant de l'édition parente        |
| `possessions_count` | int           | Nombre de possesseurs du volume         |
| `not_sold`          | boolean       | Plus en vente                           |
| `edition`           | Edition       | Objet Edition détaillé                  |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | string        | Identifiant unique de l'édition                                |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | string        | Identifiant de la série parente                                |
| `publisher_id`          | string        | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | integer       | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[str] | Numéro du dernier volume publié                                |
| `commercial_stop`       | boolean       | Arrêt commercial                                               |
| `not_finished`          | boolean       | Série non terminée                                             |
| `follow_editions_count` | integer       | Nombre de personnes qui suivent cette édition                  |
| `series`                | Serie        | Objet Serie détaillé                                          |

### Objet Serie

| Champ            | Type        | Description                           |
|------------------|-------------|---------------------------------------|
| `id`             | string      | Identifiant unique de la série        |
| `title`          | string      | Titre de la série                     |
| `type_id`        | string      | Identifiant du type de série          |
| `adult_content`  | boolean     | Contenu pour adultes                  |
| `editions_count` | integer     | Nombre d'éditions disponibles         |
| `tasks_count`    | integer     | Nombre de tâches associées à la série |
| `tasks`          | List[Task]  | Liste des tâches de la série          |

### Objet Task

| Champ       | Type   | Description                    |
|-------------|--------|--------------------------------|
| `id`        | string | Identifiant unique de la tâche |
| `job_id`    | string | Identifiant du rôle/métier     |
| `series_id` | string | Identifiant de la série        |
| `author_id` | string | Identifiant de l'auteur        |
| `author`    | Author | Objet Author détaillé          |
| `job`       | Job    | Objet Job détaillé             |

### Objet Author

| Champ         | Type          | Description                                 |
|---------------|---------------|---------------------------------------------|
| `id`          | string        | Identifiant unique de l'auteur              |
| `name`        | string        | Nom de l'auteur                             |
| `first_name`  | Optional[str] | Prénom de l'auteur                          |
| `tasks_count` | integer       | Nombre total de tâches associées à l'auteur |
| `tasks`       | List[Task]    | Liste des tâches de l'auteur                |

### Objet Job

| Champ   | Type   | Description                                 |
|---------|--------|---------------------------------------------|
| `id`    | string | Identifiant unique du rôle                  |
| `title` | string | Titre du rôle (ex: "Auteur", "Dessinateur") |

## Exemple de réponse

```json
[
    {
        "id": "4a6b6005-1071-4204-9ce2-a678d97ea434",
        "title": null,
        "number": 0,
        "release_date": "2025-11-06",
        "image_url": "https://m.media-amazon.com/images/I/51HfZzSytHL.jpg",
        "isbn": "9791032724743",
        "asin": "B0FC1DWL9R",
        "edition_id": "eef4028e-9f0b-43ae-9fb1-26f59b24509f",
        "possessions_count": 59,
        "not_sold": false,
        "edition": {
            "id": "eef4028e-9f0b-43ae-9fb1-26f59b24509f",
            "title": null,
            "series_id": "456f35ba-b93a-4de7-abce-aee169a7af8e",
            "publisher_id": "74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf",
            "parent_edition_id": null,
            "volumes_count": 1,
            "last_volume_number": 0,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 1159,
            "series": {
                "id": "456f35ba-b93a-4de7-abce-aee169a7af8e",
                "title": "Artbook Les Carnets de l'apothicaire",
                "type_id": "f41d81b0-fca6-4445-a903-da310e0899d2",
                "adult_content": false,
                "editions_count": 1,
                "tasks_count": 1,
                "tasks": [
                    {
                        "id": "60a7ca86-e40b-4215-8a19-1d2797bdafd8",
                        "job_id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
                        "series_id": "456f35ba-b93a-4de7-abce-aee169a7af8e",
                        "author_id": "f6ad072b-b030-4905-a03a-411eb39d042c",
                        "author": {
                            "id": "f6ad072b-b030-4905-a03a-411eb39d042c",
                            "name": "Nekokurage",
                            "first_name": "",
                            "tasks_count": 2,
                            "tasks": [
                                {
                                    "id": "f1f24e50-a55d-4c9d-a4b6-c596700ff75b",
                                    "job_id": "37fb2477-ec0d-4ffc-9d3b-4189c2d01629",
                                    "series_id": "cbc376d9-130c-4e17-9954-752c20133aa2",
                                    "author_id": "f6ad072b-b030-4905-a03a-411eb39d042c",
                                    "series": {
                                        "id": "cbc376d9-130c-4e17-9954-752c20133aa2",
                                        "title": "Les Carnets de l'Apothicaire",
                                        "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
                                        "adult_content": false,
                                        "editions_count": 4,
                                        "tasks_count": 3
                                    },
                                    "job": {
                                        "id": "37fb2477-ec0d-4ffc-9d3b-4189c2d01629",
                                        "title": "Dessin"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
]
```

## Notes

- Nécessite une authentification OAuth2 valide
- Les recommandations sont basées sur la collection de l'utilisateur et ses préférences
- Chaque recommandation est un volume spécifique plutôt qu'une série générale
- La structure utilise des objets imbriqués pour fournir toutes les informations nécessaires
- Les champs marqués comme `Optional[]` sont optionnels et peuvent ne pas être présents dans toutes les réponses
- Le nombre `possessions_count` indique combien de membres possèdent ce volume dans leurs collections
- `not_sold` indique si le volume n'est plus disponible à la vente
