from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.edition.entity.edition import Edition


class EditionConverter(IConverterEntity[Edition]):
    def serialize(self, model: Edition) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> Edition:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return Edition(
            id=data["id"],
            title=data["title"],
            series_id=data["series_id"],
            publisher_id=data["publisher_id"],
            parent_edition_id=data.get("parent_edition_id"),
            volumes_count=data["volumes_count"],
            last_volume_number=data.get("last_volume_number"),
            commercial_stop=data["commercial_stop"],
            not_finished=data["not_finished"],
            follow_editions_count=data["follow_editions_count"],
        )