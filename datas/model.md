# Model DOCUMENTATION

> **Voir aussi :**
> - Architecture du projet : [`CLAUDE.md`](../CLAUDE.md)
> - Endpoints par ressource : `datas/{resource}/endpoints/`
> - Repositories : `datas/{resource}/repository/repository.md`
> - Use Cases : `datas/{resource}/use_cases/`
> - Exemples de documentation : [`datas/_exemple/`](_exemple/)

## Modèles de données
**Stocké dans le répertoire `src/domain/models/`**

### Volume
**dataclass(frozen=True)**
- id: str
- title: str
- number: int | None
- release_date: date | None
- isbn: ISBN | None
- asin: ASIN | None
- edition_id: str
- possessions_count: int | None
- not_sold: bool
- image_url: URL | None
- nb_pages: int | None
- content: str | None

### Author
**dataclass(frozen=True)**
- id: str
- name: str
- first_name: str | None
- tasks_count: int

### Edition
**dataclass(frozen=True)**
- id: str
- title: str | None
- series_id: str
- publisher_id: str
- parent_edition_id: str | None
- volumes_count: int
- last_volume_number: int | None
- commercial_stop: bool
- not_finished: bool
- follow_editions_count: int

### Publisher
**dataclass(frozen=True)**
- id: str
- title: str
- closed: bool
- editions_count: int
- no_amazon: bool

### Serie
**dataclass(frozen=True)**
- id: str
- title: str
- type_id: str
- adult_content: bool
- editions_count: int
- tasks_count: int
- kinds: list[Kind] | None

### TypeSerie
**dataclass(frozen=True)**
- id: str
- title: str
- to_display: bool

### BoxVolume
**dataclass(frozen=True)**
- id: str
- box_id: str
- volume_id: str
- number: int

### Box
**dataclass(frozen=True)**
- id: str
- title: str | None
- number: int
- release_date: date | None
- isbn: ISBN | None
- asin: ASIN | None
- comercial_stop: bool
- box_edition_id: str
- box_possessions_count: int | None
- image_url: str | None

### BoxEdition
**dataclass(frozen=True)**
- id: str
- title: str | None
- publisher_id: str | None
- boxe_count: int
- adult_content: bool
- box_follow_editions_count: int

### Kind
**dataclass(frozen=True)**
- id: str
- title: str
- series_id: str | None

### Task
**dataclass(frozen=True)**
- id: str
- job_id: str
- series_id: str
- author_id: str

### Job
**dataclass(frozen=True)**
- id: str
- title: str

### FollowedEdition
**dataclass(frozen=True)**
- id: str
- edition_id: str
- user_id: str
- following: bool
- created_at: datetime (format ISO 8601)
- updated_at: datetime (format ISO 8601)

### Possession
**dataclass(frozen=True)**
- id: str
- volume_id: str
- user_id: str
- created_at: datetime (format ISO 8601)

### BoxPossession
**dataclass(frozen=True)**
- id: str
- box_id: str
- user_id: str
- created_at: datetime (format ISO 8601)

### BoxFollowEdition
**dataclass(frozen=True)**
- id: str
- box_edition_id: str
- user_id: str
- following: bool
- created_at: datetime (format ISO 8601)
- updated_at: datetime (format ISO 8601)

### ReadEdition
**dataclass(frozen=True)**
- id: str
- edition_id: str
- user_id: str
- reading: bool
- created_at: datetime (format ISO 8601)
- updated_at: datetime | None (format ISO 8601)

### Read
**dataclass(frozen=True)**
- id: str
- volume_id: str
- user_id: str
- created_at: datetime (format ISO 8601)

### BDFugueOffer
**dataclass(frozen=True)**
- id: ISBN
- formatted_price: str | None
- availability: str | None
- merchant: str
- store_link: URL

### AmazonOffer
**dataclass(frozen=True)**
- asin: ASIN
- formatted_price: str | None
- availability: str | None
- merchant: str
- store_link: URL

