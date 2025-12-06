# USE CASE DOCUMENTATION

## GetAllPublishersV1

**Description** : Récupère la liste complète des éditeurs disponibles avec leurs informations de base (version V1 de l'API).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list
    - Publisher
        - `id` (str) : Identifiant unique de l'éditeur
        - `title` (str) : Nom de l'éditeur

**Cas d'usage métier** :
- Afficher une liste simple d'éditeurs
- Créer un menu de sélection d'éditeur
- Rechercher un éditeur par son nom
- Lister rapidement tous les éditeurs disponibles

**Note** : Pour obtenir plus d'informations détaillées sur les éditeurs (nombre d'éditions, statut fermé, etc.), utiliser la version V2 de l'API.
