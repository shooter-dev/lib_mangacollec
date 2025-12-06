# REPOSITORY DOCUMENTATION

## APIPossessionRepository

**Description** : Gère les opérations d'ajout et de suppression des possessions de volumes dans la collection de l'utilisateur via l'API.

### Méthodes Disponibles
- `add_possessions_multiple_v1(volume_ids: list[str])` -> `AddPossessionsMultipleV1Response`
    - **Endpoint** :
      - methode: `POST`
      - url: `/v1/possessions_multiple`
    - **Authentification** : true
    - **Type retourné** : AddPossessionsMultipleV1Response

- `delete_possessions_multiple_v1(possession_ids: list[str])` -> `DeletePossessionsMultipleV1Response`
    - **Endpoint** :
      - methode: `DELETE`
      - url: `/v1/possessions_multiple`
    - **Authentification** : true
    - **Type retourné** : DeletePossessionsMultipleV1Response
