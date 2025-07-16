"""
Exceptions spécifiques au domaine Genre.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class GenreError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux genres."""
    pass


class GenreNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un genre demandé est introuvable."""
    
    def __init__(self, genre_id: str):
        super().__init__(f"Genre avec l'ID '{genre_id}' introuvable.")
        self.genre_id = genre_id


class GenreValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un genre."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class GenreCreationError(GenreError):
    """Erreur levée lors de la création d'un genre."""
    
    def __init__(self, message: str = "Impossible de créer le genre"):
        super().__init__(message)


class GenreUpdateError(GenreError):
    """Erreur levée lors de la mise à jour d'un genre."""
    
    def __init__(self, genre_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour le genre avec l'ID '{genre_id}'"
        super().__init__(message or default_message)
        self.genre_id = genre_id


class GenreDeletionError(GenreError):
    """Erreur levée lors de la suppression d'un genre."""
    
    def __init__(self, genre_id: str, message: str = None):
        default_message = f"Impossible de supprimer le genre avec l'ID '{genre_id}'"
        super().__init__(message or default_message)
        self.genre_id = genre_id


class GenreConversionError(GenreError):
    """Erreur levée lors de la conversion des données d'un genre."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class GenreDuplicateError(GenreError):
    """Erreur levée lorsqu'un genre en double est détecté."""
    
    def __init__(self, genre_name: str):
        super().__init__(f"Le genre '{genre_name}' existe déjà.")
        self.genre_name = genre_name