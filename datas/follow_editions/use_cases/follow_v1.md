# USE CASE DOCUMENTATION

## FollowEditionV1

**Description** : Permet à un utilisateur de suivre ou de ne plus suivre une édition spécifique dans sa collection personnelle.

**Conditions préalables** :
- L'utilisateur doit être authentifié.

**Paramètres d'entrée** :
- `edition_id` (str) : Identifiant unique de l'édition à suivre
- `following` (bool) : État de suivi (true = suivre, false = ne plus suivre)

**Données retournées** :
- FollowEdition
    - `id` (str) : Identifiant unique du suivi
    - `user_id` (str) : Identifiant unique de l'utilisateur
    - `edition_id` (str) : Identifiant unique de l'édition
    - `following` (bool) : État actuel du suivi
    - `created_at` (datetime) : Date de création du suivi (format ISO 8601)
    - `updated_at` (datetime) : Date de dernière mise à jour (format ISO 8601)

**Cas d'usage métier** :
- Ajouter une édition à sa liste de suivi
- Recevoir des notifications pour les nouvelles sorties
- Organiser sa collection personnelle
- Désactiver le suivi d'une édition