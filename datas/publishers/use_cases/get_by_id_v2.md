# USE CASE DOCUMENTATION

## GetPublisherByIdV2

**Description** : Récupère les informations complètes d'un éditeur spécifique avec toutes les entités associées 
(publisher, éditions, box_editions, séries, types(serie), volumes, boxes) en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** :
- `publisher_id` (str) : Identifiant UUID de l'éditeur

**Données retournées** :
- tuple :
    - Publisher
    - list[Edition] : Informations détaillées des éditions publiées par cet éditeur
    - list[BoxEdition] : Informations sur les éditions de coffrets
    - list[Serie] : Informations sur les séries publiées
    - list[TypeSerie] : Types de séries
    - list[Volume] : Informations détaillées des volumes
    - list[Box] : Informations sur les coffrets

**Cas d'usage métier** :
- Afficher la fiche détaillée d'un éditeur
- Visualiser le catalogue complet d'un éditeur
- Analyser la production d'un éditeur (nombre d'éditions, séries, volumes)
- Comparer différents éditeurs
- Gérer un catalogue de mangas par éditeur
