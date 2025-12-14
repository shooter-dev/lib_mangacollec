# TODO

## Critères d'Acceptation Globaux

Pour qu'une ressource soit considérée comme **TERMINÉE**, elle doit respecter **TOUS** les critères suivants :

### 1. Architecture Clean Code

- [ ] **Entity** : Entité du domaine créée avec tous les attributs
- [ ] **Repository Interface** : Interface du repository avec UNIQUEMENT les méthodes supportées par l'API
- [ ] **DTOs** : Tous les DTOs de réponse créés (GetAll, GetById, Create, etc.)
- [ ] **Mapper** : Toutes les méthodes obligatoires implémentées :
  - [ ] `from_dict()` - OBLIGATOIRE
  - [ ] `to_dict()` - OBLIGATOIRE
  - [ ] `from_api_response()` - Si structure normalisée
  - [ ] `from_all_{resources}_response()` - Si endpoint get_all existe
- [ ] **Use Cases** : Tous les cas d'utilisation créés selon les méthodes disponibles
- [ ] **API Repository** : Implémentation API avec `IMangaCollecAPI` et délégation aux mappers
- [ ] **InMemory Repository** : Implémentation en mémoire pour les tests

### 2. Qualité du Code

- [ ] **Type hints** : Partout (fonctions, méthodes, attributs)
- [ ] **Docstrings** : Format Google style sur toutes les classes et méthodes publiques
- [ ] **Formatage** : `ruff format` sans erreur
- [ ] **Linting** : `ruff check` sans erreur
- [ ] **Imports** : Organisés et sans imports inutilisés

### 3. Tests

- [ ] **Couverture** : ≥ 90% de couverture de code
- [ ] **Tests unitaires** :
  - [ ] Entity Tests
  - [ ] Mapper Tests (tous les from*\* et to*\*)
  - [ ] Repository Tests (InMemory et API)
- [ ] **Tests d'intégration** : Tous les use cases testés
- [ ] **Assertions** : Tests pertinents avec assertions significatives
- [ ] **Fixtures** : Utilisation de fixtures pytest pour réutilisabilité

### 4. Conformité aux Patterns

- [ ] **Mapper** : Suit tous le meme pattern
- [ ] **Repository API** :
  - [ ] Utilise `IMangaCollecAPI` **Obligatoire** (pas `requests`)
  - [ ] Délègue toutes les conversions aux mappers
  - [ ] Gère les erreurs avec exceptions de domaine
- [ ] **DTOs Response** : Utilise des listes (pluriel) pour les entités
- [ ] **Gestion des erreurs** : Exceptions personnalisées (`{Resource}NotFoundException`)

### 5. Validation Finale

- [ ] **Build** : `pytest` passe sans erreur
- [ ] **Documentation** : README à jour si nécessaire
- [ ] **Cohérence** : Nommage cohérent avec les conventions du projet
- [ ] **Review** : Code relu et validé

---

## Authors
**notes**
>

- [x] Author Entity
- [x] Author Repository
  - [x] InMemoryAuthorRepository
  - [x] APIAuthorRepository
- [x] Author Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_all_authors_v2_response
  - [x] from_author_detail_v2_response
- [x] Author DTOs
  - [x] GetAllAuthorsV2Response
  - [x] GetAuthorByIdV2Response
- [x] Author Use Cases
  - [x] GetAllAuthorsV2
  - [x] GetAuthorByIdV2
  - [x] GetListAuthors
- [x] Tests
  - [x] Unit Tests
    - [x] Author Entity Tests
    - [x] Author Repository Tests
      - [x] InMemoryAuthorRepository Tests
      - [x] APIAuthorRepository Tests
    - [x] Author Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_all_authors_v2_response Tests
      - [x] from_author_detail_v2_response Tests
  - [x] Integration Tests
    - [x] GetAllAuthorsV2 Tests
    - [x] GetAuthorByIdV2 Tests
    - [x] GetListAuthors Tests

## Editions
**notes**
>

- [x] Edition Entity
- [x] Edition Repository
  - [x] InMemoryEditionRepository
  - [x] APIEditionRepository
