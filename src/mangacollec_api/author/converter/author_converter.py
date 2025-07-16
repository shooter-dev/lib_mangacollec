from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.author.entity.author import Author


class AuthorConverter(IConverterEntity[Author]):
    def serialize(self, model: Author) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Author:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Author(
            id=data["id"],
            name=data["name"],
            first_name=data["first_name"],
            tasks_count=data["tasks_count"],
        )
