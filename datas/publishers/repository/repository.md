# REPOSITORY DOCUMENTATION

## APIPublisherRepository

**Description** : Gère les opérations de récupération et de manipulation des données des éditeurs dans l'api'

### Méthodes Disponibles
- `get_all_publishers_v2()` -> `GetAllPublishersV2Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v2/publishers`
    - **Authentification** : false
    - **Type retourné** : GetAllPublishersV2Response

- `get_publisher_by_id_v2(publisher_id: str)` -> `GetPublisherByIdV2Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v2/publishers/{publisher_id}`
    - **Authentification** : false
    - **Type retourné** : GetPublisherByIdV2Response

- `get_all_publishers_v1()` -> `GetAllPublishersV1Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v1/publishers`
    - **Authentification** : false
    - **Type retourné** : GetAllPublishersV1Response

- `get_publisher_by_id_v1(publisher_id: str)` -> `GetPublisherByIdV1Response`
    - **Endpoint** :
        - methode: `GET`
        - url: `/v1/publishers/{publisher_id}`
    - **Authentification** : false
    - **Type retourné** : GetPublisherByIdV1Response
