# USE CASE DOCUMENTATION

## GetListPublishersV2

**Description** : Récupère la liste complète des éditeurs disponibles dans l'api avec uniquement :
- id
- title

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list
    - PublisherListItem
        - id: str
        - title: str

**Cas d'usage métier** :
- Afficher un annuaire complet d'éditeurs pour sélection dans l'application
- Afficher les éditeurs dans une liste déroulante
- Créer un menu de navigation par éditeur
