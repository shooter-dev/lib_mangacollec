---
Resource: offers_bdfugue_detail
Version: V1
Endpoint: https://api.mangacollec.com/v1/bdfugue_offer/{volume_isbn}
Method: GET
Response_brut: datas/_endpoints/offers/bdfugue_offer_v1.json
Description: Get BDFugue offer details for a volume
Authentication: false
---

# Endpoint GET /v1/bdfugue_offer/{volume_isbn}

## Description
Retourne les informations commerciales BDFugue pour un volume spécifique via son ISBN.

## Structure de la réponse

### Objet BDFugue implement Offer

| Champ             | Type          | Description                        |
|-------------------|---------------|------------------------------------|
| `id`              | str           | International Standard Book Number |
| `formatted_price` | Optional[str] | Prix du volume sur BDFugue         |
| `availability`    | Optional[str] | Disponibilité du produit           |
| `merchant`        | str           | Précise qui est le vendeur.        |
| `store_link`      | str           | URL de la page produit BDFugue     |

## Exemple de réponse

```json
{
    "id": "9782380712957",
    "formatted_price": "7,30 €",
    "availability": "En stock !",
    "merchant": "Expédié et vendu par BDfugue.",
    "store_link": "https://www.bdfugue.com/spy-x-family-tome-8?ref=358"
}
```

## Notes

- Nécessite un ISBN valide
- Les informations de prix peuvent varier selon la disponibilité
- Les champs marqués comme `Optional[]` peuvent être null