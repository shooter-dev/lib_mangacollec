---
Resource: job_list
Version: V1
Endpoint: https://api.mangacollec.com/v1/jobs/
Method: GET
Response_brut: datas/endpoints/jobs/jobs_v1.json
Description: List all jobs
Authentication: false
---

# Endpoint GET /v1/jobs/

## Description
Retourne la liste de tous les jobs disponibles avec leurs informations de base.

## Structure de la réponse

### Structure principale

| Champ  | Type      | Description                  |
|--------|-----------|------------------------------|
| `jobs` | List[Job] | Tableau des jobs disponibles |

### Objet Job

| Champ   | Type | Description             |
|---------|------|-------------------------|
| `id`    | str  | Identifiant uuid du job |
| `title` | str  | Titre du job            |

## Exemple de réponse

```json
[
    {
        "id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
        "title": "Auteur"
    }
]
```

## Notes

- Cet endpoint retourne uniquement les informations de base des jobs
- La réponse peut être très volumineuse, car elle contient tous les jobs
- Les jobs sont retournés sans ordre particulier
