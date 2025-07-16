"""
Exceptions spécifiques au domaine Serie.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class SerieError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux séries."""
    pass


class SerieNotFoundError(NotFoundError):
    """Erreur levée lorsqu'une série demandée est introuvable."""
    
    def __init__(self, serie_id: str):
        super().__init__(f"Série avec l'ID '{serie_id}' introuvable.")
        self.serie_id = serie_id


class SerieValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'une série."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class SerieCreationError(SerieError):
    """Erreur levée lors de la création d'une série."""
    
    def __init__(self, message: str = "Impossible de créer la série"):
        super().__init__(message)


class SerieUpdateError(SerieError):
    """Erreur levée lors de la mise à jour d'une série."""
    
    def __init__(self, serie_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour la série avec l'ID '{serie_id}'"
        super().__init__(message or default_message)
        self.serie_id = serie_id


class SerieDeletionError(SerieError):
    """Erreur levée lors de la suppression d'une série."""
    
    def __init__(self, serie_id: str, message: str = None):
        default_message = f"Impossible de supprimer la série avec l'ID '{serie_id}'"
        super().__init__(message or default_message)
        self.serie_id = serie_id


class SerieConversionError(SerieError):
    """Erreur levée lors de la conversion des données d'une série."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class SerieStatusError(SerieError):
    """Erreur levée lorsqu'une opération est tentée sur une série avec un statut incompatible."""
    
    def __init__(self, serie_id: str, current_status: str, expected_status: str):
        message = f"Série '{serie_id}' a le statut '{current_status}', mais '{expected_status}' attendu"
        super().__init__(message)
        self.serie_id = serie_id
        self.current_status = current_status
        self.expected_status = expected_status