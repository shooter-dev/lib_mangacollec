# REPOSITORY DOCUMENTATION

## APIOfferRepository

**Description** : Gère les opérations de récupération des offres commerciales (Amazon et BDFugue) pour les volumes dans l'API.

### Méthodes Disponibles
- `get_amazon_offer_v1(volume_asin: str)` -> `GetAmazonOfferV1Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v1/amazon_offer/{volume_asin}`
    - **Authentification** : false
    - **Type retourné** : GetAmazonOfferV1Response

- `get_bdfugue_offer_v1(volume_isbn: str)` -> `GetBDFugueOfferV1Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v1/bdfugue_offer/{volume_isbn}`
    - **Authentification** : false
    - **Type retourné** : GetBDFugueOfferV1Response
