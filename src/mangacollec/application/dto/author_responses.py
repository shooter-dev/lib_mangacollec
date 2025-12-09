"""Response DTOs pour Author.

This module contains response DTOs for Author operations.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import Author, Edition, Job, Serie, Task, Volume


@dataclass(frozen=True)
class GetAllAuthorsV2Response:
    """Réponse pour GetAllAuthorsV2."""

    authors: list[Author]


@dataclass(frozen=True)
class GetAuthorByIdV2Response:
    """Réponse pour GetAuthorByIdV2."""

    authors: list[Author]
    tasks: list[Task]
    jobs: list[Job]
    series: list[Serie]
    editions: list[Edition]
    volumes: list[Volume]
