# USE CASE DOCUMENTATION

## GetAmazonOfferV1

**Description** : Récupère les informations commerciales Amazon pour un volume spécifique via son 
ASIN (Amazon Standard Identification Number). 
Permet d'obtenir le prix, la disponibilité et le lien vers la page produit Amazon.

**Paramètres d'entrée** :
- `volume_asin` (str) : Amazon Standard Identification Number du volume

**Données retournées** :
- AmazonOffer
    - `asin` (str) : Amazon Standard Identification Number
    - `formatted_price` (Optional[str]) : Prix formaté du volume sur Amazon (ex: "7,30 €")
    - `availability` (Optional[str]) : Statut de disponibilité du produit (ex: "En stock")
    - `merchant` (str) : Information sur le vendeur (ex: "Expédié et vendu par Amazon.")
    - `store_link` (str) : URL de la page produit Amazon avec tag affilié

**Cas d'usage métier** :
- Afficher le prix Amazon d'un volume dans la fiche produit
- Comparer les prix entre différents marchands
- Rediriger l'utilisateur vers l'achat sur Amazon
- Vérifier la disponibilité d'un volume chez Amazon
- Générer des liens affiliés pour les achats
