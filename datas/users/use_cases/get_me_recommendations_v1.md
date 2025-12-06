# USE CASE DOCUMENTATION

## GetMeRecommendationsV1

**Description** : Récupère des recommandations personnalisées de mangas pour l'utilisateur authentifié, 
basées sur sa collection, ses préférences et ses habitudes de lecture. 
Chaque recommandation est un volume spécifique avec toutes ses informations détaillées.

**Conditions préalables** :
- L'utilisateur doit être authentifié
- L'utilisateur doit avoir une collection suffisamment fournie pour générer des recommandations pertinentes

**Paramètres d'entrée** : Aucun (utilise le token d'authentification et analyse automatiquement la collection)

**Données retournées** :
- List[VolumeRecommendation]
    - Chaque VolumeRecommendation contient :
        - **Volume** :
        - **Edition** (imbriquée dans volume) :
        - **Serie** (imbriquée dans edition) :

**Cas d'usage métier** :
- Découvrir de nouveaux mangas correspondant à ses goûts
- Recevoir des suggestions personnalisées basées sur sa collection actuelle
- Trouver le prochain tome à acheter dans une série suivie
- Explorer des séries similaires à celles déjà appréciées
- Remplir automatiquement une liste de souhaits
- Planifier ses prochains achats de mangas
- Découvrir des nouveautés dans ses genres préférés
- Enrichir sa collection avec des recommandations pertinentes

**Algorithme de recommandation (hypothèses)** :
- Analyse des genres (kinds) les plus présents dans la collection
- Identification des auteurs favoris via les tasks
- Détection des séries en cours dans la collection
- Suggestions de tomes manquants dans les éditions suivies
- Nouveautés dans les mêmes catégories
- Popularité (possessions_count) comme indicateur de qualité

**Notes** :
- Requiert un token OAuth2 valide
- Retourne des volumes spécifiques, pas seulement des séries
- Structure imbriquée pour fournir toutes les informations nécessaires
- `possessions_count` indique la popularité du volume
- `not_sold` signale les volumes épuisés
- Les recommandations sont dynamiques et évoluent avec la collection
- Format de données : API V1 (structure imbriquée, pas normalisée comme V2)
