---
resource: volume_news
version: v2
endpoint: https://api.mangacollec.com/v2/volumes/news
method: GET
response_brut: datas/_endpoints/volumes/volumes_news_v2.json
description: Get latest published or announced volumes
authentication: false
---

# Endpoint GET /v2/volumes/news

## Description
Retourne la liste des derniers volumes de manga publiés ou annoncés (version V2 de l'API).

### Structure principale

| Champ                         | Type                    | Description                                              |
|-------------------------------|-------------------------|----------------------------------------------------------|
| `volumes`                     | List[Volume]            | Tableau des derniers volumes publiés ou annoncés         |
| `editions`                    | List[Edition]           | Tableau des éditions associées aux volumes               |
| `series`                      | List[Serie]             | Tableau des séries associées aux volumes                 |
| `types`                       | List[Type]              | Tableau des types de séries                              |
| `boxes`                       | List[Box]               | Tableau des coffrets inclus dans les recommandations     |
| `box_editions`                | List[BoxEdition]        | Tableau des éditions de coffrets                         |
| `box_volumes`                 | List[BoxVolume]         | Tableau des associations volumes-coffrets                |
| `native_ad_volume_home_first` | NativeAdVolumeHomeFirst | Informations sur les publicités natives pour les volumes |

### Objet Volume

| Champ               | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | str           | Identifiant uuid du volume              |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | int           | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | str           | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | bool          | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |

### Objet Edition

| Champ                   | Type          | Description                                                    |
|-------------------------|---------------|----------------------------------------------------------------|
| `id`                    | str           | Identifiant uuid de l'édition                                  |
| `title`                 | Optional[str] | Titre de l'édition                                             |
| `series_id`             | str           | Identifiant de la série parente                                |
| `publisher_id`          | str           | Identifiant de l'éditeur                                       |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente (pour les éditions spéciales) |
| `volumes_count`         | int           | Nombre de volumes dans l'édition                               |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié                                |
| `commercial_stop`       | bool          | Arrêt commercial                                               |
| `not_finished`          | bool          | Série non terminée                                             |
| `follow_editions_count` | int           | Nombre de personnes qui suivent cette édition                  |

### Objet Serie

| Champ            | Type  | Description                           |
|------------------|-------|---------------------------------------|
| `id`             | str   | Identifiant uuid de la série          |
| `title`          | str   | Titre de la série                     |
| `type_id`        | str   | Identifiant du type de série          |
| `adult_content`  | bool  | Contenu pour adultes                  |
| `editions_count` | int   | Nombre d'éditions disponibles         |
| `tasks_count`    | int   | Nombre de tâches associées à la série |

### Objet Type

| Champ        | Type | Description                          |
|--------------|------|--------------------------------------|
| `id`         | str  | Identifiant unique du type           |
| `title`      | str  | Nom du type                          |
| `to_display` | bool | Indique si le type doit être affiché |

### Objet Box

| Champ                   | Type          | Description                                      |
|-------------------------|---------------|--------------------------------------------------|
| `id`                    | str           | Identifiant unique du coffret                    |
| `title`                 | Optional[str] | Titre du coffret                                 |
| `number`                | int           | Numéro du coffret                                |
| `release_date`          | Optional[str] | Date de sortie (format ISO 8601)                 |
| `isbn`                  | Optional[str] | ISBN du coffret                                  |
| `asin`                  | Optional[str] | ASIN Amazon                                      |
| `commercial_stop`       | bool          | Indique si le coffret est arrêté commercialement |
| `box_edition_id`        | str           | ID de la box edition associée                    |
| `box_possessions_count` | Optional[int] | Nombre de possesseurs                            |
| `image_url`             | Optional[str] | URL de l'image                                   |

### Objet BoxEdition

| Champ                       | Type          | Description                                         |
|-----------------------------|---------------|-----------------------------------------------------|
| `id`                        | str           | Identifiant uuid de la box edition                  |
| `title`                     | Optional[str] | Titre de la box edition                             |
| `publisher_id`              | str           | ID de l'éditeur                                     |
| `boxes_count`               | int           | Nombre de boxes dans cette box edition              |
| `adult_content`             | bool          | Indique si le contenu est pour adultes              |
| `box_follow_editions_count` | int           | Nombre d'utilisateurs qui suivent cette box edition |

### Objet BoxVolume

| Champ       | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| `id`        | str  | Identifiant uuid de l'association               |
| `box_id`    | str  | ID du coffret                                   |
| `volume_id` | str  | ID du volume                                    |
| `included`  | bool | Indique si le volume est inclus dans le coffret |

### Objet NativeAddVolumeHomeFirst

| Champ        | Type          | Description                                   |
|--------------|---------------|-----------------------------------------------|
| `id`         | str           | Identifiant unique de la publicité native     |
| `volume_id`  | str           | ID du volume concerné par la publicité        |
| `title`      | str           | Titre de la publicité                         |
| `start_date` | Optional[str] | Date de début d'affichage (format YYYY-MM-DD) |
| `end_date`   | Optional[str] | Date de fin d'affichage (format YYYY-MM-DD)   |

## Exemple de réponse

```json
{
    "volumes": [],
    "editions": [],
    "series": [],
    "types": [],
    "boxes": [],
    "box_editions": [],
    "box_volumes": [],
    "native_ad_volume_home_first": {
        "id": "1402958a-67c0-45f1-84b9-9cbcf13f6b10",
        "volume_id": "ab9202dc-c43a-498f-b82e-ead6736b6dc7",
        "title": "Découvrir",
        "start_date": "2025-10-20",
        "end_date": "2025-10-26"
    }
}
```

## Notes / Notes

- Version V2 utilise une **structure normalisée** avec des tableaux séparés pour chaque type d'entité
- Les relations entre entités se font via les IDs (edition_id, series_id, etc.)
- Les volumes sont triés par date de sortie décroissante (du plus récent au plus ancien)
- Retourne à la fois les volumes récents (déjà publiés) et les volumes à venir (annoncés)
- Les champs marqués comme `Optional[]` sont optionnels et peuvent ne pas être présents dans toutes les réponses
- La réponse peut être très volumineuse, car elle contient de nombreuses entités associées
- Les coffrets (boxes) et leurs associations sont inclus lorsqu'ils font partie des nouveautés
- Les publicités natives (native_ad_volume_home_first) mettent en avant certains volumes spécifiques
