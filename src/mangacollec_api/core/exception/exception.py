class MangaCollecAPIError(Exception):
    """Exception de base pour toutes les erreurs liées à l'API MangaCollec."""
    pass


class NotFoundError(MangaCollecAPIError):
    """Erreur levée lorsqu'une ressource demandée est introuvable."""
    pass


class BadRequestError(MangaCollecAPIError):
    """Erreur levée lorsqu'une requête mal formée est envoyée à l'API."""
    pass