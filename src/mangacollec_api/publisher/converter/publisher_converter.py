from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.publisher.entity.publisher import Publisher


class PublisherConverter(IConverterEntity[Publisher]):
    def serialize(self, model: Publisher) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Publisher:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Publisher(
            id=data["id"],
            title=data["title"],
            closed=data["closed"],
            editions_count=data["editions_count"],
            no_amazon=data["no_amazon"],
        )