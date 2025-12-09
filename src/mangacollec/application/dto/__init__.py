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
    "GetAllAuthorsV2Response",
    "GetAllJobsV1Response",
    "GetAllPublishersV2Response",
    "GetAuthorByIdV2Response",
    "GetEditionByIdV2Response",
    "GetPublisherByIdV2Response",
    "SearchAuthor",
]

from mangacollec.application.dto.author_dto import SearchAuthor
from mangacollec.application.dto.author_responses import GetAllAuthorsV2Response, GetAuthorByIdV2Response
from mangacollec.application.dto.edition_responses import GetEditionByIdV2Response
from mangacollec.application.dto.job_responses import GetAllJobsV1Response
from mangacollec.application.dto.publisher_responses import (
    GetAllPublishersV2Response,
    GetPublisherByIdV2Response,
)
