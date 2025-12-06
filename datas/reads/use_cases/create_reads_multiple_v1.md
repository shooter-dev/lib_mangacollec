# USE CASE DOCUMENTATION

## CreateReadsMultipleV1

**Description** : Permet de marquer un ou plusieurs volumes comme lus en une seule requête. Lors du marquage d'une lecture, le système suit automatiquement l'édition associée comme étant en cours de lecture si ce n'est pas déjà fait.

**Conditions préalables** :
- L'utilisateur doit être authentifié.

**Paramètres d'entrée** :
- `volumes` (list[Volume]) : Liste des volumes à marquer comme lus

**Données retournées** :
- tuple :
  - list[Read] : Liste des lectures créées
  - list[ReadEdition] : Liste des lectures d'éditions créées automatiquement

**Cas d'usage métier** :
- Marquer plusieurs volumes comme lus après une session de lecture
- Synchroniser la progression de lecture d'une édition
- Suivre automatiquement les éditions en cours de lecture
- Importer un historique de lecture en masse
- Mettre à jour rapidement sa collection après l'achat de plusieurs volumes

**Notes** :
- Si un volume est déjà marqué comme lu, aucune erreur n'est retournée
- Si l'édition est déjà suivie en lecture, aucun nouveau suivi n'est créé
- L'ordre des lectures créées correspond à l'ordre des volumes dans la requête
- Maximum 100 volumes par requête
