"""Possession Mapper."""

from datetime import datetime

from mangacollec.application.dto import (
    AddPossessionsMultipleV1Response,
    DeletePossessionsMultipleV1Response,
)
from mangacollec.application.mappers import FollowEditionMapper
from mangacollec.domain.entities import (
    FollowEditionDeleted,
    LoanDeleted,
    Possession,
    PossessionDeleted,
)


class PossessionMapper:
    """Mapper pour convertir entre Possession et ses représentations."""

    @staticmethod
    def from_dict(data: dict) -> Possession:
        """Convertit un dictionnaire en entité Possession.

        Args:
            data: Dictionnaire contenant les données d'une possession

        Returns:
            Possession: L'entité du domaine
        """
        return Possession(
            id=data["id"],
            user_id=data["user_id"],
            volume_id=data["volume_id"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
        )

    @staticmethod
    def from_dict_deleted(data: dict) -> PossessionDeleted:
        """Convertit un dictionnaire en entité PossessionDeleted.

        Args:
            data: Dictionnaire contenant les données d'une possession supprimée

        Returns:
            PossessionDeleted: L'entité du domaine
        """
        return PossessionDeleted(
            id=data["id"],
            deleted=data["deleted"],
        )

    @staticmethod
    def from_dict_follow_edition_deleted(data: dict) -> FollowEditionDeleted:
        """Convertit un dictionnaire en entité FollowEditionDeleted.

        Args:
            data: Dictionnaire contenant les données d'un suivi d'édition supprimé

        Returns:
            FollowEditionDeleted: L'entité du domaine
        """
        return FollowEditionDeleted(
            id=data["id"],
            deleted=data["deleted"],
        )

    @staticmethod
    def from_dict_loan_deleted(data: dict) -> LoanDeleted:
        """Convertit un dictionnaire en entité LoanDeleted.

        Args:
            data: Dictionnaire contenant les données d'un prêt supprimé

        Returns:
            LoanDeleted: L'entité du domaine
        """
        return LoanDeleted(
            id=data["id"],
            deleted=data["deleted"],
        )

    @staticmethod
    def to_dict(possession: Possession) -> dict:
        """Convertit une entité Possession en dictionnaire.

        Args:
            possession: L'entité Possession à convertir

        Returns:
            dict: Représentation en dictionnaire
        """
        return {
            "id": possession.id,
            "user_id": possession.user_id,
            "volume_id": possession.volume_id,
            "created_at": possession.created_at.isoformat(),
        }

    @staticmethod
    def from_add_possessions_response(response: dict) -> AddPossessionsMultipleV1Response:
        """Convertit la réponse complète de l'API V1 en AddPossessionsMultipleV1Response.

        Args:
            response: Réponse API contenant possessions et follow_editions

        Returns:
            AddPossessionsMultipleV1Response contenant toutes les entités converties
        """
        # Convertir les possessions
        possessions = [
            PossessionMapper.from_dict(possession_data) for possession_data in response.get("possessions", [])
        ]

        # Convertir les follow_editions via leur mapper
        follow_editions = [
            FollowEditionMapper.from_dict(follow_edition_data)
            for follow_edition_data in response.get("follow_editions", [])
        ]

        return AddPossessionsMultipleV1Response(
            possessions=possessions,
            follow_editions=follow_editions,
        )

    @staticmethod
    def from_delete_possessions_response(response: dict) -> DeletePossessionsMultipleV1Response:
        """Convertit la réponse complète de l'API V1 en DeletePossessionsMultipleV1Response.

        Args:
            response: Réponse API contenant possessions, follow_editions et loans supprimés

        Returns:
            DeletePossessionsMultipleV1Response contenant toutes les entités converties
        """
        # Convertir les possessions supprimées
        possessions = [
            PossessionMapper.from_dict_deleted(possession_data) for possession_data in response.get("possessions", [])
        ]

        # Convertir les follow_editions supprimés
        follow_editions = [
            PossessionMapper.from_dict_follow_edition_deleted(follow_edition_data)
            for follow_edition_data in response.get("follow_editions", [])
        ]

        # Convertir les loans supprimés
        loans = [PossessionMapper.from_dict_loan_deleted(loan_data) for loan_data in response.get("loans", [])]

        return DeletePossessionsMultipleV1Response(
            possessions=possessions,
            follow_editions=follow_editions,
            loans=loans,
        )
