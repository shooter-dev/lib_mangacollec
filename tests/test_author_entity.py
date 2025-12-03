#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: test_author_entity.py
# __directory__: tests
"""


"""

import pytest

from domain.execptions.author_exceptions import AuthorNotFoundException
from application.use_cases.author_get_usecase import AuthorGetUseCase
from application.use_cases.author_add_usecase import AuthorAddUseCase
from domain.repositories.in_memory_author_repository import InMemoryAuthorRepository


@pytest.fixture()
def repository():
    return InMemoryAuthorRepository()
    
def test_add_author(repository):
    add_author_usecase = AuthorAddUseCase(repository)
    add_author = add_author_usecase.execute(
        id="370ac96c-49e0-4f09-b7c4-662cb1374b21",
        name="Kishimoto",
        first_name="Masashi",
        tasks_count=10
    )
    
    fetched_author = repository.get_by_id(add_author.id)
    
    assert fetched_author is not None
    assert fetched_author.id == "370ac96c-49e0-4f09-b7c4-662cb1374b21"
    assert fetched_author.name == "Kishimoto"
    assert fetched_author.first_name == "Masashi"
    assert fetched_author.tasks_count == 10

def test_add_author_without_first_name(repository):
    add_author_usecase = AuthorAddUseCase(repository)
    add_author = add_author_usecase.execute(
        id="d7f7a8a1-0543-462f-91ca-c4229f0c8108",
        name="Boichi",
        first_name="",
        tasks_count=14
    )

    fetched_author = repository.get_by_id(add_author.id)

    assert fetched_author is not None
    assert fetched_author.id == "d7f7a8a1-0543-462f-91ca-c4229f0c8108"
    assert fetched_author.name == "Boichi"
    assert fetched_author.first_name is None
    assert fetched_author.tasks_count == 14

def test_get_nonexistent_author(repository):
    get_author_usecase  = AuthorGetUseCase(repository)

    with pytest.raises(AuthorNotFoundException):
        get_author_usecase.execute(
            author_id="nonexistent-id"
        )

