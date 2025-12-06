from abc import ABC, abstractmethod

from src.domain.entities import ClientMangaCollec


class IMangaCollecAPI(ABC):
    """Interface pour le client MangaCollec API.

    Prend en charge l'authentification avec client_id/client_secret ou username/password.

    Interface for the MangaCollec API client. Supports authentication with client_id/client_secret or username/password.
    """

    BASE_URL: str = "https://api.mangacollec.com/"
    TOKEN_URL: str = f"{BASE_URL}oauth/token/"

    def __init__(self, client: ClientMangaCollec, proxy: dict[str, str] | None = None) -> None:
        self.client = client

        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.token_type: str | None = None
        self.token_expiry: int | None = None

        self.proxy: dict[str, str] | None = proxy
        self.is_auth: bool = False
        self.is_premium: bool = False
        self.username: str = ""

        self._authenticate()

    @abstractmethod
    def _authenticate(self) -> None:
        """Authentifie le client selon les identifiants fournis et initialise le token."""

    @abstractmethod
    def _refresh_access_token(self) -> None:
        """Rafraîchit le token d'accès à l'aide du refresh_token.

        Fonctionne uniquement si grant_type=password a été utilisé.
        """

    @abstractmethod
    def _ensure_token_valid(self) -> None:
        """Vérifie la validité du token. Le rafraîchit si expiré et possible.

        Check token validity. Refresh it if expired and possible.
        """

    @abstractmethod
    def _call_request(self, method: str, endpoint: str, **kwargs) -> dict | list:
        """Effectue une requête HTTP authentifiée.

        Make an authenticated HTTP request.
        """

    @abstractmethod
    def get(self, endpoint: str, params: dict | None = None) -> dict | list:
        """Effectue une requête GET vers l'API.

        Make a GET request to the API.
        """

    @abstractmethod
    def post(self, endpoint: str, data: dict | None = None) -> dict | list:
        """Effectue une requête POST vers l'API.

        Make a POST request to the API.
        """

    @abstractmethod
    def delete(self, endpoint: str) -> dict | list:
        """Effectue une requête DELETE vers l'API.

        Make a DELETE request to the API.
        """

    @classmethod
    @abstractmethod
    def reset(cls) -> None:
        """Réinitialise l'instance singleton du client. Utilisé principalement pour les tests unitaires.

        Resets the singleton instance of the client. Used primarily for unit tests.
        """
