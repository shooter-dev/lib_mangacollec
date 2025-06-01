import time
import requests
from typing import Optional

from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient


class MangaCollecAPIClient(IMangaCollecAPIClient):
    """
    Client pour interagir avec l'API MangaCollec via OAuth2.
    Prend en charge l'authentification avec client_id/client_secret ou username/password.
    """


    def _authenticate(self):
        """
        Authentifie le client selon les identifiants fournis et initialise le token.
        """
        is_auth: bool = False

        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        if self.email and self.password:
            payload["grant_type"] = "password"
            payload["username"] = self.email
            payload["password"] = self.password

            is_auth = True
        else:
            payload["grant_type"] = "client_credentials"

            is_auth = False

        response = requests.post(self.TOKEN_URL, json=payload)

        response.raise_for_status()

        self.is_auth = is_auth

        data = response.json()

        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.token_expiry = data["created_at"] + data["expires_in"]
        self.refresh_token = data.get("refresh_token")  # peut être None

    def _refresh_access_token(self):
        """
        Rafraîchit le token d'accès à l'aide du refresh_token.
        Fonctionne uniquement si grant_type=password a été utilisé.
        """
        if not self.refresh_token:
            raise RuntimeError("Aucun refresh_token disponible pour rafraîchir le token.")

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        response = requests.post(self.TOKEN_URL, data=payload)
        response.raise_for_status()

        data = response.json()

        self.access_token = data["access_token"]
        self.token_type = data["token_type"]
        self.token_expiry = data["created_at"] + data["expires_in"]
        self.refresh_token = data.get("refresh_token")

    def _ensure_token_valid(self):
        """
        Vérifie la validité du token. Le rafraîchit si expiré et possible.
        """
        if not self.token_expiry or time.time() < self.token_expiry - 60:
            return

        if self.refresh_token:
            self._refresh_access_token()
            return

        self._authenticate()

    def _call_request(self, method: str, endpoint: str, **kwargs):
        """
        Effectue une requête HTTP authentifiée.
        """
        self._ensure_token_valid()

        headers = kwargs.pop("headers", {})

        headers["Authorization"] = f"{self.token_type} {self.access_token}"

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.request(method=method, url=url, headers=headers, proxies=None, **kwargs)

        response.raise_for_status()

        return response.json()

    def get(self, endpoint: str, params: Optional[dict] = None):
        """
        Effectue une requête GET vers l'API.
        """
        return self._call_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[dict] = None):
        """
        Effectue une requête POST vers l'API.
        """
        return self._call_request("POST", endpoint, json=data)

    def delete(self, endpoint: str):
        """
        Effectue une requête DELETE vers l'API.
        """
        return self._call_request("DELETE", endpoint)
