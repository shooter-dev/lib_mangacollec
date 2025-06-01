from typing import Dict, Any

from mangacollec_api.interfaces.endpoints.kind_endpoint_interface import IKindEndpoint


class KindEndpoint(IKindEndpoint):
    """
    Implémentation des opérations pour les genres de mangas dans l'API MangaCollec.
    """

    def get_all_kinds(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des genres disponibles sur MangaCollec.

        :return: Liste des genres
        """
        return self.client.get("/v1/kinds")

    def get_all_kinds_v2(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des genres disponibles sur MangaCollec.

        :return: Liste des genres
        """
        return self.client.get("/v2/kinds")
