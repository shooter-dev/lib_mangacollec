# USE CASE DOCUMENTATION

## GetMeCollectionV2

**Description** : Récupère la collection personnelle complète de l'utilisateur authentifié avec toutes les entités associées, incluant les informations privées de prêts (version V2 de l'API).

**Conditions préalables** :
- L'utilisateur doit être authentifié

**Paramètres d'entrée** : Aucun (utilise le token d'authentification)

**Données retournées** :
- UserCollection
    - `editions` (List[Edition]) : Liste des éditions suivies ou possédées
    - `series` (List[Serie]) : Liste des séries associées aux éditions
    - `types` (List[Type]) : Liste des types de média (manga, manhwa, etc.)
    - `kinds` (List[Kind]) : Liste des genres (shōnen, seinen, etc.)
    - `volumes` (List[Volume]) : Liste des volumes individuels
    - `box_editions` (List[BoxEdition]) : Liste des éditions de coffrets
    - `boxes` (List[Box]) : Liste des coffrets individuels
    - `box_volumes` (List[BoxVolume]) : Associations entre coffrets et volumes
    - `follow_editions` (List[FollowEdition]) : Éditions suivies par l'utilisateur
    - `possessions` (List[Possession]) : Volumes possédés par l'utilisateur
    - `box_follow_editions` (List[BoxFollowEdition]) : Coffrets suivis par l'utilisateur
    - `box_possessions` (List[BoxPossession]) : Coffrets possédés par l'utilisateur
    - `read_editions` (List[ReadEdition]) : Éditions en cours de lecture
    - `reads` (List[Read]) : Volumes lus par l'utilisateur
    - `borrowers` (List[Borrower]) : Liste des emprunteurs enregistrés
    - `loans` (List[Loan]) : Prêts en cours ou historique

**Cas d'usage métier** :
- Afficher la collection complète de l'utilisateur dans son espace personnel
- Gérer ses possessions, suivis et lectures
- Visualiser ses statistiques de collection personnelles
- Gérer les prêts de volumes à des amis ou proches
- Synchroniser la collection avec une application mobile
- Exporter ou sauvegarder sa collection
- Analyser ses habitudes de lecture et d'achat
- Suivre l'évolution de sa collection dans le temps

**Différence avec GetUserCollectionByUsernameV2** :
- Inclut les données privées (`borrowers` et `loans`)
- Nécessite une authentification
- Accède uniquement à la collection de l'utilisateur connecté
- Retourne des informations complètes et non filtrées

**Notes** :
- Requiert un token OAuth2 valide
- Structure normalisée V2 avec tableaux séparés pour chaque type d'entité
- Les champs Optional peuvent être null
- Format de dates : ISO 8601
- IDs au format UUID
