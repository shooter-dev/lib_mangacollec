# TODO

## Critères d'Acceptation Globaux

Pour qu'une ressource soit considérée comme **TERMINÉE**, elle doit respecter **TOUS** les critères suivants :

### 1. Documentation

- [ ] Fichier `datas/{resource}/repository/repository.md` existe et documente toutes les méthodes
- [ ] Tous les endpoints ont leur fichier `.md` dans `datas/{resource}/endpoints/`
- [ ] Les use cases sont documentés dans `datas/{resource}/use_cases/`
- [ ] Les réponses JSON brutes sont présentes dans `datas/_endpoints/{resource}/`

### 2. Architecture Clean Code

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

### 3. Qualité du Code

- [ ] **Type hints** : Partout (fonctions, méthodes, attributs)
- [ ] **Docstrings** : Format Google style sur toutes les classes et méthodes publiques
- [ ] **Formatage** : `ruff format` sans erreur
- [ ] **Linting** : `ruff check` sans erreur
- [ ] **Imports** : Organisés et sans imports inutilisés

### 4. Tests

- [ ] **Couverture** : ≥ 90% de couverture de code
- [ ] **Tests unitaires** :
  - [ ] Entity Tests
  - [ ] Mapper Tests (tous les from*\* et to*\*)
  - [ ] Repository Tests (InMemory et API)
- [ ] **Tests d'intégration** : Tous les use cases testés
- [ ] **Assertions** : Tests pertinents avec assertions significatives
- [ ] **Fixtures** : Utilisation de fixtures pytest pour réutilisabilité

### 5. Conformité aux Patterns

- [ ] **Mapper** : Suit le pattern `AuthorMapper` (référence)
- [ ] **Repository API** :
  - [ ] Utilise `IMangaCollecAPI` (pas `requests`)
  - [ ] Délègue toutes les conversions aux mappers
  - [ ] Gère les erreurs avec exceptions de domaine
- [ ] **DTOs Response** : Utilise des listes (pluriel) pour les entités
- [ ] **Gestion des erreurs** : Exceptions personnalisées (`{Resource}NotFoundException`)

### 6. Validation Finale

- [ ] **Build** : `pytest` passe sans erreur
- [ ] **Documentation** : README à jour si nécessaire
- [ ] **Cohérence** : Nommage cohérent avec les conventions du projet
- [ ] **Review** : Code relu et validé

---

## Autors ✅ TERMINÉ (45/45 tests)

<!-- VERIFIED by Gemini on 2025-12-12 -->

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

## Editions ✅ TERMINÉ (71/71 tests)

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

## jobs ✅ TERMINÉ (31/31 tests)

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

## Publishers ✅ TERMINÉ (31/31 tests)

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

- [ ] FollowEdition Entity
- [ ] FollowEdition Repository
  - [ ] InMemoryFollowEditionRepository
  - [ ] APIFollowEditionRepository
- [ ] FollowEdition Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_follow_edition_response
- [ ] FollowEdition DTOs
  - [ ] FollowEditionV1Response
- [ ] FollowEdition Use Cases
  - [ ] FollowEditionV1
  - [ ] UnfollowEditionV1
- [ ] Tests
  - [ ] Unit Tests
    - [ ] FollowEdition Entity Tests
    - [ ] FollowEdition Repository Tests
      - [ ] InMemoryFollowEditionRepository Tests
      - [ ] APIFollowEditionRepository Tests
    - [ ] FollowEdition Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_follow_edition_response Tests
  - [ ] Integration Tests
    - [ ] FollowEditionV1 Tests
    - [ ] UnfollowEditionV1 Tests

## Kinds

- [ ] Kind Entity
- [ ] Kind Repository
  - [ ] InMemoryKindRepository
  - [ ] APIKindRepository
- [ ] Kind Mapper
  - [ ] to_dict
  - [ ] from_all_kinds_v2_response
- [ ] Kind DTOs
  - [ ] GetAllKindsV2Response
