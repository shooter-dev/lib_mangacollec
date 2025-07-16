"""
Exceptions spécifiques au domaine User.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class AuthenticationError(MangaCollecAPIError):
    """Erreur levée lors de l'authentification."""
    pass


class UserError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux utilisateurs."""
    pass


class UserNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un utilisateur demandé est introuvable."""
    
    def __init__(self, user_id: str):
        super().__init__(f"Utilisateur avec l'ID '{user_id}' introuvable.")
        self.user_id = user_id


class UserValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un utilisateur."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class UserCreationError(UserError):
    """Erreur levée lors de la création d'un utilisateur."""
    
    def __init__(self, message: str = "Impossible de créer l'utilisateur"):
        super().__init__(message)


class UserUpdateError(UserError):
    """Erreur levée lors de la mise à jour d'un utilisateur."""
    
    def __init__(self, user_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour l'utilisateur avec l'ID '{user_id}'"
        super().__init__(message or default_message)
        self.user_id = user_id


class UserDeletionError(UserError):
    """Erreur levée lors de la suppression d'un utilisateur."""
    
    def __init__(self, user_id: str, message: str = None):
        default_message = f"Impossible de supprimer l'utilisateur avec l'ID '{user_id}'"
        super().__init__(message or default_message)
        self.user_id = user_id


class UserConversionError(UserError):
    """Erreur levée lors de la conversion des données d'un utilisateur."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class UserAuthenticationError(AuthenticationError):
    """Erreur levée lors de l'authentification d'un utilisateur."""
    
    def __init__(self, username: str, message: str = None):
        default_message = f"Impossible d'authentifier l'utilisateur '{username}'"
        super().__init__(message or default_message)
        self.username = username


class UserPermissionError(UserError):
    """Erreur levée lorsqu'un utilisateur n'a pas les permissions nécessaires."""
    
    def __init__(self, user_id: str, required_permission: str):
        message = f"L'utilisateur '{user_id}' n'a pas la permission '{required_permission}'"
        super().__init__(message)
        self.user_id = user_id
        self.required_permission = required_permission


class UserDuplicateError(UserError):
    """Erreur levée lorsqu'un utilisateur en double est détecté."""
    
    def __init__(self, username: str):
        super().__init__(f"L'utilisateur '{username}' existe déjà.")
        self.username = username