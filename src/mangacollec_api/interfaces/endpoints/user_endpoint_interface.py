from abc import abstractmethod
from typing import List, Dict

from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient
from mangacollec_api.interfaces.endpoints.endpoint_interface import IEndpoint


class IUserEndpoint(IEndpoint):
    """
    Interface responsable de la gestion des users via l'API MangaCollec.
    """
    def __init__(self, client: IMangaCollecAPIClient):
        super().__init__(client)
        if self.client.is_auth:
            info = self.get_info_user()
            self.client.username = info['username']
            print('username : ', self.client.username)
        else:
            print('session invité')


    @abstractmethod
    def get_info_user(self) -> Dict:
        """
        Récupère les information de l'utilisateur connecté.

        :return: les information de l'utilisateur connecté.
        """
        pass


    @abstractmethod
    def get_recommendation(self) -> Dict:
        """
        Récupère les recommendation de l'utilisateur connecté.

        :return: les recommendation de l'utilisateur connecté.
        """
        pass


    @abstractmethod
    def get_native_planning(self) -> Dict:
        """


        :return:
        """
        pass


    @abstractmethod
    def get_collection_by_username(self, username: str) -> List[Dict]:
        """
        Récupère la collection de l'utilisateur public.

        :return: Liste des volumes récents
        """
        pass


    @abstractmethod
    def get_collection_by_username_v2(self, username: str) -> List[Dict]:
        """
        Récupère la collection de l'utilisateur public.

        :return: Liste des volumes récents
        """
        pass


    @abstractmethod
    def get_collection(self) -> List[Dict]:
        """
        Récupère la collection de l'utilisateur (auth).

        :return: Liste des volumes récents
        """
        pass


    @abstractmethod
    def get_collection_v2(self) -> List[Dict]:
        """
        Récupère la collection de l'utilisateur (auth).

        :return: Liste des volumes récents
        """
        pass