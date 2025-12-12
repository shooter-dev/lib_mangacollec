"""Exceptions spécifiques aux Volumes.

This module defines custom exceptions for Volume entities.
"""

from mangacollec.domain.exceptions.base_exceptions import MangacollecException


class VolumeNotFoundException(MangacollecException):
    """Exception levée quand un volume n'est pas trouvé."""

    def __init__(self, volume_id: str) -> None:
        """Initialise l'exception avec l'ID du volume.

        Args:
            volume_id: UUID du volume non trouvé
        """
        self.volume_id = volume_id
        super().__init__(f"Volume with ID '{volume_id}' not found.")
