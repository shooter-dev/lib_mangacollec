from typing import Dict
import datetime
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.volume.entity.volume import Volume


class VolumeConverter(IConverterEntity[Volume]):
    def serialize(self, model: Volume) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Volume:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        release_date = data.get("release_date")
        if isinstance(release_date, str):
            release_date = datetime.datetime.fromisoformat(release_date.replace('Z', '+00:00'))
        elif release_date is None:
            release_date = datetime.datetime.now()
        
        return Volume(
            id=data["id"],
            title=data.get("title"),
            number=data["number"],
            release_date=release_date,
            isbn=data.get("isbn"),
            asin=data.get("asin"),
            edition_id=data["edition_id"],
            possessions_count=data["possessions_count"],
            not_sold=data["not_sold"],
            image_url=data["image_url"],
        )