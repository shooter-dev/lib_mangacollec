from abc import ABC, abstractmethod
from typing import Any, Dict


class IAuth(ABC):
    """
    Classe responsable de l'authentification OAuth2 auprès de l'API MangaCollec.

    Elle supporte deux modes :
    - grant_type=password (avec email/mot de passe)
    - grant_type=client_credentials (avec client_id/client_secret)
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initialise l'authenticator avec les identifiants client.

        :param client_id: ID client fourni par MangaCollec
        :param client_secret: Secret client fourni par MangaCollec
        :raises ValueError: Si les identifiants sont invalides
        """
        if not client_id or not client_secret:
            raise ValueError("client_id et client_secret sont requis")

        self.client_id = client_id
        self.client_secret = client_secret

    @abstractmethod
    def authenticate_with_password(
        self, username: str, password: str
    ) -> Dict[str, Any]:
        """
        Authentifie l'utilisateur avec email/mot de passe (grant_type=password).

        :param username: Email de l'utilisateur
        :param password: Mot de passe
        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ValueError: Si les paramètres sont invalides
        :raises ConnectionError: Si l'authentification échoue
        """
        pass

    @abstractmethod
    def authenticate_with_client_credentials(self) -> Dict[str, Any]:
        """
        Authentifie via client_id/client_secret uniquement (grant_type=client_credentials).

        :return: Dictionnaire contenant le token d'accès, le refresh token, et autres métadonnées
        :raises ConnectionError: Si l'authentification échoue
        """
        pass
