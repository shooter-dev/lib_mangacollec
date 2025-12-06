# USE CASE DOCUMENTATION

##GetAuthorByIdV2

**Description** : Récupère les informations détaillées d'un auteur spécifique avec l'ensemble de ses contributions 
(author, tasks, jobs, séries, éditions, volumes) en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** :
- `author_id` (str) : Identifiant UUID de l'auteur

**Données retournées** :
- tuple :
  - Author
  - list[Task]
  - list[Job]
  - list[Serie]
  - list[Edition]
  - list[Volume]

**Cas d'usage métier** :
- Afficher la page de profil complète d'un auteur
- Analyser les contributions d'un auteur spécifique
- Créer une bibliographie détaillée
- Générer des recommandations basées sur les œuvres d'un auteur