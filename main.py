import os
from typing import List, Dict

from mangacollec_api.client import MangaCollecAPIClient
from mangacollec_api.endpoints.serie_endpoint import SerieEndpointEntity, SerieEndpoint
from mangacollec_api.entity.serie import Serie
from mangacollec_api.interfaces.client.client_interface import IMangaCollecAPIClient


def main():
    clients = init_client()

    # Series
    series_endpoint_anonyme: SerieEndpoint = SerieEndpoint(clients['client_proxy'])

    # Call Serie Api (anonyme)
    #series: List[Serie] = series_endpoint_anonyme.get_all_series_v2()
    #print('\n')
    #print(series[:5])

    # Call Serie item Api
    serie_endpoint_entity: SerieEndpointEntity = series_endpoint_anonyme.get_series_by_id_v2("a320ac19-4318-4471-9e4e-eb017f4584d5")
    serie = serie_endpoint_entity.serie
    print('\n')
    print('id', serie.id)
    print('title', serie.title)
    print('type_id', serie.type_id)
    print('adult_content', serie.adult_content)
    print('editions_count', serie.editions_count)
    print('tasks_count', serie.tasks_count)
    print('kinds_ids', serie.kinds_ids)

    print('kinds', serie_endpoint_entity.kinds)
    print('jobs', serie_endpoint_entity.jobs)
    print('authors', serie_endpoint_entity.authors)
    print('editions', serie_endpoint_entity.editions)
    print('volumes', serie_endpoint_entity.volumes)


    print('EE ', type(serie_endpoint_entity.editions[0]))


def init_client() -> Dict[str, IMangaCollecAPIClient]:
    clients = {
        "client_anonyme" : MangaCollecAPIClient(
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET")
        ),
        "client_proxy" : MangaCollecAPIClient(
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
            proxy={
                "http": "http://51.195.137.60:80"
            }
        ),
        "client_connected" : MangaCollecAPIClient(
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
            email=os.environ.get("USERNAME_DEV"),
            password=os.environ.get("PASSWORD")
        ),
    }

    return clients


if __name__ == '__main__':
    main()