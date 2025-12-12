#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: __init__.py.py
# __directory__: src/mangacollec/application/dto
"""Application DTOs."""

__all__ = [
    "AddPossessionsMultipleV1Response",
    "CreateReadsMultipleV1Response",
    "DeletePossessionsMultipleV1Response",
    "DeleteReadsMultipleV1Response",
    "FollowEditionV1Response",
    "GetAllAuthorsV2Response",
    "GetAllJobsV1Response",
    "GetAllKindsV1Response",
    "GetAllKindsV2Response",
    "GetAllPublishersV2Response",
    "GetAllSeriesV2Response",
    "GetAllTypesSerieV1Response",
    "GetAmazonOfferV1Response",
    "GetAuthorByIdV2Response",
    "GetBDFugueOfferV1Response",
    "GetEditionByIdV2Response",
    "GetMeCollectionV2Response",
    "GetMeRecommendationsV1Response",
    "GetPlanningV2Response",
    "GetPublisherByIdV2Response",
    "GetSerieByIdV2Response",
    "GetUserCollectionByUsernameV2Response",
    "GetVolumeByIdV2Response",
    "GetVolumesNewsV2Response",
    "SearchAuthor",
]

from mangacollec.application.dto.author_dto import SearchAuthor
from mangacollec.application.dto.author_responses import (
    GetAllAuthorsV2Response, GetAuthorByIdV2Response)
from mangacollec.application.dto.edition_responses import \
    GetEditionByIdV2Response
from mangacollec.application.dto.follow_edition_responses import \
    FollowEditionV1Response
from mangacollec.application.dto.job_responses import GetAllJobsV1Response
from mangacollec.application.dto.kind_responses import (GetAllKindsV1Response,
                                                        GetAllKindsV2Response)
from mangacollec.application.dto.offer_responses import (
    GetAmazonOfferV1Response, GetBDFugueOfferV1Response)
from mangacollec.application.dto.planning_responses import \
    GetPlanningV2Response
from mangacollec.application.dto.possession_responses import (
    AddPossessionsMultipleV1Response, DeletePossessionsMultipleV1Response)
from mangacollec.application.dto.publisher_responses import (
    GetAllPublishersV2Response, GetPublisherByIdV2Response)
from mangacollec.application.dto.read_responses import (
    CreateReadsMultipleV1Response, DeleteReadsMultipleV1Response)
from mangacollec.application.dto.serie_responses import (
    GetAllSeriesV2Response, GetSerieByIdV2Response)
from mangacollec.application.dto.type_serie_responses import \
    GetAllTypesSerieV1Response
from mangacollec.application.dto.user_responses import (
    GetMeCollectionV2Response, GetMeRecommendationsV1Response,
    GetUserCollectionByUsernameV2Response)
from mangacollec.application.dto.volume_responses import (
    GetVolumeByIdV2Response, GetVolumesNewsV2Response)
