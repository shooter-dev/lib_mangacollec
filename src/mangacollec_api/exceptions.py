"""
Définit les exceptions personnalisées pour la bibliothèque MangaCollec API.
"""

class MangaCollecAPIError(Exception):
    """Exception de base pour toutes les erreurs liées à l'API MangaCollec."""
    pass


class AuthenticationError(MangaCollecAPIError):
    """Erreur liée à l'authentification OAuth2 (identifiants invalides, etc.)."""
    pass


class AuthorizationError(MangaCollecAPIError):
    """Erreur en cas de tentative d'accès à une ressource protégée sans autorisation."""
    pass


class NotFoundError(MangaCollecAPIError):
    """Erreur levée lorsqu'une ressource demandée est introuvable."""
    pass


class BadRequestError(MangaCollecAPIError):
    """Erreur levée lorsqu'une requête mal formée est envoyée à l'API."""
    pass


class ServerError(MangaCollecAPIError):
    """Erreur levée lorsqu'un problème côté serveur survient (erreurs 5xx)."""
    pass


class RateLimitExceededError(MangaCollecAPIError):
    """Erreur levée lorsqu'on dépasse la limite de requêtes autorisée par l'API."""
    pass
