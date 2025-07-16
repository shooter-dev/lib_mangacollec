"""
Exceptions spécifiques au domaine Author.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class AuthorError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux auteurs."""
    pass


class AuthorNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un auteur demandé est introuvable."""
    
    def __init__(self, author_id: str):
        super().__init__(f"Auteur avec l'ID '{author_id}' introuvable.")
        self.author_id = author_id


class AuthorValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un auteur."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class AuthorCreationError(AuthorError):
    """Erreur levée lors de la création d'un auteur."""
    
    def __init__(self, message: str = "Impossible de créer l'auteur"):
        super().__init__(message)


class AuthorUpdateError(AuthorError):
    """Erreur levée lors de la mise à jour d'un auteur."""
    
    def __init__(self, author_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour l'auteur avec l'ID '{author_id}'"
        super().__init__(message or default_message)
        self.author_id = author_id


class AuthorDeletionError(AuthorError):
    """Erreur levée lors de la suppression d'un auteur."""
    
    def __init__(self, author_id: str, message: str = None):
        default_message = f"Impossible de supprimer l'auteur avec l'ID '{author_id}'"
        super().__init__(message or default_message)
        self.author_id = author_id


class AuthorConversionError(AuthorError):
    """Erreur levée lors de la conversion des données d'un auteur."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data