- [ ] Kind Use Cases
  - [ ] GetAllKindsV2
  - [ ] GetListKinds
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Kind Entity Tests
    - [ ] Kind Repository Tests
      - [ ] InMemoryKindRepository Tests
      - [ ] APIKindRepository Tests
    - [ ] Kind Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_all_kinds_v2_response Tests
  - [ ] Integration Tests
    - [ ] GetAllKindsV2 Tests
    - [ ] GetListKinds Tests

## Offers

- [ ] AmazonOffer Entity
- [ ] BDFugueOffer Entity
- [ ] Offer Repository
  - [ ] InMemoryOfferRepository
  - [ ] APIOfferRepository
- [ ] Offer Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_amazon_offer_response
  - [ ] from_bdfugue_offer_response
- [ ] Offer DTOs
  - [ ] GetAmazonOfferV1Response
  - [ ] GetBDFugueOfferV1Response
- [ ] Offer Use Cases
  - [ ] GetAmazonOfferV1
  - [ ] GetBDFugueOfferV1
- [ ] Tests
  - [ ] Unit Tests
    - [ ] AmazonOffer Entity Tests
    - [ ] BDFugueOffer Entity Tests
    - [ ] Offer Repository Tests
      - [ ] InMemoryOfferRepository Tests
      - [ ] APIOfferRepository Tests
    - [ ] Offer Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_amazon_offer_response Tests
      - [ ] from_bdfugue_offer_response Tests
  - [ ] Integration Tests
    - [ ] GetAmazonOfferV1 Tests
    - [ ] GetBDFugueOfferV1 Tests

## Planning

- [ ] Planning Entity
- [ ] Planning Repository
  - [ ] InMemoryPlanningRepository
  - [ ] APIPlanningRepository
- [ ] Planning Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_planning_v2_response
- [ ] Planning DTOs
  - [ ] GetPlanningV2Response
- [ ] Planning Use Cases
  - [ ] GetPlanningV2
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Planning Entity Tests
    - [ ] Planning Repository Tests
      - [ ] InMemoryPlanningRepository Tests
      - [ ] APIPlanningRepository Tests
    - [ ] Planning Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_planning_v2_response Tests
  - [ ] Integration Tests
    - [ ] GetPlanningV2 Tests

## Possessions

- [ ] Possession Entity
- [ ] Possession Repository
  - [ ] InMemoryPossessionRepository
  - [ ] APIPossessionRepository
- [ ] Possession Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_add_possessions_response
  - [ ] from_delete_possessions_response
- [ ] Possession DTOs
  - [ ] AddPossessionsMultipleV1Response
  - [ ] DeletePossessionsMultipleV1Response
- [ ] Possession Use Cases
  - [ ] AddPossessionsMultipleV1
  - [ ] DeletePossessionsMultipleV1
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Possession Entity Tests
    - [ ] Possession Repository Tests
      - [ ] InMemoryPossessionRepository Tests
      - [ ] APIPossessionRepository Tests
    - [ ] Possession Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_add_possessions_response Tests
      - [ ] from_delete_possessions_response Tests
  - [ ] Integration Tests
    - [ ] AddPossessionsMultipleV1 Tests
    - [ ] DeletePossessionsMultipleV1 Tests

## Reads

- [ ] Read Entity
- [ ] Read Repository
  - [ ] InMemoryReadRepository
  - [ ] APIReadRepository
- [ ] Read Mapper
  - [ ] to_dict
  - [ ] from_dict
  - [ ] from_create_reads_response
  - [ ] from_delete_reads_response
- [ ] Read DTOs
  - [ ] CreateReadsMultipleV1Response
  - [ ] DeleteReadsMultipleV1Response
- [ ] Read Use Cases
  - [ ] CreateReadsMultipleV1
  - [ ] DeleteReadsMultipleV1
- [ ] Tests
  - [ ] Unit Tests
    - [ ] Read Entity Tests
    - [ ] Read Repository Tests
      - [ ] InMemoryReadRepository Tests
      - [ ] APIReadRepository Tests
    - [ ] Read Mapper Tests
      - [ ] to_dict Tests
      - [ ] from_dict Tests
      - [ ] from_create_reads_response Tests
      - [ ] from_delete_reads_response Tests
  - [ ] Integration Tests
    - [ ] CreateReadsMultipleV1 Tests
    - [ ] DeleteReadsMultipleV1 Tests

## Series

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
