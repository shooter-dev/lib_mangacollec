# USE CASE DOCUMENTATION

## GetListAuthorsV2

**Description** : Récupère la liste complète des auteurs disponibles dans lapi' avec uniquement
- id
- full_name

**Paramètres d'entrée** : Aucun

**Données retournées** :
- list
    - AuthorListItem
        - id: str
        - full_name: str

**Cas d'usage métier** :
- Afficher un annuaire complet d'auteurs pour sélection dans l'application
- Afficher les auteurs dans une liste déroulante