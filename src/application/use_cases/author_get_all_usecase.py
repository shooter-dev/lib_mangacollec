#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: author_get_usecase.py
# __directory__: src
"""


"""
from domain.entities.author_entity import Author
from domain.repositories.author_repository_interface import IAuthorRepository
from domain.execptions.author_exceptions import AuthorNotFoundException


class AuthorGetAllUseCase:
    def __init__(self, repo: IAuthorRepository):
        self._repo = repo

    def execute(self) -> list[Author]:
        authors: list[Author] = []
        authors = self._repo.get_all()