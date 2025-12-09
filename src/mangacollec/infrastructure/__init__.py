#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __author__: lib_mangacollec
# __author__: ShooterDev
# __filename__: __init__.py.py
# __directory__: src/infrastructure
""" """

from .repositories.api.api_author_repository import APIAuthorRepository
from .repositories.api.api_edition_repository import APIEditionRepository
from .repositories.api.api_job_repository import APIJobRepository
from .repositories.api.api_publisher_repository import APIPublisherRepository

from .repositories.memory.in_memory_author_repository import InMemoryAuthorRepository
from .repositories.memory.in_memory_edition_repository import InMemoryEditionRepository
from .repositories.memory.inmemory_job_repository import InMemoryJobRepository
from .repositories.memory.inmemory_publisher_repository import InMemoryPublisherRepository
