"""
Exceptions spécifiques au domaine Job.
"""
from mangacollec_api.core.exception.exception import MangaCollecAPIError, NotFoundError, BadRequestError


class JobError(MangaCollecAPIError):
    """Exception de base pour toutes les erreurs liées aux jobs."""
    pass


class JobNotFoundError(NotFoundError):
    """Erreur levée lorsqu'un job demandé est introuvable."""
    
    def __init__(self, job_id: str):
        super().__init__(f"Job avec l'ID '{job_id}' introuvable.")
        self.job_id = job_id


class JobValidationError(BadRequestError):
    """Erreur levée lors de la validation des données d'un job."""
    
    def __init__(self, field: str, value: str, message: str = None):
        default_message = f"Valeur invalide pour le champ '{field}': {value}"
        super().__init__(message or default_message)
        self.field = field
        self.value = value


class JobCreationError(JobError):
    """Erreur levée lors de la création d'un job."""
    
    def __init__(self, message: str = "Impossible de créer le job"):
        super().__init__(message)


class JobUpdateError(JobError):
    """Erreur levée lors de la mise à jour d'un job."""
    
    def __init__(self, job_id: str, message: str = None):
        default_message = f"Impossible de mettre à jour le job avec l'ID '{job_id}'"
        super().__init__(message or default_message)
        self.job_id = job_id


class JobDeletionError(JobError):
    """Erreur levée lors de la suppression d'un job."""
    
    def __init__(self, job_id: str, message: str = None):
        default_message = f"Impossible de supprimer le job avec l'ID '{job_id}'"
        super().__init__(message or default_message)
        self.job_id = job_id


class JobConversionError(JobError):
    """Erreur levée lors de la conversion des données d'un job."""
    
    def __init__(self, data: dict, message: str = None):
        default_message = f"Impossible de convertir les données: {data}"
        super().__init__(message or default_message)
        self.data = data


class JobExecutionError(JobError):
    """Erreur levée lors de l'exécution d'un job."""
    
    def __init__(self, job_id: str, message: str = None):
        default_message = f"Erreur lors de l'exécution du job '{job_id}'"
        super().__init__(message or default_message)
        self.job_id = job_id


class JobStatusError(JobError):
    """Erreur levée lorsqu'une opération est tentée sur un job avec un statut incompatible."""
    
    def __init__(self, job_id: str, current_status: str, expected_status: str):
        message = f"Job '{job_id}' a le statut '{current_status}', mais '{expected_status}' attendu"
        super().__init__(message)
        self.job_id = job_id
        self.current_status = current_status
        self.expected_status = expected_status