- [x] Edition Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_edition_detail_v2_response
- [x] Edition DTOs
  - [x] GetEditionByIdV2Response
- [x] Edition Use Cases
  - [x] GetEditionByIdV2
- [x] Tests
  - [x] Unit Tests
    - [x] Edition Entity Tests
    - [x] Edition Repository Tests
      - [x] InMemoryEditionRepository Tests
      - [x] APIEditionRepository Tests
    - [x] Edition Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_edition_detail_v2_response Tests
  - [x] Integration Tests
    - [x] GetEditionByIdV2 Tests

## jobs
**notes**
>

- [x] Job Entity
- [x] Job Repository
  - [x] InMemoryJobRepository
  - [x] APIJobRepository
- [x] Job Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_all_jobs_response
- [x] Job DTOs
  - [x] GetAllJobsV1Response
- [x] Job Use Cases
  - [x] GetAllJobsV1
- [x] Tests
  - [x] Unit Tests
    - [x] Job Entity Tests
    - [x] Job Repository Tests
      - [x] InMemoryJobRepository Tests
      - [x] APIJobRepository Tests
    - [x] Job Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_all_jobs_response Tests
  - [x] Integration Tests
    - [x] GetAllJobsV1 Tests

## Publishers
**notes**
>

- [x] Publisher Entity
- [x] Publisher Repository
  - [x] InMemoryPublisherRepository
  - [x] APIPublisherRepository
- [x] Publisher Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_all_publishers_response
  - [x] from_publisher_detail_response
- [x] Publisher DTOs
  - [x] GetAllPublishersV2Response
  - [x] GetPublisherByIdV2Response
- [x] Publisher Use Cases
  - [x] GetAllPublishersV2
  - [x] GetPublisherByIdV2
  - [x] GetListPublishers
- [x] Tests
  - [x] Unit Tests
    - [x] Publisher Entity Tests
    - [x] Publisher Repository Tests
      - [x] InMemoryPublisherRepository Tests
      - [x] APIPublisherRepository Tests
    - [x] Publisher Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_all_publishers_response Tests
      - [x] from_publisher_detail_response Tests
  - [x] Integration Tests
    - [x] GetAllPublishersV2 Tests
    - [x] GetPublisherByIdV2 Tests
    - [x] GetListPublishers Tests

## Follow Editions
**notes**
>

- [x] FollowEdition Entity
- [x] FollowEdition Repository
  - [x] InMemoryFollowEditionRepository
  - [x] APIFollowEditionRepository
- [x] FollowEdition Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_api_response
- [x] FollowEdition DTOs
  - [x] FollowEditionV1Response
- [x] FollowEdition Use Cases
  - [x] FollowEditionV1
  - [x] UnfollowEditionV1
- [x] Tests
  - [x] Unit Tests
    - [x] FollowEdition Entity Tests
    - [x] FollowEdition Repository Tests
      - [x] InMemoryFollowEditionRepository Tests
      - [x] APIFollowEditionRepository Tests
    - [x] FollowEdition Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_api_response Tests
  - [x] Integration Tests
    - [x] FollowEditionV1 Tests
    - [x] UnfollowEditionV1 Tests

## Kinds
**notes**
>

- [x] Kind Entity
- [x] Kind Repository
  - [x] InMemoryKindRepository
  - [x] APIKindRepository
- [x] Kind Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_all_kinds_v1_response
  - [x] from_all_kinds_v2_response
- [x] Kind DTOs
  - [x] GetAllKindsV1Response
  - [x] GetAllKindsV2Response
- [x] Kind Use Cases
  - [x] GetAllKindsV1
  - [x] GetAllKindsV2
- [x] Tests
  - [x] Unit Tests
    - [x] Kind Entity Tests
    - [x] Kind Repository Tests
      - [x] InMemoryKindRepository Tests
      - [x] APIKindRepository Tests
    - [x] Kind Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_all_kinds_v1_response Tests
      - [x] from_all_kinds_v2_response Tests
  - [x] Integration Tests
    - [x] GetAllKindsV1 Tests
    - [x] GetAllKindsV2 Tests

## Offers
**notes**
>

