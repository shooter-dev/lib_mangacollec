# REPOSITORY DOCUMENTATION

## APIUserRepository

**Description** : Gère les opérations de récupération des données utilisateur et de leur collection dans l'API.

### Méthodes Disponibles

- `get_user_collection_by_username_v2(username: str)` -> `GetUserCollectionByUsernameV2Response`
    - **Endpoint** :
      - méthode: `GET`
      - url: `/v2/user/{username}/collection`
    - **Authentification** : false
    - **Type retourné** : GetUserCollectionByUsernameV2Response

- `get_me_collection_v2()` -> `GetMeCollectionV2Response`
    - **Endpoint** :
      - méthode: `GET`
      - url: `/v2/users/me/collection`
    - **Authentification** : true
    - **Type retourné** : GetMeCollectionV2Response

- `get_me_recommendations_v1()` -> `GetMeRecommendationsV1Response`
    - **Endpoint** :
      - méthode: `GET`
      - url: `/v1/users/me/recommendation`
    - **Authentification** : true
    - **Type retourné** : GetMeRecommendationsV1Response
