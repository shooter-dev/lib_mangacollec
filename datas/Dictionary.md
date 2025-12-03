# Dictionary des objets de l'API MangaCollection

Ce dictionnaire répertorie tous les objets JSON réels retournés par les endpoints de l'API MangaCollection, avec leurs propriétés et les endpoints associés.

## Objets de l'API Input

### VolumeToPossession
**Type** : VolumeToPossession

| Propriété   | Type | Description                                            |
|-------------|------|--------------------------------------------------------|
| `volume_id` | str  | Identifiant unique du volume à ajouter à la collection |

**Endpoints où cet objet est envoyé** :
- `/v1/possessions_multiple` (possessions_multiple_v1.md)

---

### VolumeToRead
**Type** : VolumeToRead

| Propriété   | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| `volume_id` | str  | Identifiant unique du volume à marquer comme lu |

**Endpoints où cet objet est envoyé** :
- `/v1/reads_multiple` (reads_multiple_v1.md)

---

### ReadToDelete
**Type** : ReadToDelete

| Propriété | Type | Description                            |
|-----------|------|----------------------------------------|
| `id`      | str  | Identifiant unique de Read à supprimer |

**Endpoints où cet objet est envoyé** :
- `/v1/reads_multiple` (reads_multiple_delete_v1.md)

---

### PossessionToDelete
**Type** : PossessionToDelete

| Propriété | Type | Description                                  |
|-----------|------|----------------------------------------------|
| `id`      | str  | Identifiant unique de Possession à supprimer |

**Endpoints où cet objet est envoyé** :
- `/v1/possessions_multiple` (possessions_multiple_delete_v1.md)

---

### FollowEditionInput
**Type** : FollowEditionInput

| Propriété    | Type | Description                                                    |
|--------------|------|----------------------------------------------------------------|
| `edition_id` | str  | Identifiant unique de l'édition à suivre                       |
| `following`  | bool | État de suivi (true pour suivre, false pour arrêter de suivre) |

**Endpoints où cet objet est envoyé** :
- `/v1/follow_editions` (follow_editions_v1.md)

---

## Objets de l'API Output

### Author
**Type** : Author

| Propriété     | Type          | Description                                 |
|---------------|---------------|---------------------------------------------|
| `id`          | str           | Identifiant unique de l'auteur              |
| `name`        | str           | Nom de l'auteur                             |
| `first_name`  | Optional[str] | Prénom de l'auteur                          |
| `tasks_count` | int           | Nombre total de tâches associées à l'auteur |

**Endpoints où cet objet est retourné** :
- `/v2/authors/` (authors_v2.md)
- `/v2/authors/{author_id}` (author_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)

---

### Serie
**Type** : Serie

| Propriété        | Type      | Description                           |
|------------------|-----------|---------------------------------------|
| `id`             | str       | Identifiant unique de la série        |
| `title`          | str       | Titre de la série                     |
| `type_id`        | str       | Identifiant du type de série          |
| `adult_content`  | bool      | Contenu pour adultes                  |
| `editions_count` | int       | Nombre d'éditions disponibles         |
| `tasks_count`    | int       | Nombre de tâches associées à la série |

