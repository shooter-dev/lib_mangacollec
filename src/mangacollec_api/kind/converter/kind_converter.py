from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.kind.entity.kind import Kind


class KindConverter(IConverterEntity[Kind]):
    def serialize(self, model: Kind) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Kind:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Kind(
            id=data["id"],
            title=data["title"],
        )