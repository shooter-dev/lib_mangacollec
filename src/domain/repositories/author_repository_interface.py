#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: author_repository_interface.py
# __directory__: 
"""


"""
from abc import ABC, abstractmethod

from domain.entities.author_entity import Author


class IAuthorRepository(ABC):

    # @abstractmethod
    # def create(self):
    #     ...

    @abstractmethod
    def add(self, author: Author):
        ...

    @abstractmethod
    def get_by_id(self, id: str) -> Author | None:
        ...

    @abstractmethod
    def get_all(self) -> list[Author]:
        ...