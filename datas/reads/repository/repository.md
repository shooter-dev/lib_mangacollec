# REPOSITORY DOCUMENTATION

## APIReadRepository

**Description** : Gère les opérations de création et de suppression des lectures de volumes dans l'API.

### Méthodes Disponibles
- `create_reads_multiple_v1(volume_ids: list[str])` -> `CreateReadsMultipleV1Response`
    - **Endpoint** :
      - methode: `POST`
      - url: `/v1/reads_multiple`
    - **Authentification** : true
    - **Type retourné** : CreateReadsMultipleV1Response

- `delete_reads_multiple_v1(read_ids: list[str])` -> `DeleteReadsMultipleV1Response`
    - **Endpoint** :
      - methode: `DELETE`
      - url: `/v1/reads_multiple`    
    - **Authentification** : true
    - **Type retourné** : DeleteReadsMultipleV1Response
