"""Use cases."""

__all__ = [
    "AddPossessionsMultipleV1UseCase",
    "CreateReadsMultipleV1UseCase",
    "DeletePossessionsMultipleV1UseCase",
    "DeleteReadsMultipleV1UseCase",
    "FollowEditionV1UseCase",
    "GetAllAuthorUseCase",
    "GetAllJobsV1UseCase",
    "GetAllKindsV1UseCase",
    "GetAllKindsV2UseCase",
    "GetAllPublishersV2UseCase",
    "GetAllSeriesV2UseCase",
    "GetAllTypesSerieV1UseCase",
    "GetAmazonOfferV1UseCase",
    "GetBDFugueOfferV1UseCase",
    "GetByIdAuthorUseCase",
    "GetEditionByIdV2UseCase",
    "GetListAuthorUseCase",
    "GetListPublishersUseCase",
    "GetListSeriesUseCase",
    "GetMeCollectionV2UseCase",
    "GetMeRecommendationsV1UseCase",
    "GetPlanningV2UseCase",
    "GetPublisherByIdV2UseCase",
    "GetSerieByIdV2UseCase",
    "GetUserCollectionByUsernameV2UseCase",
    "GetVolumeByIdV2UseCase",
    "GetVolumesNewsV2UseCase",
    "SearchAuthorUseCase",
    "UnfollowEditionV1UseCase",
]

from mangacollec.application.use_cases.author_usecase import (
    GetAllAuthorUseCase,
    GetByIdAuthorUseCase,
    GetListAuthorUseCase,
    SearchAuthorUseCase,
)
from mangacollec.application.use_cases.edition_usecase import GetEditionByIdV2UseCase
from mangacollec.application.use_cases.follow_edition_usecase import (
    FollowEditionV1UseCase,
    UnfollowEditionV1UseCase,
)
from mangacollec.application.use_cases.job_usecase import GetAllJobsV1UseCase
from mangacollec.application.use_cases.kind_usecase import (
    GetAllKindsV1UseCase,
    GetAllKindsV2UseCase,
)
from mangacollec.application.use_cases.offer_usecase import (
    GetAmazonOfferV1UseCase,
    GetBDFugueOfferV1UseCase,
)
from mangacollec.application.use_cases.planning_usecase import GetPlanningV2UseCase
from mangacollec.application.use_cases.possession_usecase import (
    AddPossessionsMultipleV1UseCase,
    DeletePossessionsMultipleV1UseCase,
)
from mangacollec.application.use_cases.publisher_usecase import (
    GetAllPublishersV2UseCase,
    GetListPublishersUseCase,
    GetPublisherByIdV2UseCase,
)
from mangacollec.application.use_cases.read_usecase import (
    CreateReadsMultipleV1UseCase,
    DeleteReadsMultipleV1UseCase,
)
from mangacollec.application.use_cases.serie_usecase import (
    GetAllSeriesV2UseCase,
    GetListSeriesUseCase,
    GetSerieByIdV2UseCase,
)
from mangacollec.application.use_cases.type_serie_usecase import (
    GetAllTypesSerieV1UseCase,
)
from mangacollec.application.use_cases.user_usecase import (
    GetMeCollectionV2UseCase,
    GetMeRecommendationsV1UseCase,
    GetUserCollectionByUsernameV2UseCase,
)
from mangacollec.application.use_cases.volume_usecase import (
    GetVolumeByIdV2UseCase,
    GetVolumesNewsV2UseCase,
)
