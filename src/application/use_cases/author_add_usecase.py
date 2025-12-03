#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: author_add_usecase.py
# __directory__: src
"""


"""
from domain.entities.author_entity import Author
from domain.repositories.author_repository_interface import IAuthorRepository


class AuthorAddUseCase():
    def __init__(self, repo: IAuthorRepository):
        self.repo = repo

    def execute(self, id: str, name: str, first_name: str | None, tasks_count: int):
        if first_name == "":
            first_name = None

        author = Author(id=id, name=name, first_name=first_name, tasks_count=tasks_count)
        self.repo.add(author=author)

        return author