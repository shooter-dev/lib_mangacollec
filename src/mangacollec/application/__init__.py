#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __author__: lib_mangacollec
# __author__: ShooterDev
# __filename__: __init__.py.py
# __directory__: src/application
""" """

# DTOs
from .dto.author_dto import SearchAuthor
from .dto.responses.author_responses import (
    GetAuthorByIdV2Response,
    GetAllAuthorsV2Response,
)
from .dto.responses.edition_responses import GetEditionByIdV2Response
from .dto.responses.job_responses import GetAllJobsV1Response
from .dto.responses.publisher_responses import (
    GetPublisherByIdV2Response,
    GetAllPublishersV2Response,
)

# Mappers
from .mappers.author_mapper import AuthorMapper
from .mappers.edition_mapper import EditionMapper
from .mappers.job_mapper import JobMapper
from .mappers.publisher_mapper import PublisherMapper
from .mappers.serie_mapper import SerieMapper
from .mappers.task_mapper import TaskMapper
from .mappers.type_mapper import TypeMapper
from .mappers.volume_mapper import VolumeMapper
from .mappers.box_mapper import BoxMapper
from .mappers.box_edition_mapper import BoxEditionMapper


# Use Cases
from .use_cases.author_usecase import (
    GetAllAuthorUseCase,
    GetByIdAuthorUseCase,
    GetListAuthorUseCase,
    SearchAuthorUseCase,
)
from .use_cases.edition_usecase import GetEditionByIdV2UseCase
from .use_cases.job_usecase import GetAllJobsV1UseCase
from .use_cases.publisher_usecase import (
    GetAllPublishersV2UseCase,
    GetListPublishersUseCase,
    GetPublisherByIdV2UseCase,
)

# Interfaces
from .interfaces.mangacollec_api_interface import IMangaCollecAPI