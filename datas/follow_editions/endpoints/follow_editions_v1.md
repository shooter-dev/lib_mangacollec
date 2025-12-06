---
resource: follow_editions
version: v1
endpoint: https://api.mangacollec.com/v1/follow_editions
method: POST
response_brut: datas/_endpoints/follow_editions/follow_editions_v1.json
description: Follow or unfollow an edition
authentication: true
---

# Endpoint POST /v1/follow_editions

## Description
Permet de suivre une édition spécifique. Cet endpoint permet à un utilisateur de gérer son suivi d'éditions, ce qui lui permet de recevoir des notifications et de suivre les actualités liées à cette édition. L'opération s'effectue en utilisant un paramètre booléen pour suivre ou arrêter de suivre.

## Structure de la requête

### Structure principale requête

| Champ         | Type                | Description                              |
|---------------|---------------------|------------------------------------------|
| `edition_id`  | str                 | Identifiant unique de l'édition à suivre |
| `following`   | bool                | État de suivi (true pour suivre, false pour ne plus suivre) |

## Structure de la réponse

### Structure principale réponse

| Champ         | Type                | Description                           |
|---------------|---------------------|---------------------------------------|
| `id`          | str                 | Identifiant unique du suivi           |
| `user_id`     | str                 | Identifiant unique de l'utilisateur   |
| `edition_id`  | str                 | Identifiant unique de l'édition       |
| `following`   | bool                | État actuel du suivi                  |
| `created_at`  | str                 | Date de création du suivi (format ISO 8601) |
| `updated_at`  | str                 | Date de dernière mise à jour (format ISO 8601) |

## Exemple de requête

```json
{
    "edition_id": "bd982e24-525d-47cc-a152-7582e5f8236d",
    "following": true
}
```

## Exemple de réponse

```json
{
    "id": "bc325464-e110-49fa-b346-726d116f8975",
    "user_id": "1f32e2fc-c7c3-4dd3-9f18-e0fcdb075295",
    "edition_id": "bd982e24-525d-47cc-a152-7582e5f8236d",
    "following": true,
    "created_at": "2025-10-26T20:45:42.486Z",
    "updated_at": "2025-10-26T20:45:42.486Z"
}
```

## Notes

- Nécessite une authentification OAuth2 valide
- L'opération est idempotente : suivre une édition déjà suivie ou arrêter de suivre une édition non suivie ne génère pas d'erreur
- Les champs `created_at` et `updated_at` sont au format ISO 8601
- L'identifiant `id` est une chaîne de caractères au format UUID
- L'utilisateur associé au `user_id` est celui qui fait la requête
- Les notifications liées au suivi ne sont pas précisées ici mais peuvent être liées à cette fonctionnalité