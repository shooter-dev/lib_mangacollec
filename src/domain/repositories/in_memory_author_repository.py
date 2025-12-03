#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: in_memory_author_repository.py
# __directory__: 
"""


"""
from domain.entities.author_entity import Author
from author_repository_interface import IAuthorRepository


class InMemoryAuthorRepository(IAuthorRepository):

    def __int__(self):
        self._authors: dict[str, Author] = {}

    def get_all(self) -> list[Author]:
        return list(self._authors.values())

    def get_by_id(self, id: str) -> Author | None:
        return self._authors.get(id, None)

    def add(self, author: Author):
        self._authors[author.id] = author
