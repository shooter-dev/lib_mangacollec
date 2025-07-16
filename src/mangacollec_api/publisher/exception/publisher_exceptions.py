"""
Exceptions spécifiques au domaine Publisher.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class PublisherError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux éditeurs."""
    pass


class PublisherNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un éditeur demandé est introuvable."""
    
    def __init__(self, publisher_id: str):
        super().__init__(f"Éditeur avec l'ID '{publisher_id}' introuvable.")
        self.publisher_id = publisher_id


class PublisherValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un éditeur."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class PublisherCreationError(PublisherError):
    """Erreur levée lors de la création d'un éditeur."""
    
    def __init__(self, message: str = "Impossible de créer l'éditeur"):
        super().__init__(message)


class PublisherUpdateError(PublisherError):
    """Erreur levée lors de la mise à jour d'un éditeur."""
    
    def __init__(self, publisher_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour l'éditeur avec l'ID '{publisher_id}'"
        super().__init__(message or default_message)
        self.publisher_id = publisher_id


class PublisherDeletionError(PublisherError):
    """Erreur levée lors de la suppression d'un éditeur."""
    
    def __init__(self, publisher_id: str, message: str = None):
        default_message = f"Impossible de supprimer l'éditeur avec l'ID '{publisher_id}'"
        super().__init__(message or default_message)
        self.publisher_id = publisher_id


class PublisherConversionError(PublisherError):
    """Erreur levée lors de la conversion des données d'un éditeur."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class PublisherDuplicateError(PublisherError):
    """Erreur levée lorsqu'un éditeur en double est détecté."""
    
    def __init__(self, publisher_name: str):
        super().__init__(f"L'éditeur '{publisher_name}' existe déjà.")
        self.publisher_name = publisher_name