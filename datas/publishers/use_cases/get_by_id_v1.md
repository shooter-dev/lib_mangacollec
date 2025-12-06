# USE CASE DOCUMENTATION

## GetPublisherByIdV1

**Description** : Récupère les informations détaillées d'un éditeur spécifique avec toutes ses éditions et séries associées (version V1 de l'API).

**Paramètres d'entrée** :
- `publisher_id` (str) : Identifiant UUID de l'éditeur

**Données retournées** :
- Publisher
    - `id` (str) : Identifiant unique de l'éditeur
    - `title` (str) : Nom de l'éditeur
    - `editions_count` (int) : Nombre d'éditions publiées

**Cas d'usage métier** :
- Afficher les informations de base d'un éditeur
- Consulter le nombre d'éditions d'un éditeur
- Naviguer vers les détails d'un éditeur sélectionné
- Afficher le nom et l'identifiant d'un éditeur

**Note** : Pour obtenir les informations complètes (éditions, séries, volumes, etc.), utiliser la version V2 de l'API qui retourne une structure normalisée avec toutes les entités associées.
