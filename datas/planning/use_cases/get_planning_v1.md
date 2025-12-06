# USE CASE DOCUMENTATION

## GetPlanningV1

**Description** : Récupère la liste de tous les volumes planifiés pour un mois donné avec leurs 
informations complètes, incluant les relations imbriquées vers les éditions et séries (version V1 de l'API).

**Paramètres d'entrée** :
- `month` (date) : Date au format YYYY-MM-DD (ex: "2022-09-30") pour filtrer les sorties par mois

**Données retournées** :
- list[Volume] : Liste des volumes planifiés avec leurs relations imbriquées
  - Chaque Volume contient :
    - Les informations du volume (id, title, number, release_date, isbn, asin, image_url, etc.)
    - Un objet Edition complet avec :
      - Les informations de l'édition (id, title, volumes_count, commercial_stop, etc.)
      - Un objet Serie complet avec :
        - Les informations de la série (id, title, type_id, adult_content, etc.)

**Structure imbriquée** :
- Les volumes contiennent directement leurs éditions
- Les éditions contiennent directement leurs séries
- Contrairement à V2, les objets sont imbriqués (pas de structure normalisée)
- Plus facile à utiliser pour afficher des informations complètes d'un volume
- Peut générer des redondances si plusieurs volumes appartiennent à la même édition

**Cas d'usage métier** :
- Afficher le calendrier de sortie des volumes pour un mois donné
- Planifier ses achats de mangas à venir
- Visualiser rapidement les informations complètes d'un volume (avec édition et série)
- Suivre les nouvelles sorties d'éditions suivies
- Gérer un budget mensuel de collection
- Créer des alertes pour les sorties à venir
- Comparer les sorties entre différents éditeurs
