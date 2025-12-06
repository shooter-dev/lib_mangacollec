# USE CASE DOCUMENTATION

## GetAllSeriesV1

**Description** : Récupère la liste complète des séries de manga disponibles avec leurs informations de base (version V1 de l'API).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list[Serie]

**Structure des données :**

### Serie
- `id` (str) : Identifiant unique de la série
- `title` (str) : Titre de la série
- `type_id` (str | None) : Identifiant du type de série (peut être null)
- `adult_content` (bool) : Contenu pour adultes
- `editions_count` (int) : Nombre d'éditions disponibles
- `tasks_count` (int) : Nombre de tâches associées

**Cas d'usage métier** :
- Afficher un catalogue complet de séries dans l'application
- Créer une liste de sélection pour filtrer par série
- Générer des statistiques sur les séries disponibles
- Filtrer les séries avec contenu pour adultes

**Notes** :
- Retourne uniquement les informations de base des séries
- Pour obtenir les détails complets (éditions, volumes), utiliser `GetSerieByIdV1`
- La réponse peut être volumineuse car elle contient toutes les séries
- Les séries sont retournées sans ordre particulier
