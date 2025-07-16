"""
Exceptions spécifiques au domaine Edition.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class EditionError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux éditions."""
    pass


class EditionNotFoundError(NotFoundError):
    """Erreur levée lorsqu'une édition demandée est introuvable."""
    
    def __init__(self, edition_id: str):
        super().__init__(f"Édition avec l'ID '{edition_id}' introuvable.")
        self.edition_id = edition_id


class EditionValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'une édition."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class EditionCreationError(EditionError):
    """Erreur levée lors de la création d'une édition."""
    
    def __init__(self, message: str = "Impossible de créer l'édition"):
        super().__init__(message)


class EditionUpdateError(EditionError):
    """Erreur levée lors de la mise à jour d'une édition."""
    
    def __init__(self, edition_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour l'édition avec l'ID '{edition_id}'"
        super().__init__(message or default_message)
        self.edition_id = edition_id


class EditionDeletionError(EditionError):
    """Erreur levée lors de la suppression d'une édition."""
    
    def __init__(self, edition_id: str, message: str = None):
        default_message = f"Impossible de supprimer l'édition avec l'ID '{edition_id}'"
        super().__init__(message or default_message)
        self.edition_id = edition_id


class EditionConversionError(EditionError):
    """Erreur levée lors de la conversion des données d'une édition."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class EditionAvailabilityError(EditionError):
    """Erreur levée lorsqu'une édition n'est pas disponible."""
    
    def __init__(self, edition_id: str, message: str = None):
        default_message = f"Édition '{edition_id}' non disponible"
        super().__init__(message or default_message)
        self.edition_id = edition_id