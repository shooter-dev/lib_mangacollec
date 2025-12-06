# REPOSITORY DOCUMENTATION

## APIEditionRepository

**Description** : Gère les opérations de récupération et de manipulation des données des éditions dans l'api'

### Méthodes Disponibles
- `get_edition_by_id_v2(edition_id: str)` -> `GetEditionByIdV2Response`
    - **Endpoint** : 
      - methode: `GET` 
      - url: `/v2/editions/{edition_id}`
    - **Authentification** : false
    - **Type retourné** : GetEditionByIdV2Response

- `get_edition_by_id_v1(edition_id: str)` -> `GetEditionByIdV1Response`
    - **Endpoint** : 
        - methode: `GET` 
        - url: `/v1/editions/{edition_id}`
    - **Authentification** : false
    - **Type retourné** : GetEditionByIdV1Response