- [x] AmazonOffer Entity
- [x] BDFugueOffer Entity
- [x] Offer Repository
  - [x] InMemoryOfferRepository
  - [x] APIOfferRepository
- [x] Offer Mapper
  - [x] to_dict_amazon
  - [x] to_dict_bdfugue
  - [x] from_dict_amazon
  - [x] from_dict_bdfugue
  - [x] from_amazon_offer_response
  - [x] from_bdfugue_offer_response
- [x] Offer DTOs
  - [x] GetAmazonOfferV1Response
  - [x] GetBDFugueOfferV1Response
- [x] Offer Use Cases
  - [x] GetAmazonOfferV1
  - [x] GetBDFugueOfferV1
- [x] Tests
  - [x] Unit Tests
    - [x] AmazonOffer Entity Tests
    - [x] BDFugueOffer Entity Tests
    - [x] Offer Repository Tests
      - [x] InMemoryOfferRepository Tests
      - [x] APIOfferRepository Tests
    - [x] Offer Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_amazon_offer_response Tests
      - [x] from_bdfugue_offer_response Tests
  - [x] Integration Tests
    - [x] GetAmazonOfferV1 Tests
    - [x] GetBDFugueOfferV1 Tests

## Planning
**notes**
>

- [x] Planning Repository
  - [x] InMemoryPlanningRepository
  - [x] APIPlanningRepository
- [x] Planning Mapper
  - [x] from_planning_v2_response
- [x] Planning DTOs
  - [x] GetPlanningV2Response
- [x] Planning Use Cases
  - [x] GetPlanningV2
- [x] Tests
  - [x] Unit Tests
    - [x] Planning Repository Tests
      - [x] InMemoryPlanningRepository Tests (via use cases)
      - [x] APIPlanningRepository Tests
    - [x] Planning Mapper Tests
      - [x] from_planning_v2_response Tests
  - [x] Integration Tests
    - [x] GetPlanningV2 Tests

## Possessions
**notes**
>

- [x] Possession Entity
- [x] Possession Repository
  - [x] InMemoryPossessionRepository
  - [x] APIPossessionRepository
- [x] Possession Mapper
  - [x] to_dict
  - [x] from_dict
  - [x] from_add_possessions_response
  - [x] from_delete_possessions_response
- [x] Possession DTOs
  - [x] AddPossessionsMultipleV1Response
  - [x] DeletePossessionsMultipleV1Response
- [x] Possession Use Cases
  - [x] AddPossessionsMultipleV1
  - [x] DeletePossessionsMultipleV1
- [x] Tests
  - [x] Unit Tests
    - [x] Possession Entity Tests
    - [x] Possession Repository Tests
      - [x] InMemoryPossessionRepository Tests
      - [x] APIPossessionRepository Tests
    - [x] Possession Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_add_possessions_response Tests
      - [x] from_delete_possessions_response Tests
  - [x] Integration Tests
    - [x] AddPossessionsMultipleV1 Tests
    - [x] DeletePossessionsMultipleV1 Tests

## Reads
**notes**
>

- [x] Read Entity
- [x] Read Repository
  - [x] InMemoryReadRepository
  - [x] APIReadRepository
- [x] Read Mapper
  - [x] to_read_dict
  - [x] from_read_dict
  - [x] from_create_reads_response
  - [x] from_delete_reads_response
- [x] Read DTOs
  - [x] CreateReadsMultipleV1Response
  - [x] DeleteReadsMultipleV1Response
- [x] Read Use Cases
  - [x] CreateReadsMultipleV1
  - [x] DeleteReadsMultipleV1
- [x] Tests
  - [x] Unit Tests
    - [x] Read Entity Tests
    - [x] Read Repository Tests
      - [x] InMemoryReadRepository Tests
      - [x] APIReadRepository Tests
    - [x] Read Mapper Tests
      - [x] to_dict Tests
      - [x] from_dict Tests
      - [x] from_create_reads_response Tests
      - [x] from_delete_reads_response Tests
  - [x] Integration Tests
    - [x] CreateReadsMultipleV1 Tests
    - [x] DeleteReadsMultipleV1 Tests

## Series
**notes**
>

- [ ] Serie Entity
- [ ] Serie Repository
  - [ ] InMemorySerieRepository
  - [ ] APISerieRepository
