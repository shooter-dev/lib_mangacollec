---
resource: reads_multiple_delete
version: v1
endpoint: https://api.mangacollec.com/v1/reads_multiple
method: DELETE
response_brut: datas/reads/endpoints/reads_multiple_delete_v1.json
description: Remove multiple reads from user's collection
authentication: true
---

# Endpoint DELETE /v1/reads_multiple

## Description
Permet de supprimer un ou plusieurs enregistrements de lecture de la collection personnelle de l'utilisateur en une seule requête.
Lors de la suppression d'une lecture, le système supprime automatiquement l'édition associée en cours de lecture si c'était la dernière lecture de cette édition.
Nécessite une authentification valide.

## Structure de la requête

### Structure principale requête

| Champ      | Type               | Description                    |
|------------|--------------------|--------------------------------|
| `read_ids` | List[ReadToDelete] | Liste des lectures à supprimer |

### Objet ReadToDelete

| Champ | Type | Description                                  |
|-------|------|----------------------------------------------|
| `id`  | str  | Identifiant unique de la lecture à supprimer |

## Structure de la réponse

### Structure principale réponse

| Champ           | Type                     | Description                                                |
|-----------------|--------------------------|------------------------------------------------------------|
| `reads`         | List[ReadDeleted]        | Tableau des lectures supprimées                            |
| `read_editions` | List[ReadEditionDeleted] | Tableau des lectures d'éditions supprimées automatiquement |

### Objet ReadDeleted

| Champ     | Type | Description                        |
|-----------|------|------------------------------------|
| `id`      | str  | Identifiant unique de la lecture   |
| `deleted` | bool | Indique si la suppression a réussi |

### Objet ReadEditionDeleted

| Champ     | Type | Description                                |
|-----------|------|--------------------------------------------|
| `id`      | str  | Identifiant unique de la lecture d'édition |
| `deleted` | bool | Indique si la suppression a réussi         |

## Exemple de requête
**id:** id Read
```json
[
    {
        "id": "dcf1f103-48d0-4a0a-b20a-acc20f656f04"
    }
]
```

## Exemple de réponse

```json
{
    "reads": [
        {
            "id": "0994509d-1227-411d-ac18-73708b3f6371",
            "deleted": true
        }
    ],
    "read_editions": [
        {
            "id": "3a15a949-28f8-4ab9-bdc2-94df79b84d6d",
            "deleted": true
        }
    ]
}
```

## Notes

- Nécessite une authentification OAuth2 valide
- Permet de supprimer jusqu'à 100 lectures par requête
- Le système supprime automatiquement l'édition associée en cours de lecture si c'était la dernière lecture de cette édition
- Si d'autres lectures existent pour la même édition, l'édition reste marquée comme étant en cours de lecture
- Les objets retournés contiennent un champ `deleted` pour confirmer le succès de l'opération
- Les IDs sont des chaînes de caractères au format UUID
- Si une lecture n'existe pas, aucune erreur n'est retournée
- L'ordre des réponses correspond à l'ordre des IDs dans la requête