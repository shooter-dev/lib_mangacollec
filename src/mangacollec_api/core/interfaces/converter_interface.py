import abc
from abc import ABC
from typing import Dict, TypeVar, Generic

# Définition du type générique T
T = TypeVar("T")


class IConverterEntity(ABC, Generic[T]):
    @abc.abstractmethod
    def serialize(self, model: T) -> Dict:
        """Transforme un objet du modèle T en dictionnaire."""
        pass

    @abc.abstractmethod
    def deserialize(self, data: Dict) -> T:
        """Transforme un dictionnaire en objet du modèle T."""
        pass
