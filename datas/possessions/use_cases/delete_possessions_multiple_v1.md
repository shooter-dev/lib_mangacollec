# USE CASE DOCUMENTATION

## DeletePossessionsMultipleV1

**Description** : Permet de supprimer un ou plusieurs enregistrements de possession de la collection personnelle 
de l'utilisateur en une seule requête. Lors de la suppression d'une possession, le système supprime automatiquement 
le suivi de l'édition associée si c'était la seule possession de cette édition. 
Les prêts associés aux possessions sont également supprimés automatiquement.

**Conditions préalables** :
- L'utilisateur doit être authentifié.
- Les possessions doivent appartenir à l'utilisateur authentifié.

**Paramètres d'entrée** :
- `possession_ids` (list[Possession]) : Liste des possessions à supprimer

**Données retournées** :
- tuple :
  - `possessions` (list[PossessionDeleted]) : Liste des possessions supprimées
  - `follow_editions` (list[FollowEditionDeleted]) : Liste des suivis d'éditions supprimés automatiquement
  - `loans` (list[LoanDeleted]) : Liste des prêts supprimés automatiquement

**Cas d'usage métier** :
- Supprimer des volumes vendus ou donnés de sa collection
- Corriger une erreur d'ajout de possession
- Nettoyer sa collection en retirant plusieurs volumes à la fois
- Gérer la fin d'un prêt en supprimant la possession et le prêt associé
- Arrêter automatiquement le suivi d'une édition si c'était la dernière possession
- Synchroniser la collection suite à une vérification d'inventaire

**Notes** :
- Si une possession n'existe pas, aucune erreur n'est retournée
- Le suivi de l'édition n'est supprimé que si c'était la dernière possession de cette édition
- Si d'autres possessions existent pour la même édition, l'édition reste suivie
- Les prêts associés sont automatiquement supprimés sans confirmation supplémentaire
- L'ordre des réponses correspond à l'ordre des IDs dans la requête
- Le tableau `loans` peut être vide si aucun prêt n'était associé aux possessions supprimées
- Maximum 100 possessions par requête pour éviter les timeouts
