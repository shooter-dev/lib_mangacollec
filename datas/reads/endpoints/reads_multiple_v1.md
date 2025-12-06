---
resource: reads_multiple
version: v1
endpoint: https://api.mangacollec.com/v1/reads_multiple
method: POST
response_brut: datas/reads/endpoints/reads_multiple_v1.json
description: Mark multiple volumes as read
authentication: true
---

# Endpoint POST /v1/reads_multiple

## Description
Permet de marquer un ou plusieurs volumes comme lus en une seule requête.
Lors du marquage d'une lecture, le système suit automatiquement l'édition associée comme étant en cours de lecture si ce n'est pas déjà fait.
Nécessite une authentification valide.

## Structure de la requête

### Structure principale requête

| Champ      | Type               | Description                           |
|------------|--------------------|---------------------------------------|
| `read_ids` | List[VolumeToRead] | Liste des volumes à marquer comme lus |

### Objet VolumeToRead

| Champ       | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| `volume_id` | str  | Identifiant unique du volume à marquer comme lu |

## Structure de la réponse

### Structure principale réponse

| Champ           | Type              | Description                                            |
|-----------------|-------------------|--------------------------------------------------------|
| `reads`         | List[Read]        | Tableau des lectures créées                            |
| `read_editions` | List[ReadEdition] | Tableau des lectures d'éditions créées automatiquement |

### Objet Read

| Champ        | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la lecture    |
| `user_id`    | str  | ID de l'utilisateur               |
| `volume_id`  | str  | ID du volume lu                   |
| `created_at` | str  | Date de lecture (format ISO 8601) |

### Objet ReadEdition

| Champ        | Type | Description                                  |
|--------------|------|----------------------------------------------|
| `id`         | str  | Identifiant uuid de la lecture               |
| `edition_id` | str  | ID de l'édition                              |
| `user_id`    | str  | ID de l'utilisateur                          |
| `reading`    | bool | Indique si l'édition est en cours de lecture |
| `created_at` | str  | Date de création (format ISO 8601)           |

## Exemple de requête
**id:** id Read

```json
[
    {
        "volume_id": "dcf1f103-48d0-4a0a-b20a-acc20f656f04"
    }
]
```

## Exemple de réponse

```json
{
    "reads": [],
    "read_editions": []
}
```

## Notes

- Nécessite une authentification OAuth2 valide
- Permet de marquer jusqu'à 100 volumes comme lus par requête
- Le système suit automatiquement l'édition associée à chaque volume marqué comme lu
- Si l'édition est déjà suivie en lecture, aucun nouveau suivi n'est créé
- Les dates suivent le format ISO 8601 (ex: "2025-10-26T19:57:46.199Z")
- Les IDs sont des chaînes de caractères au format UUID
- Si un volume est déjà marqué comme lu, aucune erreur n'est retournée
- L'ordre des lectures créées correspond à l'ordre des volumes dans la requête