- [ ] Serie Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_all_series_v2_response
  - [ ] from_serie_detail_v2_response
- [ ] Serie DTOs
  - [ ] GetAllSeriesV2Response
  - [ ] GetSerieByIdV2Response
- [ ] Serie Use Cases
  - [ ] GetAllSeriesV2
  - [ ] GetSerieByIdV2
  - [ ] GetListSeries
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Serie Entity Tests
    - [ ] Serie Repository Tests
      - [ ] InMemorySerieRepository Tests
      - [ ] APISerieRepository Tests
    - [ ] Serie Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_all_series_v2_response Tests
      - [ ] from_serie_detail_v2_response Tests
  - [ ] Integration Tests
    - [ ] GetAllSeriesV2 Tests
    - [ ] GetSerieByIdV2 Tests
    - [ ] GetListSeries Tests

## Types
**notes**
>

- [ ] TypeSerie Entity
- [ ] TypeSerie Repository
  - [ ] InMemoryTypeSerieRepository
  - [ ] APITypeSerieRepository
- [ ] TypeSerie Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_all_types_v1_response
- [ ] TypeSerie DTOs
  - [ ] GetAllTypesSerieV1Response
- [ ] TypeSerie Use Cases
  - [ ] GetAllTypesSerieV1
  - [ ] GetListTypesSerie
- [ ] Tests
  - [ ] Unit Tests
    - [ ] TypeSerie Entity Tests
    - [ ] TypeSerie Repository Tests
      - [ ] InMemoryTypeSerieRepository Tests
      - [ ] APITypeSerieRepository Tests
    - [ ] TypeSerie Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_all_types_v1_response Tests
  - [ ] Integration Tests
    - [ ] GetAllTypesSerieV1 Tests
    - [ ] GetListTypesSerie Tests

## Users
**notes**
>

- [ ] User Entity
- [ ] UserCollection Entity
- [ ] User Repository
  - [ ] InMemoryUserRepository
  - [ ] APIUserRepository
- [ ] User Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_user_collection_v2_response
  - [ ] from_me_collection_v2_response
  - [ ] from_me_recommendations_v1_response
- [ ] User DTOs
  - [ ] GetUserCollectionByUsernameV2Response
  - [ ] GetMeCollectionV2Response
  - [ ] GetMeRecommendationsV1Response
- [ ] User Use Cases
  - [ ] GetUserCollectionByUsernameV2
  - [ ] GetMeCollectionV2
  - [ ] GetMeRecommendationsV1
- [ ] Tests
  - [ ] Unit Tests
    - [ ] User Entity Tests
    - [ ] UserCollection Entity Tests
    - [ ] User Repository Tests
      - [ ] InMemoryUserRepository Tests
      - [ ] APIUserRepository Tests
    - [ ] User Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_user_collection_v2_response Tests
      - [ ] from_me_collection_v2_response Tests
      - [ ] from_me_recommendations_v1_response Tests
  - [ ] Integration Tests
    - [ ] GetUserCollectionByUsernameV2 Tests
    - [ ] GetMeCollectionV2 Tests
    - [ ] GetMeRecommendationsV1 Tests

## Volumes
**notes**
>

- [ ] Volume Entity
- [ ] Volume Repository
  - [ ] InMemoryVolumeRepository
  - [ ] APIVolumeRepository
- [ ] Volume Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_volume_detail_v2_response
  - [ ] from_volumes_news_v2_response
- [ ] Volume DTOs
  - [ ] GetVolumeByIdV2Response
  - [ ] GetVolumesNewsV2Response
- [ ] Volume Use Cases
  - [ ] GetVolumeByIdV2
  - [ ] GetVolumesNewsV2
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Volume Entity Tests
    - [ ] Volume Repository Tests
      - [ ] InMemoryVolumeRepository Tests
      - [ ] APIVolumeRepository Tests
    - [ ] Volume Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_volume_detail_v2_response Tests
      - [ ] from_volumes_news_v2_response Tests
  - [ ] Integration Tests
    - [ ] GetVolumeByIdV2 Tests
    - [ ] GetVolumesNewsV2 Tests
