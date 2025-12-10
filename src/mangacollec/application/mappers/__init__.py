#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: __init__.py.py
# __directory__: src/application/mappers
"""Mappers module for converting between API responses and domain entities."""

__all__ = [
    "AuthorMapper",
    "BoxMapper",
    "BoxEditionMapper",
    "EditionMapper",
    "JobMapper",
    "PublisherMapper",
    "SerieMapper",
    "TaskMapper",
    "TypeSerieMapper",
    "VolumeMapper",
    "FollowEditionMapper",
]

from mangacollec.application.mappers.author_mapper import AuthorMapper
from mangacollec.application.mappers.box_edition_mapper import BoxEditionMapper
from mangacollec.application.mappers.box_mapper import BoxMapper
from mangacollec.application.mappers.edition_mapper import EditionMapper
from mangacollec.application.mappers.follow_edition_mapper import \
    FollowEditionMapper
from mangacollec.application.mappers.job_mapper import JobMapper
from mangacollec.application.mappers.publisher_mapper import PublisherMapper
from mangacollec.application.mappers.serie_mapper import SerieMapper
from mangacollec.application.mappers.task_mapper import TaskMapper
from mangacollec.application.mappers.type_mapper import TypeSerieMapper
from mangacollec.application.mappers.volume_mapper import VolumeMapper
