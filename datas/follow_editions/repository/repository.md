# REPOSITORY DOCUMENTATION

## APIFollowEditionRepository
**Description** : Gère les opérations de récupération et de manipulation des données des suivis d'éditions dans l'api'.

### Méthodes Disponibles
- `follow_edition_v1(id_edition: str)` -> `FollowEditionV1Response`
    - **Endpoint** : 
      - methode: `POST`
      - url: `/v1/follow-editions`
    - **Authentification** : true
    - **Type retourné** : FollowEditionV1Response

- `unfollow_edition_v1(id_follow_edition: str)` -> `bool`
    - **Endpoint** : 
      - methode: `DELETE`
      - url: `/v1/follow-editions/{id_follow_edition}`
    - **Authentification** : true
    - **Type retourné** : true -> 204 No Content | false -> autre code HTTP