**Endpoints où cet objet est retourné** :
- `/v2/series/` (series_v2.md)
- `/v2/authors/` (author_v2.md)
- `/v2/editions/{edition_id}` (edition_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

**Type** : SerieDetail

| Propriété        | Type      | Description                           |
|------------------|-----------|---------------------------------------|
| `id`             | str       | Identifiant unique de la série        |
| `title`          | str       | Titre de la série                     |
| `type_id`        | str       | Identifiant du type de série          |
| `adult_content`  | bool      | Contenu pour adultes                  |
| `editions_count` | int       | Nombre d'éditions disponibles         |
| `tasks_count`    | int       | Nombre de tâches associées à la série |
| `kinds_ids`      | List[str] | Liste des IDs des kinds               |

**Endpoints où cet objet est retourné** :
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### Edition
**Type** : Edition

| Propriété               | Type          | Description                                   |
|-------------------------|---------------|-----------------------------------------------|
| `id`                    | str           | Identifiant unique de l'édition               |
| `title`                 | Optional[str] | Titre de l'édition                            |
| `series_id`             | str           | Identifiant de la série parente               |
| `publisher_id`          | str           | Identifiant de l'éditeur                      |
| `parent_edition_id`     | Optional[str] | Identifiant de l'édition parente              |
| `volumes_count`         | int           | Nombre de volumes dans l'édition              |
| `last_volume_number`    | Optional[int] | Numéro du dernier volume publié               |
| `commercial_stop`       | bool          | Arrêt commercial                              |
| `not_finished`          | bool          | Série non terminée                            |
| `follow_editions_count` | int           | Nombre de personnes qui suivent cette édition |

**Endpoints où cet objet est retourné** :
- `/v2/editions/{edition_id}` (edition_v2.md)
- `/v2/authors/` (author_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

### Volume
**Type** : Volume

| Propriété           | Type          | Description                              |
|---------------------|---------------|------------------------------------------|
| `id`                | str           | Identifiant unique du volume             |
| `title`             | Optional[str] | Titre du volume                          |
| `number`            | int           | Numéro du volume                         |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD)  |
| `isbn`              | Optional[str] | ISBN du volume                           |
| `asin`              | Optional[str] | ASIN Amazon du volume                    |
| `edition_id`        | str           | Identifiant de l'édition parente         |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume          |
| `not_sold`          | bool          | Plus en vente                            |
| `image_url`         | Optional[str] | URL de l'image de couverture             |

**Endpoints où cet objet est retourné** :
- `/v2/volumes/news` (volumes_news_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/authors/{author_id}` (author_v2.md)
- `/v2/editions/{edition_id}` (edition_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

**Type** : VolumeDetail

| Propriété           | Type          | Description                             |
|---------------------|---------------|-----------------------------------------|
| `id`                | str           | Identifiant unique du volume            |
| `title`             | Optional[str] | Titre du volume                         |
| `number`            | int           | Numéro du volume                        |
| `release_date`      | Optional[str] | Date de publication (format YYYY-MM-DD) |
| `isbn`              | Optional[str] | ISBN du volume                          |
| `asin`              | Optional[str] | ASIN Amazon du volume                   |
| `edition_id`        | str           | Identifiant de l'édition parente        |
| `possessions_count` | Optional[int] | Nombre de possesseurs du volume         |
| `not_sold`          | bool          | Plus en vente                           |
| `image_url`         | Optional[str] | URL de l'image de couverture            |
| `nb_pages`          | Optional[int] | Nombre de pages du volume               |
| `content`           | Optional[str] | Contenu/description du volume           |

**Endpoints où cet objet est retourné** :
- `/v2/volumes/{volume_id}` (volume_v2.md)

---

### Publisher
**Type** : Publisher

| Propriété        | Type | Description                     |
|------------------|------|---------------------------------|
| `id`             | str  | Identifiant unique de l'éditeur |
| `title`          | str  | Nom de l'éditeur                |
| `closed`         | bool | Éditeur fermé                   |
| `editions_count` | int  | Nombre d'éditions disponibles   |
| `no_amazon`      | bool | Disponibilité Amazon            |

**Endpoints où cet objet est retourné** :
- `/v2/publishers/` (publishers_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/editions/{edition_id}` (edition_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)

---

### Type
**Type** : Type

| Propriété    | Type  | Description                             |
|--------------|-------|-----------------------------------------|
| `id`         | str   | Identifiant unique du type              |
| `title`      | str   | Nom du type                             |
| `to_display` | bool  | Afficher dans l'interface               |

**Endpoints où cet objet est retourné** :
- `/v1/types/` (types_v1.md)
- `/v2/series/` (series_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/editions/{edition_id}` (edition_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

### Kind
**Type** : Kind

| Propriété    | Type      | Description                          |
|--------------|-----------|--------------------------------------|
| `id`         | str       | Identifiant unique du genre          |
| `title`      | str       | Titre du genre                       |

**Endpoints où cet objet est retourné** :
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

**Type** : KindDetail

| Propriété    | Type      | Description                          |
|--------------|-----------|--------------------------------------|
| `id`         | str       | Identifiant unique du genre          |
| `title`      | str       | Titre du genre                       |
| `series_ids` | List[str] | Liste des IDs des séries de ce genre |

**Endpoints où cet objet est retourné** :
- `/v2/kinds/` (kinds_v2.md)

---

### Task
**Type** : Task

| Propriété   | Type | Description                    |
|-------------|------|--------------------------------|
| `id`        | str  | Identifiant unique de la tâche |
| `job_id`    | str  | Identifiant du rôle/métier     |
| `series_id` | str  | Identifiant de la série        |
| `author_id` | str  | Identifiant de l'auteur        |

**Endpoints où cet objet est retourné** :
- `/v1/authors/{author_id}` (author_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)

---

### Job
**Type** : Job

| Propriété | Type |                                                 |
|-----------|------|-------------------------------------------------|
| `id`      | str  | Identifiant unique du rôle                      |
| `title`   | str  | Titre du rôle (ex: "Auteur", "Auteur original") |

**Endpoints où cet objet est retourné** :
- `/v1/jobs/` (jobs_v1.md)
- `/v2/authors/{author_id}` (author_v2.md)
- `/v2/series/{series_id}` (serie_v2.md)

---

### BoxEdition
**Type** : BoxEdition

| Propriété                   | Type          | Description                                    |
|-----------------------------|---------------|------------------------------------------------|
| `id`                        | str           | Identifiant unique de la box édition           |
| `title`                     | Optional[str] | Titre de la box édition                        |
| `publisher_id`              | str           | Identifiant de l'éditeur                       |
| `boxes_count`               | int           | Nombre de coffrets dans la box édition         |
| `adult_content`             | bool          | Contenu pour adultes                           |
| `box_follow_editions_count` | int           | Nombre de personnes qui suivent la box édition |

**Endpoints où cet objet est retourné** :
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

### Box
**Type** : Box

| Propriété               | Type          |                                                         |
|-------------------------|---------------|---------------------------------------------------------|
| `id`                    | str           | Identifiant unique du coffret                           |
| `title`                 | Optional[str] | Titre du coffret                                        |
| `number`                | int           | Numéro du coffret                                       |
| `release_date`          | Optional[str] | Date de publication (format YYYY-MM-DD, peut être null) |
| `isbn`                  | Optional[str] | ISBN du coffret                                         |
| `asin`                  | Optional[str] | ASIN Amazon du coffret                                  |
| `commercial_stop`       | bool          | Arrêt commercial                                        |
| `box_edition_id`        | str           | Identifiant de la box édition parente                   |
| `box_possessions_count` | Optional[int] | Nombre de possesseurs du coffret                        |
| `image_url`             | Optional[str] | URL de l'image de couverture                            |

**Endpoints où cet objet est retourné** :
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/publishers/{publisher_id}` (publisher_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

### BoxVolume
**Type** : BoxVolume

| Propriété   | Type |                                           |
|-------------|------|-------------------------------------------|
| `id`        | str  | Identifiant unique du volume dans coffret |
| `box_id`    | str  | Identifiant du coffret parent             |
| `volume_id` | str  | Identifiant du volume                     |
| `number`    | int  | Numéro du volume dans le coffret          |

**Endpoints où cet objet est retourné** :
- `/v2/series/{series_id}` (serie_v2.md)
- `/v2/planning/` (planning_v2.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)
- `/v2/volumes/{volume_id}` (volume_v2.md)
- `/v2/volumes/news` (volumes_news_v2.md)

---

### BDFugueOffer
**Type** : BDFugueOffer

| Propriété         | Type          | Description                    |
|-------------------|---------------|--------------------------------|
| `id`              | str           | Identifiant unique de l'offre  |
| `formatted_price` | Optional[str] | Prix formaté de l'offre        |
| `availability`    | Optional[str] | Disponibilité de l'offre       |
| `merchant`        | str           | Nom du marchand                |
| `store_link`      | str           | Lien vers la boutique en ligne |

**Endpoints où cet objet est retourné** :
- `/v1/offers/bdfugue/{volume_isbn}` (offers/bdfugue_offer_v1.md)

---

### AmazonOffer
**Type** : AmazonOffer

| Propriété         | Type          | Description                      |
|-------------------|---------------|----------------------------------|
| `asin`            | str           | ASIN Amazon du produit           |
| `formatted_price` | Optional[str] | Prix formaté sur Amazon          |
| `availability`    | Optional[str] | Disponibilité sur Amazon         |
| `merchant`        | str           | Nom du vendeur Amazon            |
| `store_link`      | str           | Lien vers la page produit Amazon |

**Endpoints où cet objet est retourné** :
- `/v1/offers/amazon/{volume_asin}` (offers/amazon_offer_v1.md)

---

### NativeAdVolumeHomeFirst
**Type** : NativeAdVolumeHomeFirst

| Propriété    | Type          | Description                         |
|--------------|---------------|-------------------------------------|
| `id`         | str           | Identifiant unique de la publicité  |
| `volume_id`  | str           | ID du volume associé à la publicité |
| `title`      | Optional[str] | Titre de la publicité               |
| `start_date` | Optional[str] | Date de début (format YYYY-MM-DD)   |
| `end_date`   | Optional[str] | Date de fin (format YYYY-MM-DD)     |

**Endpoints où cet objet est retourné** :
- `/v2/volumes/news` (volumes_news_v2.md)

---

### FollowEdition
**Type** : FollowEdition

| Propriété    | Type | Description                           |
|--------------|------|---------------------------------------|
| `id`         | str  | Identifiant unique du suivi           |
| `edition_id` | str  | ID de l'édition suivie                |
| `user_id`    | str  | ID de l'utilisateur                   |
| `following`  | bool | Indique si l'édition est suivie       |
| `created_at` | str  | Date de création (format ISO 8601)    |
| `updated_at` | str  | Date de mise à jour (format ISO 8601) |

**Endpoints où cet objet est retourné** :
- `/v1/follow_editions` (follow_editions_v1.md)
- `/v1/follow_editions/{id_follow_edition}` (follow_editions_delete_v1.md)
- `/v1/possessions_multiple` (possessions_multiple_v1.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### Possession
**Type** : Possession

| Propriété    | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la possession |
| `volume_id`  | str  | ID du volume possédé              |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date d'ajout (format ISO 8601)    |

**Endpoints où cet objet est retourné** :
- `/v1/possessions_multiple` (possessions_multiple_v1.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### BoxFollowEdition
**Type** : BoxFollowEdition

| Propriété        | Type | Description                           |
|------------------|------|---------------------------------------|
| `id`             | str  | Identifiant unique du suivi           |
| `box_edition_id` | str  | ID de la box edition suivie           |
| `user_id`        | str  | ID de l'utilisateur                   |
| `following`      | bool | Indique si la box edition est suivie  |
| `created_at`     | str  | Date de création (format ISO 8601)    |
| `updated_at`     | str  | Date de mise à jour (format ISO 8601) |

**Endpoints où cet objet est retourné** :
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### BoxPossession
**Type** : BoxPossession

| Propriété    | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la possession |
| `box_id`     | str  | ID du coffret possédé             |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date d'ajout (format ISO 8601)    |

**Endpoints où cet objet est retourné** :
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### ReadEdition
**Type** : ReadEdition

| Propriété    | Type | Description                                  |
|--------------|------|----------------------------------------------|
| `id`         | str  | Identifiant uuid de la lecture               |
| `edition_id` | str  | ID de l'édition                              |
| `user_id`    | str  | ID de l'utilisateur                          |
| `reading`    | bool | Indique si l'édition est en cours de lecture |
| `created_at` | str  | Date de création (format ISO 8601)           |
| `updated_at` | str  | Date de mise à jour (format ISO 8601)        |

**Endpoints où cet objet est retourné** :
- `/v1/reads_multiple` (reads_multiple_v1.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### Read
**Type** : Read

| Propriété    | Type | Description                       |
|--------------|------|-----------------------------------|
| `id`         | str  | Identifiant uuid de la lecture    |
| `volume_id`  | str  | ID du volume lu                   |
| `user_id`    | str  | ID de l'utilisateur               |
| `created_at` | str  | Date de lecture (format ISO 8601) |

**Endpoints où cet objet est retourné** :
- `/v1/reads_multiple` (reads_multiple_v1.md)
- `/v2/users/me/collection` (users_me_collection_v2.md)
- `/v2/user/{username}/collection` (users_collection_username_v2.md)

---

### Borrower
**Type** : Borrower

| Propriété    | Type | Description                        |
|--------------|------|------------------------------------|
| `id`         | str  | Identifiant uuid de l'emprunteur   |
| `user_id`    | str  | ID de l'utilisateur propriétaire   |
| `title`      | str  | Nom de l'emprunteur                |
| `category`   | str  | Catégorie de l'emprunteur          |
| `created_at` | str  | Date de création (format ISO 8601) |

**Endpoints où cet objet est retourné** :
- `/v2/users/me/collection` (users_me_collection_v2.md)

---

### Loan
**Type** : Loan

| Propriété       | Type | Description                    |
|-----------------|------|--------------------------------|
| `id`            | str  | Identifiant unique du prêt     |
| `possession_id` | str  | ID de la possession prêtée     |
| `borrower_id`   | str  | ID de l'emprunteur             |
| `created_at`    | str  | Date du prêt (format ISO 8601) |

**Endpoints où cet objet est retourné** :
- `/v2/users/me/collection` (users_me_collection_v2.md)

---

### ReadDeleted
**Type** : ReadDeleted

| Propriété | Type | Description                        |
|-----------|------|------------------------------------|
| `id`      | str  | Identifiant unique de la lecture   |
| `deleted` | bool | Indique si la suppression a réussi |

**Endpoints où cet objet est retourné** :
- `/v1/reads_multiple` (reads_multiple_delete_v1.md)

---

### ReadEditionDeleted
**Type** : ReadEditionDeleted

| Propriété | Type | Description                                |
|-----------|------|--------------------------------------------|
| `id`      | str  | Identifiant unique de la lecture d'édition |
| `deleted` | bool | Indique si la suppression a réussi         |

**Endpoints où cet objet est retourné** :
- `/v1/reads_multiple` (reads_multiple_delete_v1.md)

---

### PossessionDeleted
**Type** : PossessionDeleted

| Propriété | Type | Description                         |
|-----------|------|-------------------------------------|
| `id`      | str  | Identifiant unique de la possession |
| `deleted` | bool | Indique si la suppression a réussi  |

**Endpoints où cet objet est retourné** :
- `/v1/possessions_multiple` (possessions_multiple_delete_v1.md)

---

### FollowEditionDeleted
**Type** : FollowEditionDeleted

| Propriété | Type | Description                           |
|-----------|------|---------------------------------------|
| `id`      | str  | Identifiant unique du suivi d'édition |
| `deleted` | bool | Indique si la suppression a réussi    |

**Endpoints où cet objet est retourné** :
- `/v1/possessions_multiple` (possessions_multiple_delete_v1.md)

---

### LoanDeleted
**Type** : LoanDeleted

| Propriété | Type | Description                        |
|-----------|------|------------------------------------|
| `id`      | str  | Identifiant unique du prêt         |
| `deleted` | bool | Indique si la suppression a réussi |

**Endpoints où cet objet est retourné** :
- `/v1/possessions_multiple` (possessions_multiple_delete_v1.md)

---

### User
**Type** : User

| Propriété                  | Type               | Description                                               |
|----------------------------|--------------------|-----------------------------------------------------------|
| `id`                       | str                | Identifiant unique de l'utilisateur                       |
| `email`                    | str                | Adresse email principale de l'utilisateur                 |
| `username`                 | str                | Nom d'utilisateur unique                                  |
| `notification_email`       | bool               | Active les notifications par email                        |
| `setting_collection_order` | str                | Ordre d'affichage de la collection (ex: "title")          |
| `created_at`               | str                | Date de création du compte (format ISO 8601)              |
| `confirmed_at`             | str                | Date de confirmation de l'email (format ISO 8601)         |
| `confirmation_sent_at`     | str                | Date d'envoi de l'email de confirmation (format ISO 8601) |
| `unconfirmed_email`        | Optional[str]      | Email non confirmé (peut être null)                       |
| `certify_adult`            | bool               | Certifie que l'utilisateur est adulte                     |
| `possessions_count`        | int                | Nombre de volumes dans la collection de l'utilisateur     |
| `ad_home_banner`           | bool               | Active les bannières publicitaires sur la page d'accueil  |
| `ad_native_home_first`     | bool               | Active les publicités natives en première page            |
| `ad_native_planning_perso` | bool               | Active les publicités natives dans le planning personnel  |
| `is_premium`               | bool               | Indique si l'utilisateur a un abonnement premium actif    |
| `subscriptions`            | List[Subscription] | Liste des abonnements de l'utilisateur                    |

**Endpoints où cet objet est retourné** :
- `/v1/users/me` (users_me_v1.md)
- `/v1/user/{username}` (user_username_v1.md)

---

### Subscription
**Type** : Subscription

| Propriété                | Type          | Description                                           |
|--------------------------|---------------|-------------------------------------------------------|
| `id`                     | str           | Identifiant unique de l'abonnement                    |
| `user_id`                | str           | Identifiant de l'utilisateur                          |
| `app`                    | str           | Application d'abonnement (ex: "android")              |
| `product_id`             | str           | ID du produit (ex: "com.mangacollec.premium.yearly")  |
| `original_purchase_date` | str           | Date d'achat original (format ISO 8601)               |
| `expires_date`           | str           | Date d'expiration de l'abonnement (format ISO 8601)   |
| `auto_renewing`          | bool          | Renouvellement automatique activé                     |
| `created_at`             | str           | Date de création de l'abonnement (format ISO 8601)    |
| `updated_at`             | str           | Date de mise à jour de l'abonnement (format ISO 8601) |
| `cancellation_date`      | Optional[str] | Date d'annulation (peut être null si non annulé)      |

**Endpoints où cet objet est retourné** :
- `/v1/users/me` (users_me_v1.md)
- `/v1/user/{username}` (user_username_v1.md)

---

## Statistiques

- **Total d'objets API réels identifiés** : 31
- **Objets principaux** : 9 (Author, Serie, Edition, Volume, VolumeDetail, Publisher, Type, Kind, Task, Job)
- **Objets de coffret** : 3 (BoxEdition, Box, BoxVolume)
- **Objets commerciaux** : 2 (BDFugueOffer, AmazonOffer)
- **Objets de collection utilisateur** : 15 (User, Subscription, NativeAdVolumeHomeFirst, FollowEdition, Possession, 
BoxFollowEdition, BoxPossession, ReadEdition, Read, Borrower, Loan, ReadDeleted, ReadEditionDeleted, PossessionDeleted,
FollowEditionDeleted, LoanDeleted)
- **Objets de notification/publicité** : 1 (NativeAdVolumeHomeFirst)
- **Objets de gestion utilisateur** : 2 (User, Subscription)

## Notes importantes

- **Seuls les objets JSON réellement retournés par l'API sont listés**
- **Volume** : Version de base utilisée par la plupart des endpoints
- **VolumeDetail** : Version étendue utilisée uniquement par `/v2/volumes/{volume_id}`
- **Les propriétés Optional[str] peuvent être null dans les réponses API**
- **Les types de données correspondent exactement à ce que retourne l'API**
- **Les endpoints listés sont ceux où l'objet est retourné comme entité principale**
- **Les structures internes du SDK (DTOs, entités de domaine) ne sont pas incluses**

<<<INFO

Fichier généré à partir de l'analyse des endpoints du 2025-10-26
Objets identifiés : 31 objets API réels différents
Endpoints analysés : 34 fichiers sur 34 (100% complété)

INFO>>>