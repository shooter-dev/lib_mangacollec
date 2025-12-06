# USE CASE DOCUMENTATION

## GetBDFugueOfferV1

**Description** : Récupère les informations commerciales BDFugue pour un volume spécifique via son 
ISBN (International Standard Book Number). 
Permet d'obtenir le prix, la disponibilité et le lien vers la page produit BDFugue.

**Paramètres d'entrée** :
- `volume_isbn` (str) : International Standard Book Number du volume

**Données retournées** :
- BDFugueOffer
    - `id` (str) : International Standard Book Number (ISBN)
    - `formatted_price` (Optional[str]) : Prix formaté du volume sur BDFugue (ex: "7,30 €")
    - `availability` (Optional[str]) : Statut de disponibilité du produit (ex: "En stock !")
    - `merchant` (str) : Information sur le vendeur (ex: "Expédié et vendu par BDfugue.")
    - `store_link` (str) : URL de la page produit BDFugue avec référence affiliée

**Cas d'usage métier** :
- Afficher le prix BDFugue d'un volume dans la fiche produit
- Comparer les prix entre différents marchands
- Rediriger l'utilisateur vers l'achat sur BDFugue
- Vérifier la disponibilité d'un volume chez BDFugue
- Générer des liens affiliés pour les achats
- Privilégier un marchand spécialisé en BD/Manga
