# USE CASE DOCUMENTATION

## AddPossessionsMultipleV1

**Description** : Permet d'ajouter un ou plusieurs volumes à la collection personnelle de l'utilisateur en une 
seule requête. 
Lors de l'ajout d'une possession, le système suit automatiquement l'édition associée si ce n'est pas déjà fait.

**Conditions préalables** :
- L'utilisateur doit être authentifié.
- Les volumes doivent exister dans la base de données.

**Paramètres d'entrée** :
- `volume_ids` (list[Volume]) : Liste des volumes à ajouter à la collection

**Données retournées** :
- tuple :
  - `possessions` (list[Possession]) : Liste des possessions créées
  - `follow_editions` (list[FollowEdition]) : Liste des suivis d'éditions créés automatiquement

**Cas d'usage métier** :
- Ajouter un ou plusieurs volumes à sa collection personnelle après un achat
- Suivre automatiquement les éditions associées aux volumes ajoutés
- Gérer l'état de possession d'une collection de mangas
- Recevoir des notifications pour les nouvelles sorties des éditions suivies
- Synchroniser la collection suite à un inventaire physique

**Notes** :
- Si un volume est déjà possédé, aucune erreur n'est retournée
- Si l'édition est déjà suivie, aucun nouveau suivi n'est créé
- L'ordre des possessions créées correspond à l'ordre des volumes dans la requête
- Maximum 100 volumes par requête pour éviter les timeouts
