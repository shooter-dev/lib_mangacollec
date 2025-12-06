# USE CASE DOCUMENTATION

## GetVolumesNewsV2

**Description** : Récupère la liste des derniers volumes de manga publiés ou annoncés avec toutes leurs entités 
associées en structure normalisée (version V2 de l'API). 
Cette méthode permet de consulter les nouveautés et sorties à venir.

**Paramètres d'entrée** : Aucun

**Données retournées** :
- tuple :
  - list[Volume] : Volumes récents et à venir
  - list[Edition] : Éditions associées aux volumes
  - list[Serie] : Séries associées aux volumes
  - list[Type] : Types de séries
  - list[Box] : Coffrets inclus dans les nouveautés
  - list[BoxEdition] : Éditions de coffrets
  - list[BoxVolume] : Associations volumes-coffrets
  - NativeAdVolumeHomeFirst : Informations sur les publicités natives pour les volumes

**Cas d'usage métier** :
- Afficher une page d'accueil avec les dernières sorties manga
- Créer un fil d'actualités des nouveaux volumes
- Consulter les volumes à paraître et planifier ses achats
- Identifier les tendances du marché manga
- Mettre en avant les volumes sponsorisés via les publicités natives
- Permettre aux utilisateurs de découvrir de nouvelles séries
- Afficher un calendrier de sorties avec les dates de publication
- Filtrer les nouveautés par éditeur, série ou type

**Notes** :
- Les volumes sont triés par date de sortie décroissante (du plus récent au plus ancien)
- Retourne à la fois les volumes déjà publiés et les volumes annoncés
- La réponse peut être volumineuse car elle contient de nombreuses entités associées
- Les coffrets et leurs associations sont inclus lorsqu'ils font partie des nouveautés
- Les publicités natives (native_ad_volume_home_first) mettent en avant certains volumes spécifiques
