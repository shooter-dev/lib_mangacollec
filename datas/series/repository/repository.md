# REPOSITORY DOCUMENTATION

## APISerieRepository

**Description** : Gère les opérations de récupération et de manipulation des données des séries dans l'api'.

### Méthodes Disponibles
- `get_all_series_v2()` -> `GetAllSeriesV2Response`
  - **Endpoint** :
    - methode: `GET`
    - url: `/v2/series`
  - **Authentification** : false
  - **Type retourné** : GetAllSeriesV2Response

- `get_serie_by_id_v2(serie_id: str)` -> `GetSerieByIdV2Response`
  - **Endpoint** :
    - methode: `GET`
    - url: `/v2/series/{serie_id}`
  - **Authentification**: false
  - **Type retourné**: GetSerieByIdV2Response

- `get_all_series_v1()` -> `GetAllSeriesV1Response`
  - **Endpoint** :
    - methode: `GET`
    - url: `/v1/series`
  - **Authentification**: false
  - **Type retourné**: GetAllSeriesV1Response

- `get_serie_by_id_v1(serie_id: str)` -> `GetSerieByIdV1Response`
  - **Endpoint** :
    - methode: `GET`
    - url: `/v1/series/{serie_id}`
  - **Authentification**: false
  - **Type retourné**: GetSerieByIdV1Response

