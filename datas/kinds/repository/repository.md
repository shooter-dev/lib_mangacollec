# REPOSITORY DOCUMENTATION

## APIKindRepository

**Description** : Gère les opérations de récupération et de manipulation des données des kinds (genres/catégories) dans l'API.

### Méthodes Disponibles

- `get_all_kinds_v2()` -> `GetAllKindsV2Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v2/kinds`
    - **Authentification** : false
    - **Type retourné** : GetAllKindsV2Response

- `get_all_kinds_v1()` -> `GetAllKindsV1Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v1/kinds`
    - **Authentification** : false
    - **Type retourné** : GetAllKindsV1Response
