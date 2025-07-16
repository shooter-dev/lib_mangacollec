"""
Exceptions spécifiques au domaine Kind.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class KindError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux kinds (types)."""
    pass


class KindNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un kind demandé est introuvable."""
    
    def __init__(self, kind_id: str):
        super().__init__(f"Kind avec l'ID '{kind_id}' introuvable.")
        self.kind_id = kind_id


class KindValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un kind."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class KindCreationError(KindError):
    """Erreur levée lors de la création d'un kind."""
    
    def __init__(self, message: str = "Impossible de créer le kind"):
        super().__init__(message)


class KindUpdateError(KindError):
    """Erreur levée lors de la mise à jour d'un kind."""
    
    def __init__(self, kind_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour le kind avec l'ID '{kind_id}'"
        super().__init__(message or default_message)
        self.kind_id = kind_id


class KindDeletionError(KindError):
    """Erreur levée lors de la suppression d'un kind."""
    
    def __init__(self, kind_id: str, message: str = None):
        default_message = f"Impossible de supprimer le kind avec l'ID '{kind_id}'"
        super().__init__(message or default_message)
        self.kind_id = kind_id


class KindConversionError(KindError):
    """Erreur levée lors de la conversion des données d'un kind."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class KindTypeError(KindError):
    """Erreur levée lorsqu'un type de kind n'est pas supporté."""
    
    def __init__(self, kind_type: str):
        super().__init__(f"Type de kind '{kind_type}' non supporté.")
        self.kind_type = kind_type