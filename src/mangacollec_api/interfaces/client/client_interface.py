from abc import ABC, abstractmethod
from typing import Optional, Dict, List


class IMangaCollecAPIClient(ABC):
    """
    Client pour interagir avec l'API MangaCollec via OAuth2.
    Prend en charge l'authentification avec client_id/client_secret ou username/password.
    """

    TOKEN_URL: str = "https://api.mangacollec.com/oauth/token/"
    BASE_URL: str = "https://api.mangacollec.com/"

    def __init__(self, client_id: str, client_secret: str, email: Optional[str] = None, password: Optional[str] = None, proxy: Optional[Dict] = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.email = email
        self.password = password

        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.token_type: Optional[str] = None
        self.token_expiry: Optional[int] = None

        self.proxy: Dict = proxy

        self.is_auth: bool = False
        self.is_premium: bool = False

        self.username: str = ''

        self._authenticate()

    @abstractmethod
    def _authenticate(self) -> None:
        """
        Authentifie le client selon les identifiants fournis et initialise le token.
        """
        pass

    @abstractmethod
    def _refresh_access_token(self) -> None:
        """
        Rafraîchit le token d'accès à l'aide du refresh_token.
        Fonctionne uniquement si grant_type=password a été utilisé.
        """
        pass

    @abstractmethod
    def _ensure_token_valid(self):
        """
        Vérifie la validité du token. Le rafraîchit si expiré et possible.
        """
        pass

    @abstractmethod
    def _call_request(self, method: str, endpoint: str, **kwargs):
        """
        Effectue une requête HTTP authentifiée.
        """
        pass

    @abstractmethod
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict | List]:
        """
        Effectue une requête GET vers l'API.
        """
        pass

    @abstractmethod
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Optional[Dict | List]:
        """
        Effectue une requête POST vers l'API.
        """
        pass

    @abstractmethod
    def delete(self, endpoint: str) -> Optional[Dict | List]:
        """
        Effectue une requête DELETE vers l'API.
        """
        pass