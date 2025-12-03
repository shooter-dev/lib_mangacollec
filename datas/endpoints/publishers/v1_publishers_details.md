---
resource: publishers
version: v1
endpoint: /v1/publishers/{publisher_id}
method: GET
description: Get publisher by ID with full details
---

# Endpoint GET /v1/publishers/{publisher_id}

## Description
Retourne les informations détaillées d'un éditeur avec toutes ses éditions et séries associées.
----------
Returns detailed information about a publisher with all its associated editions and series.

## Structure de la réponse / Response Structure

### Objet Publisher / Publisher Object

| Champ | Type | Description |
|-------|------|-------------|
| `id` | string | Identifiant unique de l'éditeur |
| `title` | string | Nom de l'éditeur |
| `editions_count` | integer | Nombre d'éditions publiées |

## Notes

- Les champs marqués comme `null` sont optionnels
- Pour obtenir toutes les éditions, consultez l'endpoint dédié aux éditions
