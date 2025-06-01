import datetime
from typing import Dict, List, Optional

from mangacollec_api.interfaces.endpoints.volumes_endpoint_interface import IVolumeEndpoint


class VolumeEndpoint(IVolumeEndpoint):
    """
    Classe responsable de la gestion des volumes via l'API MangaCollec.
    """

    def get_amazon_offer(self, asin: str) -> Dict:
        return self.client.get(f"/v1/amazon_offer/{asin}")

    def get_bd_fugue_offer(self, isbn: str) -> Dict:
        return self.client.get(f"/v1/bdfugue_offer/{isbn}")

    def get_planning_volumes(self, month: Optional[datetime] = None) -> List[Dict]:
        return self.client.get("/v1/planning", dict(month=date.strftime("%Y-%m-%d")))

    def get_planning_volumes_v2(self, month: Optional[datetime] = None) -> List[Dict]:
        return self.client.get("/v2/planning", dict(month=date.strftime("%Y-%m-%d")))

    def get_latest_volumes_news(self) -> List[Dict]:
        return self.client.get("/v1/volumes/news")

    def get_volume_by_id(self, volume_id: str) -> Dict:
        return self.client.get(f"/v1/volumes/{volume_id}")

    def get_volume_by_id_v2(self, volume_id: str) -> Dict:
        return self.client.get(f"/v2/volumes/{volume_id}")

if __name__ == '__main__':
    import os
    from mangacollec_api.client import MangaCollecAPIClient

    client_inv = MangaCollecAPIClient(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET')
    )

    client_dev = MangaCollecAPIClient(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        email=os.environ.get('USERNAME_DEV'),
        password=os.environ.get('PASSWORD'),
    )

    client_prod = MangaCollecAPIClient(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        email=os.environ.get('USERNAME_PROD'),
        password=os.environ.get('PASSWORD'),
    )

    date = datetime.datetime(2024,10,5)

    endpoint = VolumeEndpoint(client_dev)

    print(endpoint.get_planning_volumes(date))

    print(endpoint.get_planning_volumes_v2(date))
    print()
    print()
    print()
    print(endpoint.get_amazon_offer('2380712956'))

    print()
    print(endpoint.get_bd_fugue_offer('9782380712957'))