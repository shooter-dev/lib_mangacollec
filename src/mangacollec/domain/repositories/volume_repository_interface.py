"""Interface du repository pour les Volumes.

This module defines the repository interface for Volume entities.
"""

from abc import ABC, abstractmethod

from mangacollec.application.dto import (GetVolumeByIdV2Response,
                                         GetVolumesNewsV2Response)


class IVolumeRepository(ABC):
    """Interface du repository pour Volume."""

    @abstractmethod
    def get_by_id_v2(self, volume_id: str) -> GetVolumeByIdV2Response:
        """Récupère un volume par son ID avec toutes ses relations via l'API V2.

        Args:
            volume_id: UUID du volume

        Returns:
            GetVolumeByIdV2Response contenant le volume et ses relations

        Raises:
            VolumeNotFoundException: Si le volume n'existe pas
        """
        pass

    @abstractmethod
    def get_volumes_news_v2(self) -> GetVolumesNewsV2Response:
        """Récupère les volumes récents avec publicité native via l'API V2.

        Returns:
            GetVolumesNewsV2Response contenant les volumes récents et la publicité native

        Raises:
            RuntimeError: Si une erreur survient lors de la récupération
        """
        pass
