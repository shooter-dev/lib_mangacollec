"""Cas d'utilisation pour les Volumes.

This module contains use cases for Volume operations.
"""

from mangacollec.application.dto import (GetVolumeByIdV2Response,
                                         GetVolumesNewsV2Response)
from mangacollec.domain.repositories import IVolumeRepository


class GetVolumeByIdV2UseCase:
    """Cas d'utilisation pour récupérer un volume par son ID avec toutes ses relations."""

    def __init__(self, repository: IVolumeRepository) -> None:
        """Initialise le use case avec le repository.

        Args:
            repository: Repository pour les volumes
        """
        self.repository = repository

    def __call__(self, volume_id: str) -> GetVolumeByIdV2Response:
        """Récupère un volume par son ID.

        Args:
            volume_id: UUID du volume

        Returns:
            GetVolumeByIdV2Response contenant le volume et ses relations

        Raises:
            VolumeNotFoundException: Si le volume n'existe pas
        """
        return self.repository.get_by_id_v2(volume_id)


class GetVolumesNewsV2UseCase:
    """Cas d'utilisation pour récupérer les volumes récents avec publicité native."""

    def __init__(self, repository: IVolumeRepository) -> None:
        """Initialise le use case avec le repository.

        Args:
            repository: Repository pour les volumes
        """
        self.repository = repository

    def __call__(self) -> GetVolumesNewsV2Response:
        """Récupère les volumes récents.

        Returns:
            GetVolumesNewsV2Response contenant les volumes récents et la publicité native

        Raises:
            RuntimeError: Si une erreur survient lors de la récupération
        """
        return self.repository.get_volumes_news_v2()
