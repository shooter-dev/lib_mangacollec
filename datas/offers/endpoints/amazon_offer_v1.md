---
Resource: offer_amazone_detail
Version: V1
Endpoint: https://api.mangacollec.com/v1/amazon_offer/{volume_asin}
Method: GET
Response_brut: datas/_endpoints/offers/amazon_offer_v1.json
Description: Get Amazon offer details for a volume
Authentication: false
---

# Endpoint GET /v1/amazon_offer/{volume_asin}

## Description
Retourne les informations commerciales Amazon pour un volume spécifique via son `ASIN`.

## Structure de la réponse

### Objet Amazon implement Offer

| Champ             | Type          | Description                           |
|-------------------|---------------|---------------------------------------|
| `asin`            | str           | Amazon Standard Identification Number |
| `formatted_price` | Optional[str] | Prix du volume sur Amazon             |
| `availability`    | Optional[str] | Disponibilité du produit              |
| `merchant`        | str           | Précise qui est le vendeur.           |
| `store_link`      | str           | URL de la page produit Amazon         |

## Exemple de réponse

```json
{
    "asin": "2380712956",
    "formatted_price": "7,30 €",
    "availability": "En stock",
    "merchant": "Expédié et vendu par Amazon.",
    "store_link": "https://www.amazon.fr/dp/2380712956?tag=manga-web-21&linkCode=ogi&th=1&psc=1"
}
```

## Notes

- Nécessite un ASIN valide
- Les informations de prix peuvent varier selon la disponibilité
- Les champs marqués comme `Optional[]` peuvent être null
