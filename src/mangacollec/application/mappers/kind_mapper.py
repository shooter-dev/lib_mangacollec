"""Mapper pour la conversion des données Kind."""

from mangacollec.application.dto import GetAllKindsV1Response, GetAllKindsV2Response
from mangacollec.domain.entities import Kind


class KindMapper:
    """Mapper pour convertir les données Kind entre différents formats."""

    @staticmethod
    def from_dict(data: dict) -> Kind:
        """Convertit un dictionnaire en entité Kind.

        Args:
            data: Dictionnaire contenant les données d'un kind

        Returns:
            Kind: Entité Kind créée à partir du dictionnaire
        """
        return Kind(
            id=data["id"],
            name=data["name"],
            name_en=data["name_en"],
        )

    @staticmethod
    def to_dict(kind: Kind) -> dict:
        """Convertit une entité Kind en dictionnaire.

        Args:
            kind: Entité Kind à convertir

        Returns:
            dict: Dictionnaire contenant les données du kind
        """
        return {
            "id": kind.id,
            "name": kind.name,
            "name_en": kind.name_en,
        }

    @staticmethod
    def from_all_kinds_v2_response(response: dict) -> GetAllKindsV2Response:
        """Convertit la réponse de l'API V2 pour get_all_kinds.

        Args:
            response: Réponse API contenant la liste des kinds

        Returns:
            GetAllKindsV2Response contenant la liste des kinds convertis
        """
        kinds = [KindMapper.from_dict(kind_data) for kind_data in response.get("kinds", [])]

        return GetAllKindsV2Response(kinds=kinds)

    @staticmethod
    def from_all_kinds_v1_response(response: dict) -> GetAllKindsV1Response:
        """Convertit la réponse de l'API V1 pour get_all_kinds.

        Args:
            response: Réponse API contenant la liste des kinds

        Returns:
            GetAllKindsV1Response contenant la liste des kinds convertis
        """
        kinds = [KindMapper.from_dict(kind_data) for kind_data in response.get("kinds", [])]

        return GetAllKindsV1Response(kinds=kinds)
