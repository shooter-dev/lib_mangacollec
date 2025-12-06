# USE CASE DOCUMENTATION

## DeleteReadsMultipleV1

**Description** : Permet de supprimer un ou plusieurs enregistrements de lecture de la collection personnelle de 
l'utilisateur en une seule requête. Lors de la suppression d'une lecture, le système supprime automatiquement 
l'édition associée en cours de lecture si c'était la dernière lecture de cette édition.

**Conditions préalables** :
- L'utilisateur doit être authentifié.

**Paramètres d'entrée** :
- `read_ids` (list[Read]) : Liste des reads à supprimer

**Données retournées** :
- tuple :
  - list[ReadDeleted] : Liste des lectures supprimées
  - list[ReadEditionDeleted] : Liste des lectures d'éditions supprimées automatiquement

**Cas d'usage métier** :
- Corriger des erreurs de marquage de lecture
- Supprimer des lectures en masse après révision de sa collection
- Nettoyer l'historique de lecture
- Retirer le suivi automatique des éditions terminées
- Réinitialiser la progression de lecture d'une édition

**Notes** :
- Si une lecture n'existe pas, aucune erreur n'est retournée
- Si d'autres lectures existent pour la même édition, l'édition reste marquée comme étant en cours de lecture
- Le système supprime automatiquement l'édition associée en cours de lecture uniquement si c'était la dernière lecture de cette édition
- L'ordre des réponses correspond à l'ordre des IDs dans la requête
