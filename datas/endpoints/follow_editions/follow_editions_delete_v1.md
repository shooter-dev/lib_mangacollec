---
resource: follow_editions_delete
version: v1
endpoint: https://api.mangacollec.com/v1/follow_editions/{id_follow_edition}
method: DELETE
response_brut: datas/endpoints/follow_editions/follow_editions_delete_v1.json
description: Delete a follow edition from user's collection
authentication: true
---

# Endpoint DELETE /v1/follow_editions/{id_follow_edition}

## Description
Permet de supprimer un suivi d'édition de la collection personnelle de l'utilisateur. Cette opération supprime définitivement l'enregistrement de suivi, ce qui signifie que l'utilisateur ne suivra plus l'édition et ne recevra plus de notifications liées à celle-ci. Nécessite une authentification valide.

## Structure de la requête

### Paramètres de chemin

| Paramètre            | Type | Description                           |
|----------------------|------|---------------------------------------|
| `id_follow_edition` | str  | Identifiant unique du suivi à supprimer |

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
- L'identifiant `id_follow_edition` doit être au format UUID valide
- L'opération est irréversible : une fois le suivi supprimé, il ne peut pas être restauré
- Les champs `created_at` et `updated_at` sont au format ISO 8601
- L'utilisateur associé au `user_id` est celui qui fait la requête
- Si l'ID de suivi n'existe pas, une erreur 404 est retournée
- Si l'utilisateur n'est pas le propriétaire du suivi, une erreur 403 est retournée