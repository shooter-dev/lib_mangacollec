# USE CASE DOCUMENTATION

## GetUserCollectionByUsernameV2

**Description** : Récupère la collection publique complète d'un utilisateur spécifique via son nom d'utilisateur.
Retourne toutes les entités liées à sa collection : éditions, séries, volumes, coffrets, possessions, suivis et lectures.

**Paramètres d'entrée** :
- `username` (str) : Nom d'utilisateur de l'utilisateur dont on veut voir la collection

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

**Cas d'usage métier** :
- Visualiser la collection publique d'un autre utilisateur
- Comparer sa collection avec celle d'autres membres de la communauté
- Découvrir les mangas possédés ou suivis par un utilisateur spécifique
- Afficher les statistiques de collection d'un profil public
- Explorer les goûts et préférences d'un membre de la communauté

**Notes** :
- N'affiche que les données publiques de la collection
- N'inclut pas les informations privées comme les prêts (borrowers/loans)
- Ne nécessite pas d'authentification
