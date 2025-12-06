# USE CASE DOCUMENTATION

## GetEditionByIdV2

**Description** : Récupère les informations complètes d'une édition spécifique avec toutes les entités associées 
(edition, publisher, série(s), types(serie), volumes) en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** :
- `edition_id` (str) : Identifiant UUID de l'édition

**Données retournées** :
- tuple :
  - list[Edition]
  - Publisher
  - list[Serie]
  - list[TypeSerie]
  - list[Volume]

**Cas d'usage métier** :
- Afficher la fiche détaillée d'une édition
- Visualiser la progression de collection d'une édition
- Comparer différentes éditions d'une même série
- Gérer les éditions dans une collection personnelle