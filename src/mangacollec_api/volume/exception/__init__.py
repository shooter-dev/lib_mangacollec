"""
Exceptions du domaine Volume.
"""

from .volume_exceptions import (
    VolumeError,
    VolumeNotFoundError,
    VolumeValidationError,
    VolumeCreationError,
    VolumeUpdateError,
    VolumeDeletionError,
    VolumeConversionError,
    VolumeOrderError,
    VolumeAvailabilityError,
)

__all__ = [
    "VolumeError",
    "VolumeNotFoundError",
    "VolumeValidationError",
    "VolumeCreationError",
    "VolumeUpdateError",
    "VolumeDeletionError",
    "VolumeConversionError",
    "VolumeOrderError",
    "VolumeAvailabilityError",
]