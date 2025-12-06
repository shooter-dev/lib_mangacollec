# USE CASE DOCUMENTATION

## GetAllKindsV2

**Description** : Récupère la liste complète des kinds (genres/catégories) disponibles avec leurs 
informations essentielles et les IDs des séries associées (version V2 de l'API).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list
    - Kind
        - `id` (str) : Identifiant UUID du kind
        - `title` (str) : Titre du kind (ex: "Action", "Aventure", "Romance")
        - `series_ids` (List[str]) : Liste des identifiants UUID des séries associées à ce kind

**Cas d'usage métier** :
- Afficher un catalogue complet des genres de mangas disponibles
- Créer un système de filtrage par genre dans l'application
- Générer des statistiques sur les genres les plus populaires
- Permettre la navigation par catégorie de manga
- Construire un système de recommandations basé sur les genres
- Afficher le nombre de séries par genre

**Notes** :
- La réponse peut être volumineuse car elle contient tous les kinds et leurs séries associées
- La structure V2 utilise un format normalisé avec un tableau "kinds"
- Les kinds sont retournés sans ordre particulier
- Chaque kind peut être associé à plusieurs séries (relation many-to-many)
