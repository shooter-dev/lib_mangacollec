from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.serie.entity.serie import Serie


class SerieConverter(IConverterEntity[Serie]):
    def serialize(self, model: Serie) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Serie:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Serie(
            id=data["id"],
            title=data["title"],
            type_id=data["type_id"],
            adult_content=data["adult_content"],
            editions_count=data["editions_count"],
            tasks_count=data["tasks_count"],
        )