### NativeAdVolumeHomeFirst
**dataclass(frozen=True)**
- id: str
- volume_id: str
- title: str
- start_date: datetime
- end_date: datetime

### Borrower
**dataclass(frozen=True)**
- id: str
- user_id: str
- title: str
- category: str
- created_at: datetime (format ISO 8601)

### Loan
**dataclass(frozen=True)**
- id: str
- possession_id: str
- borrower_id: str
- created_at: datetime (format ISO 8601)

### User
**dataclass(frozen=True)**
- id: str
- email: EMAIL
- username: str
- notifications_email: bool
- setting_collection_order: str
- created_at: datetime (format ISO 8601)
- confirmed_at: datetime (format ISO 8601) | None
- confirmation_sent_at: str
- unconfirmed_email: str | None
- certify_adult: bool
- possessions_count: int
- ad_home_banner: bool
- ad_native_home_first: bool
- ad_native_planning_perso: bool
- is_premium: bool
- subscriptions: list[Subscription]

### Subscription
**dataclass(frozen=True)**
- id: str
- user_id: str
- app: str
- product_id: str
- original_purchase_date: str
- expires_date: str
- auto_renewing: bool
- created_at: datetime (format ISO 8601)
- updated_at: datetime (format ISO 8601)
- cancellation_date: str

### ReadDelete
**dataclass(frozen=True)**
- id: str
- deleted: bool

### ReadEditionDelete
**dataclass(frozen=True)**
- id: str
- deleted: bool

### PossessionDelete
**dataclass(frozen=True)**
- id: str
- deleted: bool

### FollowEditionDelete
**dataclass(frozen=True)**
- id: str
- deleted: bool

### LoanDelete
**dataclass(frozen=True)**
- id: str
- deleted: bool


## Models de réponses
**Stocké dans le répertoire `src/application/dto/responses/`**

### GetVolumeByIdV2Response
**dataclass(frozen=True)**
- volumes: list[Volume]
- editions: list[Edition]
- publishers: list[Publisher]
- series: list[Serie]
- types: list[TypeSerie]
- box_volumes: list[BoxVolume]
- boxes: list[Box]
- box_editions: list[BoxEdition]

### GetVolumesNewsV2Response
**dataclass(frozen=True)**
- volumes: list[Volume]
- editions: list[Edition]
- series: list[Serie]
- types: list[TypeSerie]
- boxes: list[Box]
- box_editions: list[BoxEdition]
- box_volumes: list[BoxVolume]
- native_ad_volume_home_first: NativeAdVolumeHomeFirst

### GetUserCollectionByUsernameV2Response
**dataclass(frozen=True)**
- editions: list[Edition]
- series: list[Serie]
- types: list[TypeSerie]
- kinds: list[Kind]
- volumes: list[Volume]
- box_editions: list[BoxEdition]
- boxes: list[Box]
- box_volumes: list[BoxVolume]
- follow_editions: list[FollowedEdition]
- possessions: list[Possession]
- box_possessions: list[BoxPossession]
- read_editions: list[ReadEdition]
- read: list[Read]

### GetAllTypesSerieV1Response
**dataclass(frozen=True)**
- types: list[TypeSerie]

### GetAllSeriesV2Response
**dataclass(frozen=True)**
- series: list[Serie]
- types: list[TypeSerie]

### GetSerieByIdV2Response
**dataclass(frozen=True)**
- series: list[Serie]
- types: list[TypeSerie]
- kinds: list[Kind]
- tasks: list[Task]
- jobs: list[Job]
- authors: list[Author]
- editions: list[Edition]
- publishers: list[Publisher]
- volumes: list[Volume]
- box_editions: list[BoxEdition]
- boxes: list[Box]
- box_volumes: list[BoxVolume]

### GetAllSeriesV1Response
**dataclass(frozen=True)**
**En cours**

