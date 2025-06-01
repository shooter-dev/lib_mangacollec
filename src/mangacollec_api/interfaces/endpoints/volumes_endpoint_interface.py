from abc import abstractmethod
from datetime import datetime
from typing import List, Dict, Optional

from mangacollec_api.interfaces.endpoints.endpoint_interface import IEndpoint


class IVolumeEndpoint(IEndpoint):
    """
    Interface responsable de la gestion des volumes via l'API MangaCollec.
    """

    @abstractmethod
    def get_planning_volumes(self, month: Optional[datetime] = None) -> List[Dict]:
        """
        Récupère les volumes du planning current ou via une date.

        :return: Liste des volumes de planning
        """
        pass

    @abstractmethod
    def get_planning_volumes_v2(self, month: Optional[datetime] = None) -> List[Dict]:
        """
        Récupère les volumes du planning current ou via une date.

        :return: Liste des volumes de planning
        """
        pass

    @abstractmethod
    def get_latest_volumes_news(self) -> List[Dict]:
        """
        Récupère les volumes les plus récents (actualités).

        :return: Liste des volumes récents
        """
        pass

    @abstractmethod
    def get_volume_by_id(self, volume_id: str) -> Dict:
        """
        Récupère les informations d'un volume spécifique en utilisant son ID.

        :param volume_id: Identifiant du volume
        :return: Détails du volume demandé.
        """
        pass

    @abstractmethod
    def get_volume_by_id_v2(self, volume_id: str) -> Dict:
        """
        Récupère les informations d'un volume spécifique en utilisant son ID.

        :param volume_id: Identifiant du volume
        :return: Détails du volume demandé.
        """
        pass

    @abstractmethod
    def get_amazon_offer(self, asin: str) -> Dict:
        """

        :param asind: Identifiant amazone du volume
        :return: Détails du volume demandé.
        """
        pass

    @abstractmethod
    def get_bd_fugue_offer(self, isbn: str) -> Dict:
        """

        :param isbn: Identifiant bd fugue du volume
        :return: Détails du volume demandé.
        """
        pass