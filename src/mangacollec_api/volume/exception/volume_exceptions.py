"""
Exceptions spécifiques au domaine Volume.
"""


class MangaCollecAPIError(Exception):
    """Exception de base pour toutes les erreurs liées à l'API MangaCollec."""
    pass


class NotFoundError(MangaCollecAPIError):
    """Erreur levée lorsqu'une ressource demandée est introuvable."""
    pass


class BadRequestError(MangaCollecAPIError):
    """Erreur levée lorsqu'une requête mal formée est envoyée à l'API."""
    pass


class VolumeError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux volumes."""
    pass


class VolumeNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un volume demandé est introuvable."""
    
    def __init__(self, volume_id: str):
        super().__init__(f"Volume avec l'ID '{volume_id}' introuvable.")
        self.volume_id = volume_id


class VolumeValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un volume."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class VolumeCreationError(VolumeError):
    """Erreur levée lors de la création d'un volume."""
    
    def __init__(self, message: str = "Impossible de créer le volume"):
        super().__init__(message)


class VolumeUpdateError(VolumeError):
    """Erreur levée lors de la mise à jour d'un volume."""
    
    def __init__(self, volume_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour le volume avec l'ID '{volume_id}'"
        super().__init__(message or default_message)
        self.volume_id = volume_id


class VolumeDeletionError(VolumeError):
    """Erreur levée lors de la suppression d'un volume."""
    
    def __init__(self, volume_id: str, message: str = None):
        default_message = f"Impossible de supprimer le volume avec l'ID '{volume_id}'"
        super().__init__(message or default_message)
        self.volume_id = volume_id


class VolumeConversionError(VolumeError):
    """Erreur levée lors de la conversion des données d'un volume."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class VolumeOrderError(VolumeError):
    """Erreur levée lorsqu'un numéro de volume est invalide."""
    
    def __init__(self, volume_number: int, message: str = None):
        default_message = f"Numéro de volume invalide: {volume_number}"
        super().__init__(message or default_message)
        self.volume_number = volume_number


class VolumeAvailabilityError(VolumeError):
    """Erreur levée lorsqu'un volume n'est pas disponible."""
    
    def __init__(self, volume_id: str, message: str = None):
        default_message = f"Volume '{volume_id}' non disponible"
        super().__init__(message or default_message)
        self.volume_id = volume_id