### GetSerieByIdV1Response
**dataclass(frozen=True)**
**En cours**

### CreateReadsMultipleV1Response
**dataclass(frozen=True)**
- reads: list[Read]
- read_editions: list[ReadEdition]

### DeleteReadsMultipleV1Response
**dataclass(frozen=True)**
- reads: list[ReadDelete]
- read_editions: list[ReadEditionDelete]

### GetAllPublishersV2Response
**dataclass(frozen=True)**
- publishers: list[Publisher]

### GetPublisherByIdV2Response
**dataclass(frozen=True)**
- publishers: list[Publisher]
- editions: list[Edition]
- box_editions: list[BoxEdition]
- series: list[Serie]
- types: list[TypeSerie]
- volumes: list[Volume]
- boxes: list[Box]

### GetAllPublishersV1Response
**dataclass(frozen=True)**
**En cours**

### GetPublisherByIdV1Response
**dataclass(frozen=True)**
**En cours**

### AddPossessionsMultipleV1Response
**dataclass(frozen=True)**
- possessions: list[Possession]
- follow_editions: list[FollowedEdition]

### DeletePossessionsMultipleV1Response
**dataclass(frozen=True)**
- possessions: list[PossessionDelete]
- follow_editions: list[FollowEditionDelete]
- loans: list[LoanDelete]

### GetPlanningV2Response
**dataclass(frozen=True)**
- volumes: list[Volume]
- editions: list[Edition]
- series: list[Serie]
- types: list[TypeSerie]
- boxes: list[Box]
- box_editions: list[BoxEdition]
- box_volumes: list[BoxVolume]

### GetPlanningV1Response
**dataclass(frozen=True)**
**En cours**

### GetAmazonOfferV1Response
**dataclass(frozen=True)**
- amazon_offers: AmazonOffer

### GetBDFugueOfferV1Response
**dataclass(frozen=True)**
- bd_fugue_offers: BDFugueOffer

### GetAllKindsV2Response
**dataclass(frozen=True)**
- kinds: list[Kind]

### GetAllKindsV1Response
**dataclass(frozen=True)**
**En cours**

### GetAllJobsV1Response
**dataclass(frozen=True)**
- jobs: list[Job]

### FollowEditionV1Response
**dataclass(frozen=True)**
- follow_editions: FollowedEdition

### UnfollowEditionV1Response
**204 No Content**

### GetEditionByIdV2Response
**dataclass(frozen=True)**
- editions: list[Edition]
- publishers: list[Publisher]
- series: list[Serie]
- types: list[TypeSerie]
- volumes: list[Volume]

### GetEditionByIdV1Response
**dataclass(frozen=True)**
**En cours**

### GetAllAuthorsV2Response
**dataclass(frozen=True)**
- authors: list[Author]

### GetAuthorByIdV2Response
**dataclass(frozen=True)**
- authors: list[Author]
- tasks: list[Task]
- jobs: list[Job]
- series: list[Serie]
- editions: list[Edition]
- volumes: list[Volume]

### GetAuthorByIdV1Response
**dataclass(frozen=True)**
**En cours**

### GetAuthorByIdV1Response
**dataclass(frozen=True)**
**En cours**


## Value Objects
**Stocké dans le répertoire `src/domain/value_objects/`**

### ISBN
**Détaille** : Un identifiant ISBN (International Standard Book Number) est un code unique attribué à chaque édition 
d'un livre publié. 
Il est utilisé pour identifier de manière unique les livres dans le commerce et les bibliothèques. 
Un ISBN peut être au format ISBN-13.

### ASIN
**Détaille** : Un identifiant ASIN (Amazon Standard Identification Number) est un code unique attribué par Amazon

### URL
**Détaille** : Une URL (Uniform Resource Locator) est une adresse web utilisée pour localiser des ressources sur Internet.

### EMAIL
**Détaille** : Une adresse email est une chaîne de caractères utilisée pour identifier une boîte aux lettres électronique.