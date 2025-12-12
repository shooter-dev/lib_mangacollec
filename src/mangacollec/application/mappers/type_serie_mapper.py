"""TypeSerie mapper."""

from mangacollec.application.dto import GetAllTypesSerieV1Response
from mangacollec.domain.entities import TypeSerie


class TypeSerieMapper:
    """Mapper pour convertir entre TypeSerie et ses représentations."""

    @staticmethod
    def from_dict(data: dict) -> TypeSerie:
        """Convertit un dictionnaire en entité TypeSerie.

        Args:
            data: Dictionnaire contenant les données d'un type de série

        Returns:
            TypeSerie: Entité du domaine
        """
        return TypeSerie(
            id=data["id"],
            title=data["title"],
            to_display=data.get("to_display", False),
        )

    @staticmethod
    def to_dict(type_serie: TypeSerie) -> dict:
        """Convertit une entité TypeSerie en dictionnaire.

        Args:
            type_serie: Entité TypeSerie du domaine

        Returns:
            dict: Dictionnaire représentant le type de série
        """
        return {
            "id": type_serie.id,
            "title": type_serie.title,
            "to_display": type_serie.to_display,
        }

    @staticmethod
    def from_all_types_v1_response(response: list[dict]) -> GetAllTypesSerieV1Response:
        """Convertit la réponse API V1 en GetAllTypesSerieV1Response.

        La réponse de l'API V1 /types est une liste directe de types.

        Args:
            response: Liste de dictionnaires contenant les types de séries

        Returns:
            GetAllTypesSerieV1Response contenant la liste des types convertis
        """
        types = [TypeSerieMapper.from_dict(type_data) for type_data in response]

        return GetAllTypesSerieV1Response(types=types)
