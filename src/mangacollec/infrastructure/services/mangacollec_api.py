import logging
import time

import requests

from mangacollec.application.interfaces.mangacollec_api_interface import IMangaCollecAPI
from mangacollec.domain.entities import ClientMangaCollec

logger = logging.getLogger(__name__)


class MangaCollecAPI(IMangaCollecAPI):

    def __init__(self, client: ClientMangaCollec, proxy: dict[str, str] | None = None) -> None:

        # Créer la session avant l'appel au parent pour qu'elle soit disponible dans _authenticate
        self._session = requests.Session()
        super().__init__(client, proxy)

    def _authenticate(self) -> None:
        """Authentifie le client selon les identifiants fournis et initialise le token.

        Authenticate the client according to provided credentials and initialize the token.
        """
        is_auth: bool = False

        payload = {
            "client_id": self.client.client_id,
            "client_secret": self.client.client_secret,
        }

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        if self.client.username and self.client.password:
            payload["grant_type"] = "password"
            payload["username"] = self.client.username
            payload["password"] = self.client.password
            is_auth = True
        else:
            payload["grant_type"] = "client_credentials"
            is_auth = False

        logger.info(f"Tentative d'authentification - Mode: {'password' if is_auth else 'client_credentials'}")

        try:
            response = self._session.post(self.TOKEN_URL, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error("Échec de l'authentification: %s", e)
            raise

        self.is_auth = is_auth

        data = response.json()

        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.token_expiry = data["created_at"] + data["expires_in"]
        self.refresh_token = data.get("refresh_token")

        logger.info("Authentification réussie")

    def _refresh_access_token(self) -> None:
        """Rafraîchit le token d'accès à l'aide du refresh_token. Fonctionne uniquement si grant_type=password a été
        utilisé.

        Refresh the access token using the refresh_token. Only works if grant_type=password was used.
        """
        if not self.refresh_token:
            logger.error("Aucun refresh_token disponible pour rafraîchir le token.")
            raise RuntimeError("Aucun refresh_token disponible pour rafraîchir le token.")

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client.client_id,
            "client_secret": self.client.client_secret,
        }

        logger.info("Tentative de rafraîchissement du token")

        try:
            response = self._session.post(self.TOKEN_URL, data=payload, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error("Échec du rafraîchissement du token: %s", e)
            raise

        data = response.json()

        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.token_expiry = data["created_at"] + data["expires_in"]
        self.refresh_token = data.get("refresh_token")

        logger.info("Token rafraîchi avec succès")

    def _ensure_token_valid(self) -> None:
        """Vérifie la validité du token. Le rafraîchit si expiré et possible.

        Check token validity. Refresh it if expired and possible.
        """
        if not self.token_expiry or time.time() < self.token_expiry - 60:
            return

        logger.warning("Token expiré, tentative de rafraîchissement")

        if self.refresh_token and self.is_auth:
            try:
                self._refresh_access_token()
                return
            except Exception as e:
                logger.warning("Échec du rafraîchissement: %s", e)

        # Fallback sur nouvelle authentification
        self._authenticate()

    def _call_request(self, method: str, endpoint: str, **kwargs) -> dict | list:
        """Effectue une requête HTTP authentifiée.

        Make an authenticated HTTP request.
        """
        self._ensure_token_valid()

        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"{self.token_type} {self.access_token}"
        headers["Accept"] = "application/json"

        # Gérer correctement les slashes pour éviter les doubles slashes
        base_url = self.BASE_URL.rstrip("/")
        endpoint_clean = endpoint.lstrip("/")
        url = f"{base_url}/{endpoint_clean}"

        logger.debug("Requête %s %s", method, url)

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers,
                proxies=self.proxy,
                timeout=30,
                **kwargs,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Échec de la requête %s %s: %s", method, url, e)
            raise

    def get(self, endpoint: str, params: dict | None = None) -> dict | list:
        """Effectue une requête GET vers l'API.

        Make a GET request to the API.
        """
        return self._call_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: dict | None = None) -> dict | list:
        """Effectue une requête POST vers l'API.

        Make a POST request to the API.
        """
        return self._call_request("POST", endpoint, json=data)

    def delete(self, endpoint: str) -> dict | list:
        """Effectue une requête DELETE vers l'API.

        Make a DELETE request to the API.
        """
        return self._call_request("DELETE", endpoint)

    @classmethod
    def reset(cls) -> None:
        """Réinitialise l'instance singleton du client. Utilisé principalement pour les tests unitaires.

        Resets the singleton instance of the client. Used primarily for unit tests.
        """
        cls._instance = None
        cls._initialized = False
