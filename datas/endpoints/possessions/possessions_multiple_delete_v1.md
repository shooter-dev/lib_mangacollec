---
resource: possessions_multiple_delete
version: v1
endpoint: https://api.mangacollec.com/v1/possessions_multiple
method: DELETE
response_brut: datas/endpoints/possessions/possessions_multiple_delete_v1.json
description: Remove multiple possessions from user's collection
authentication: true
---

# Endpoint DELETE /v1/possessions_multiple

## Description
Permet de supprimer un ou plusieurs enregistrements de possession de la collection personnelle de l'utilisateur en une seule requête.
Lors de la suppression d'une possession, le système supprime automatiquement le suivi de l'édition associée si c'était la seule possession de cette édition.
Si des prêts sont associés à la possession, ils sont également supprimés.
Nécessite une authentification valide.

## Structure de la requête

### Structure principale requête

| Champ            | Type                       | Description                                  |
|------------------|----------------------------|----------------------------------------------|
| `possession_ids` | List[PossessionToDelete]   | Liste des possessions à supprimer       |

### Objet PossessionToDelete

| Champ | Type | Description                         |
|--------|------|-------------------------------------|
| `id`    | str  | Identifiant unique de la possession à supprimer |

## Structure de la réponse

### Structure principale réponse

| Champ             | Type                       | Description                                        |
|-------------------|----------------------------|----------------------------------------------------|
| `possessions`     | List[PossessionDeleted]    | Tableau des possessions supprimées                    |
| `follow_editions` | List[FollowEditionDeleted] | Tableau des suivis d'éditions supprimés automatiquement |
| `loans`           | List[LoanDeleted]          | Tableau des prêts supprimés automatiquement           |

### Objet PossessionDeleted

| Champ    | Type | Description                           |
|----------|------|---------------------------------------|
| `id`      | str  | Identifiant unique de la possession   |
| `deleted` | bool | Indique si la suppression a réussi  |

### Objet FollowEditionDeleted

| Champ    | Type | Description                                |
|----------|------|--------------------------------------------|
| `id`      | str  | Identifiant unique du suivi d'édition    |
| `deleted` | bool | Indique si la suppression a réussi     |

### Objet LoanDeleted

| Champ    | Type | Description                        |
|----------|------|------------------------------------|
| `id`      | str  | Identifiant unique du prêt     |
| `deleted` | bool | Indique si la suppression a réussi  |

## Exemple de requête

```json
[
    {
        "id": "c3c66009-f8c5-4d4e-abcc-a34591f29166"
    }
]
```

## Exemple de réponse

```json
{
    "possessions": [
        {
            "id": "c3c66009-f8c5-4d4e-abcc-a34591f29166",
            "deleted": true
        }
    ],
    "follow_editions": [
        {
            "id": "9e0b1776-546e-4d1f-8856-e22ba47dec68",
            "deleted": true
        }
    ],
    "loans": []
}
```

## Notes

- Nécessite une authentification OAuth2 valide
- Permet de supprimer jusqu'à 100 possessions par requête
- Le système supprime automatiquement le suivi de l'édition associée si c'était la seule possession de cette édition
- Si d'autres possessions existent pour la même édition, l'édition reste suivie
- Les prêts associés aux possessions supprimées sont automatiquement supprimés
- Les objets retournés contiennent un champ `deleted` pour confirmer le succès de l'opération
- Le tableau `loans` peut être vide si aucun prêt n'était associé aux possessions supprimées
- Les IDs sont des chaînes de caractères au format UUID
- Si une possession n'existe pas, aucune erreur n'est retournée
- L'ordre des réponses correspond à l'ordre des IDs dans la requête