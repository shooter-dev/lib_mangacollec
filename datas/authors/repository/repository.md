# REPOSITORY DOCUMENTATION

## APIAuthorRepository
**Description** : Gère les opérations de récupération et de manipulation des données des auteurs dans l'api'

### Méthodes Disponibles
- `get_all_authors_v2()` -> `GetAllAuthorsV2Response`
    - **Endpoint** : 
        - methode: `GET` 
        - url: `/v2/authors`
    - **Authentification** : false
    - **Type retourné** : GetAllAuthorsV2Response

- `get_author_by_id_v2(author_id: str)` -> `GetAuthorByIdV2Response`
    - **Endpoint** : 
        - methode: `GET` 
        - url: `/v2/authors/{author_id}`
    - **Authentification** : false
    - **Type retourné** : GetAuthorByIdV2Response

- `get_all_authors_v1()` -> `GetAllAuthorV1Response`
    - **Endpoint** : 
        - methode: `GET` 
        - url: `/v1/authors`
    - **Authentification** : false
    - **Type retourné** : GetAllAuthorV1Response

- `get_author_by_id_v1(author_id: str)` -> `GetAuthorByIdV1Response`
    - **Endpoint** : 
        - methode: `GET` 
        - url: `/v1/authors/{author_id}`
    - **Authentification** : false
    - **Type retourné** : GetAuthorByIdV1Response