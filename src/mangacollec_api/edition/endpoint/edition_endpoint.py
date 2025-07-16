from typing import Dict

from mangacollec_api.edition.endpoint.edition_endpoint_interface import (
    IEditionEndpoint,
)


class EditionEndpoint(IEditionEndpoint):
    """
    Classe responsable de la gestion des editions via l'API MangaCollec.
    """

    def get_edition_by_id(self, edition_id: str) -> Dict:
        return self.client.get(f"/v1/editions/{edition_id}")

    def get_edition_by_id_v2(self, edition_id: str) -> Dict:
        return self.client.get(f"/v2/editions/{edition_id}")
