# REPOSITORY DOCUMENTATION

## APIPlanningRepository

**Description** : Gère les opérations de récupération des données de planning (volumes et coffrets planifiés) dans l'API.

### Méthodes Disponibles
- `get_planning_v2(month: str)` -> `GetPlanningV2Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v2/planning/?month={month}`
    - **Paramètres** :
      - `month` (str) : Date au format YYYY-MM-DD (ex: "2022-09-30")
    - **Authentification** : false
    - **Type retourné** : GetPlanningV2Response

- `get_planning_v1(month: str)` -> `GetPlanningV1Response`
    - **Endpoint** :
      - methode: `GET`
      - url: `/v1/planning/?month={month}`
    - **Paramètres** :
      - `month` (str) : Date au format YYYY-MM-DD (ex: "2022-09-30")
    - **Authentification** : false
    - **Type retourné** : GetPlanningV1Response
