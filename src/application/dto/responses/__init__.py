"""Response DTOs module."""

__all__ = [
    "GetAllAuthorsV2Response",
    "GetAuthorByIdV2Response",
    "GetEditionByIdV2Response",
]

from src.application.dto.responses.author_responses import (
    GetAllAuthorsV2Response,
    GetAuthorByIdV2Response,
)
from src.application.dto.responses.edition_responses import GetEditionByIdV2Response
