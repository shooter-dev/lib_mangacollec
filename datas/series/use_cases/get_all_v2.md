# USE CASE DOCUMENTATION

## GetAllSeriesV2

**Description** : Récupère la liste complète des séries de manga disponibles avec leurs informations de base et leurs types en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- tuple :
  - list[Serie]
  - list[TypeSerie]

**Cas d'usage métier** :
- Afficher un catalogue complet de séries dans l'application
- Créer une liste de sélection pour filtrer par série
- Générer des statistiques sur les séries les plus populaires

**Notes** :
- La version V2 de l'API utilise une structure de données améliorée pour les séries
- Chaque série inclut un identifiant de type pour une meilleure classification
- La liste des types de séries permet de comprendre les catégories associées à chaque série