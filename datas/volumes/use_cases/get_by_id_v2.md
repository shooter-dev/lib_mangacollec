# USE CASE DOCUMENTATION

## GetVolumeByIdV2

**Description** : Récupère les informations détaillées d'un volume spécifique avec toutes les entités associées 
(volume, édition, éditeur, série, type, coffrets et associations) en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** :
- `volume_id` (str) : Identifiant UUID du volume

**Données retournées** :
- tuple :
  - list[Volume] : Informations du volume (toujours un seul élément)
  - list[Edition] : Éditions associées
  - list[Publisher] : Éditeurs associés
  - list[Serie] : Séries associées
  - list[Type] : Types de séries
  - list[BoxVolume] : Associations volumes-coffrets
  - list[Box] : Coffrets contenant le volume
  - list[BoxEdition] : Éditions des coffrets

**Cas d'usage métier** :
- Afficher la fiche détaillée d'un volume spécifique
- Consulter les informations complètes (titre, numéro, date de sortie, ISBN, ASIN)
- Identifier l'édition et la série parentes du volume
- Visualiser les coffrets contenant ce volume
- Vérifier la disponibilité commerciale d'un volume (not_sold)
- Accéder aux métadonnées (nombre de pages, contenu, image de couverture)
- Analyser la popularité d'un volume via le nombre de possesseurs
