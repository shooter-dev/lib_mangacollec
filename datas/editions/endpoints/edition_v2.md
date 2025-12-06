---
resource: edition_detail
version: v2
endpoint: https://api.mangacollec.com/v2/editions/{edition_id}
method: GET
response_brut: datas/_endpoints/editions/edition_v2.json
description: Get edition by ID with full details
---

# Endpoint GET /v2/editions/{edition_id}

## Description
Retourne les informations détaillées d'une édition avec toutes ses entités associées (série, éditeur, volumes) 
en structure normalisée (version V2 de l'API).

## Structure de la réponse

La réponse V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité, 
contrairement à V1 qui utilise des objets imbriqués.

### Structure principale

| Champ        | Type            | Description                 |
|--------------|-----------------|-----------------------------|
| `editions`   | List[Edition]   | Tableau des éditions        |
| `publishers` | List[Publisher] | Tableau des éditeurs        |
| `series`     | List[Serie]     | Tableau des séries          |
| `types`      | List[Type]      | Tableau des types de séries |
| `volumes`    | List[Volume]    | Tableau des volumes         |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | string        | Identifiant uuid de l'édition                                  |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | string        | Identifiant de la série parente                                |
| `publisher_id`          | string        | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | integer       | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié                                |
| `commercial_stop`       | boolean       | Arrêt commercial                                               |
| `not_finished`          | boolean       | Série non terminée                                             |
| `follow_editions_count` | integer       | Nombre de personnes qui suivent cette édition                  |

### Objet Publisher

| Champ              | Type    | Description                                    |
|--------------------|---------|------------------------------------------------|
| `id`               | string  | Identifiant uuid de l'éditeur                  |
| `title`            | string  | Nom de l'éditeur                               |
| `closed`           | boolean | Éditeur fermé                                  |
| `editions_count`   | integer | Nombre d'éditions disponibles chez cet éditeur |
| `no_amazon`        | boolean | Disponibilité Amazon (true = non disponible)   |

### Objet Serie

| Champ            | Type    | Description                           |
|------------------|---------|---------------------------------------|
| `id`             | string  | Identifiant uuid de la série          |
| `title`          | string  | Titre de la série                     |
| `type_id`        | string  | Identifiant du type de série          |
| `adult_content`  | boolean | Contenu pour adultes                  |
| `editions_count` | integer | Nombre d'éditions disponibles         |
| `tasks_count`    | integer | Nombre de tâches associées à la série |

### Objet Type

| Champ        | Type    | Description                |
|--------------|---------|----------------------------|
| `id`         | string  | Identifiant uuid du type   |
| `title`      | string  | Nom du type                |
| `to_display` | boolean | Afficher dans l'interface  |

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | string        | Identifiant uuid du volume              |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | integer       | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | string        | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | boolean       | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |

## Exemple de réponse

```json
{
    "editions": [],
    "publishers": [],
    "series": [],
    "types": [],
    "volumes": []
}
```

## Notes

- La version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque entité
- Les relations entre entités se font via les IDs
- Contrairement à V1, les objets ne sont pas imbriqués
- Les champs marqués comme `Optional[]` peuvent être null
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux
- Une édition peut avoir des éditions enfants (ex : éditions collector) via `parent_edition_id`
