---
resource: serie_list
version: v2
endpoint: https://api.mangacollec.com/v2/series/
method: GET
response_brut: datas/endpoints/series/series_v2.json
description: List all series
---

# Endpoint GET /v2/series

## Description
Retourne la liste de toutes les séries de manga disponibles avec leurs informations de base (version V2 de l'API).

## Structure de la réponse

### Structure principale

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, contrairement 
à V1 qui utilise des objets imbriqués.

| Champ    | Type        | Description        |
|----------|-------------|--------------------|
| `series` | List[Serie] | Tableau des series |
| `types`  | List[Type]  | Tableau des types  |

### Objet Serie

| Champ            | Type    | Description                       |
|------------------|---------|-----------------------------------|
| `id`             | string  | Identifiant unique de la série    |
| `title`          | string  | Titre de la série                 |
| `type_id`        | string  | Identifiant du type de série      |
| `adult_content`  | boolean | Contenu pour adultes (true/false) |
| `editions_count` | integer | Nombre d'éditions disponibles     |
| `tasks_count`    | integer | Nombre de tâches associées        |

### Objet Type

| Champ         | Type | Description                                      |
|---------------|------|--------------------------------------------------|
| `id`          | str  | Identifiant unique du type                       |
| `title`       | str  | Titre du type                                    |
| `to_display`  | bool | Indique si le type doit être affiché             |

## Notes

- Cet endpoint retourne uniquement la liste des series
- La version V2 utilise une structure avec les tableaux "series", "types" contenant les objets
- Pour obtenir les détails complets, utiliser la resource `serie_detail`
- La réponse peut être très volumineuse, car elle contient tous les series
- Les champs marqués comme `Optional[]` peuvent être null
