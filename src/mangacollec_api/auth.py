"""auth.py - Gestion de l'authentification OAuth2 pour l'API MangaCollec."""

import requests
from typing import Dict, Any

from interfaces.auth.auth_interface import IAuth


class OAuth2Authenticator(IAuth):
    """
    Classe responsable de l'authentification OAuth2 auprès de l'API MangaCollec.

    Elle supporte deux modes :
    - grant_type=password (avec email/mot de passe)
    - grant_type=client_credentials (avec client_id/client_secret)
    """

    TOKEN_URL = "https://api.mangacollec.com/oauth/token"
    DEFAULT_HEADERS = {
        "Accept": "application/json",
        "Accept-language": "fr-FR,fr;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "api.mangacollec.com",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }


    def authenticate_with_password(self, username: str, password: str) -> Dict[str, Any]:
        """
        Authentifie l'utilisateur avec email/mot de passe (grant_type=password).

        :param username: Email de l'utilisateur
        :param password: Mot de passe
        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ValueError: Si les paramètres sont invalides
        :raises ConnectionError: Si l'authentification échoue
        """
        if not username or not password:
            raise ValueError("username et password sont requis")

        payload = {
            "grant_type": "password",
            "username": username,
            "password": password,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        try:
            response = requests.post(self.TOKEN_URL, headers=self.DEFAULT_HEADERS, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise ConnectionError("Identifiants invalides")
            raise ConnectionError(f"Erreur d'authentification: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Erreur de connexion: {str(e)}")

    def authenticate_with_client_credentials(self) -> Dict[str, Any]:
        """
        Authentifie via client_id/client_secret uniquement (grant_type=client_credentials).

        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ConnectionError: Si l'authentification échoue
        """
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        try:
            response = requests.post(self.TOKEN_URL, headers=self.DEFAULT_HEADERS, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise ConnectionError("Identifiants client invalides")
            raise ConnectionError(f"Erreur d'authentification: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Erreur de connexion: {str(e)}")


if __name__ == '__main__':
    # Exemple d'utilisation (à remplacer par des variables d'environnement en production)
    import os
    
    client_id = os.getenv("MANGACOLLEC_CLIENT_ID")
    client_secret = os.getenv("MANGACOLLEC_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("Erreur: MANGACOLLEC_CLIENT_ID et MANGACOLLEC_CLIENT_SECRET doivent être définis")
        exit(1)
        
    auth = OAuth2Authenticator(client_id=client_id, client_secret=client_secret)
    token_data = auth.authenticate_with_client_credentials()
    print(token_data["access_token"])