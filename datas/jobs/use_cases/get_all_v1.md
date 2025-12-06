# USE CASE DOCUMENTATION

## GetAllJobsV1

**Description** : Récupère la liste complète des jobs (métiers/rôles) disponibles dans la base de données. 
Les jobs représentent les différents rôles qu'un auteur peut avoir dans la création 
d'un manga (auteur, dessinateur, scénariste, etc.).

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list[Job]
    - Job
        - `id` (str) : Identifiant UUID unique du job
        - `title` (str) : Titre/nom du job (ex: "Auteur", "Dessin", "Scénario")

**Cas d'usage métier** :
- Afficher la liste des rôles possibles lors de l'ajout d'un auteur à une série
- Créer une liste de sélection pour filtrer les auteurs par rôle
- Afficher les contributeurs d'un manga avec leurs rôles respectifs
- Générer des statistiques sur les types de contributions
