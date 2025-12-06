# USE CASE DOCUMENTATION

## GetAllTypesV1

**Description** : Récupère la liste complète des types de séries disponibles dans la base de données. 
Les types représentent les catégories de publications (Manga, Manhwa, Manhua, BD, Comics, etc.) 
ainsi que les formats spéciaux (Artbook, Guidebook, Roman, etc.).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list
    - TypeSerie

**Cas d'usage métier** :
- Afficher la liste des types de séries disponibles dans un filtre de recherche
- Créer une liste de sélection pour catégoriser une nouvelle série
- Distinguer les types principaux (Manga, BD, Comics) des types secondaires (Artbook, Roman)
- Filtrer les séries par type dans l'application
- Générer des statistiques sur la répartition des publications par type
