# USE CASE DOCUMENTATION

## GetSerieByIdV1

**Description** : Récupère les informations détaillées d'une série spécifique avec toutes ses éditions et volumes associés (version V1 de l'API).

**Paramètres d'entrée** :
- `serie_id` (str) : Identifiant UUID de la série

**Données retournées** :
- Serie (objet avec éditions imbriquées)

**Structure des données :**

### Serie
- `id` (str) : Identifiant unique de la série
- `title` (str) : Titre de la série
- `type_id` (str) : Identifiant du type de série
- `adult_content` (bool) : Contenu pour adultes
- `editions_count` (int) : Nombre d'éditions disponibles
- `tasks_count` (int) : Nombre de tâches associées à la série
- `editions` (list[Edition]) : Liste des éditions de la série

### Edition (imbriquée)
- `id` (str) : Identifiant unique de l'édition
- `title` (str | None) : Titre de l'édition (peut être null)
- `series_id` (str) : Identifiant de la série parente
- `publisher_id` (str) : Identifiant de l'éditeur
- `parent_edition_id` (str | None) : Identifiant de l'édition parente
- `volumes_count` (int) : Nombre de volumes dans l'édition
- `last_volume_number` (int | None) : Numéro du dernier volume publié
- `commercial_stop` (bool) : Arrêt commercial
- `not_finished` (bool) : Série non terminée
- `follow_editions_count` (int) : Nombre de personnes qui suivent cette édition
- `publisher` (Publisher) : Objet Publisher détaillé
- `volumes` (list[Volume]) : Liste des volumes de l'édition

### Volume (imbriqué)
- `id` (str) : Identifiant unique du volume
- `title` (str | None) : Titre du volume (peut être null)
- `number` (int) : Numéro du volume
- `release_date` (str | None) : Date de publication (format YYYY-MM-DD)
- `image_url` (str | None) : URL de l'image de couverture
- `isbn` (str | None) : ISBN du volume
- `asin` (str | None) : ASIN Amazon du volume
- `edition_id` (str) : Identifiant de l'édition parente
- `possessions_count` (int | None) : Nombre de possesseurs du volume
- `not_sold` (bool) : Plus en vente

**Cas d'usage métier** :
- Afficher la fiche complète d'une série avec tous ses détails
- Visualiser l'arborescence complète : série → éditions → volumes
- Gérer sa collection personnelle de volumes
- Suivre la progression de publication d'une série
- Comparer les différentes éditions disponibles
- Vérifier la disponibilité des volumes
- Afficher les informations commerciales (ISBN, ASIN, statut de vente)

**Notes** :
- La réponse peut être volumineuse car elle contient toute la hiérarchie des données
- Les éditions spéciales ont un `parent_edition_id` pointant vers l'édition standard
- Les volumes peuvent avoir des informations commerciales comme `not_sold` et `possessions_count`
- Structure imbriquée (différente de V2 qui utilise une structure normalisée)
