from abc import ABC

from mangacollec_api.client.client_interface import IMangaCollecAPIClient


class IEndpoint(ABC):
    """
    Initialise l'accès aux endpoints.

    :param client: Instance du client API authentifié
    """

    def __init__(self, client: IMangaCollecAPIClient):
        self.client = client
