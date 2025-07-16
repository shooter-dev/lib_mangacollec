from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.genre.entity.genre import Genre


class GenreConverter(IConverterEntity[Genre]):
    def serialize(self, model: Genre) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Genre:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Genre(
            id=data["id"],
            title=data["title"],
            to_display=data["to_display"],
        )