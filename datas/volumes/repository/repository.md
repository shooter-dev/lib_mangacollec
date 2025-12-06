# REPOSITORY DOCUMENTATION

## APIVolumeRepository

**Description** : Gère les opérations de récupération et de manipulation des données des volumes dans l'API.

### Méthodes Disponibles

- `get_volume_by_id_v2(volume_id: str)` -> `GetVolumeByIdV2Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v2/volumes/{volume_id}`
    - **Authentification** : true
    - **Type retourné** : GetVolumeByIdV2Response

- `get_volumes_news_v2()` -> `GetVolumesNewsV2Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v2/volumes/news`
    - **Authentification** : false
    - **Type retourné** : GetVolumesNewsV2Response