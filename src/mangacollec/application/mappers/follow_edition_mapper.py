"""Follow Edition Mapper."""

from datetime import datetime

from mangacollec.application.dto import FollowEditionV1Response
from mangacollec.domain.entities import FollowEdition


class FollowEditionMapper:
    """Mapper pour convertir entre FollowEdition et ses représentations."""

    @staticmethod
    def from_dict(data: dict) -> FollowEdition:
        """Convertit un dictionnaire en entité FollowEdition.

        Args:
            data: Dictionnaire contenant les données d'un suivi d'édition

        Returns:
            FollowEdition: L'entité du domaine
        """
        return FollowEdition(
            id=data["id"],
            user_id=data["user_id"],
            edition_id=data["edition_id"],
            following=data["following"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00")),
        )

    @staticmethod
    def to_dict(follow_edition: FollowEdition) -> dict:
        """Convertit une entité FollowEdition en dictionnaire.

        Args:
            follow_edition: L'entité FollowEdition à convertir

        Returns:
            dict: Représentation en dictionnaire
        """
        return {
            "id": follow_edition.id,
            "user_id": follow_edition.user_id,
            "edition_id": follow_edition.edition_id,
            "following": follow_edition.following,
            "created_at": follow_edition.created_at.isoformat(),
            "updated_at": follow_edition.updated_at.isoformat(),
        }

    @staticmethod
    def from_api_response(response: dict) -> FollowEditionV1Response:
        """Convertit la réponse complète de l'API V1 en FollowEditionV1Response.

        Args:
            response: Réponse API contenant les données du suivi d'édition

        Returns:
            FollowEditionV1Response: Objet contenant l'entité FollowEdition
        """
        follow_edition = FollowEditionMapper.from_dict(response)
        return FollowEditionV1Response(follow_edition=follow_edition)
