# USE CASE DOCUMENTATION

## GetPlanningV2

**Description** : Récupère la liste de tous les volumes et coffrets planifiés pour un mois donné avec 
leurs informations de base et les entités associées en structure normalisée (version V2 de l'API).

**Paramètres d'entrée** :
- `month` (date) : Date au format YYYY-MM-DD (ex: "2022-09-30") pour filtrer les sorties par mois

**Données retournées** :
- tuple :
  - list[Volume] : Liste des volumes planifiés
  - list[Edition] : Liste des éditions associées
  - list[Serie] : Liste des séries associées
  - list[TypeSerie] : Liste des types de séries
  - list[Box] : Liste des coffrets planifiés
  - list[BoxEdition] : Liste des éditions de coffrets
  - list[BoxVolume] : Liste des volumes contenus dans les coffrets

**Structure normalisée** :
- Contrairement à V1, les objets ne sont pas imbriqués
- Les relations entre entités se font via les IDs
- Chaque entité est retournée dans un tableau séparé
- Pour reconstruire les relations, utiliser les IDs pour faire correspondre les entités entre les tableaux

**Cas d'usage métier** :
- Afficher le calendrier de sortie des volumes pour un mois donné
- Planifier ses achats de mangas à venir
- Suivre les nouvelles sorties d'éditions suivies
- Gérer un budget mensuel de collection
- Créer des alertes pour les sorties à venir
- Comparer les sorties entre différents éditeurs
- Visualiser les coffrets et éditions spéciales à venir
