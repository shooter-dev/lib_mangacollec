from typing import Dict
from mangacollec_api.core.interfaces.converter_interface import IConverterEntity
from mangacollec_api.users.entity.user import User


class UserConverter(IConverterEntity[User]):
    def serialize(self, model: User) -> Dict:
        """
        Convertit une instance de modèle en dictionnaire.
        À implémenter selon la structure de T.
        """
        pass

    def deserialize(self, data: Dict) -> User:
        """
        Convertit un dictionnaire en instance de modèle T.
        À implémenter selon la structure attendue.
        """
        return User(
            username=data["username"],
            email=data.get("email"),
            id=data.get("id"),
        )