from abc import ABC, abstractmethod
from typing import Dict


class Entity(ABC):

    @abstractmethod
    def to_dict(self) -> Dict[str, any]:
        """

        :return:
        """
        pass