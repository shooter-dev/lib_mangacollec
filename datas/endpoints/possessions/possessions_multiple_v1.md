---
resource: possessions_multiple
version: v1
endpoint: https://api.mangacollec.com/v1/possessions_multiple
method: POST
response_brut: datas/endpoints/possessions/possessions_multiple_v1.json
authentication: true
description: Add multiple volumes to user's collection
---

# Endpoint POST /v1/possessions_multiple

## Description
Permet d'ajouter un ou plusieurs volumes à la collection personnelle de l'utilisateur en une seule requête.
Lors de l'ajout d'une possession, le système suit automatiquement l'édition associée si ce n'est pas déjà fait.
Nécessite une authentification valide.

## Structure de la requête

### Structure principale requête

| Champ        | Type                     | Description                                 |
|--------------|--------------------------|---------------------------------------------|
| `volume_ids` | List[VolumeToPossession] | Liste des volumes à ajouter à la collection |

### Objet VolumeToPossession

| Champ        | Type | Description                            |
|--------------|------|----------------------------------------|
| `volume_id`  | str  | Identifiant unique du volume à ajouter |

## Structure de la réponse

### Structure principale réponse

| Champ             | Type                | Description                                         |
|-------------------|---------------------|-----------------------------------------------------|
| `possessions`     | List[Possession]    | Tableau des possessions créées                      |
| `follow_editions` | List[FollowEdition] | Tableau des suivis d'éditions créés automatiquement |

### Objet Possession

| Champ        | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la possession |
| `user_id`    | str  | ID de l'utilisateur               |
| `volume_id`  | str  | ID du volume possédé              |
| `created_at` | str  | Date d'ajout (format ISO 8601)    |

### Objet FollowEdition

| Champ        | Type | Description                           |
|--------------|------|---------------------------------------|
| `id`         | str  | Identifiant unique du suivi           |
| `edition_id` | str  | ID de l'édition suivie                |
| `user_id`    | str  | ID de l'utilisateur                   |
| `following`  | bool | Indique si l'édition est suivie       |
| `created_at` | str  | Date de création (format ISO 8601)    |
| `updated_at` | str  | Date de mise à jour (format ISO 8601) |

## Exemple de requête
**id:** id Volume

```json
[
    {
        "volume_id": "fdb3365e-b18d-45b3-9ab0-09b3b73b9367"
    }
]
```

## Exemple de réponse

```json
{
    "possessions": [],
    "follow_editions": []
}
```

## Notes

- Nécessite une authentification OAuth2 valide
- Permet d'ajouter jusqu'à 100 volumes par requête
- Le système suit automatiquement l'édition associée à chaque volume ajouté
- Si l'édition est déjà suivie, aucun nouveau suivi n'est créé
- Les dates suivent le format ISO 8601 (ex : "2025-10-26T19:46:02.397Z")
- Les IDs sont des chaînes de caractères au format UUID
- Si un volume est déjà possédé, aucune erreur n'est retournée
- L'ordre des possessions créées correspond à l'ordre des volumes dans la requête