from typing import List, Dict, Any

from mangacollec_api.author.entity.author import Author
from mangacollec_api.box.entity.box import Box
from mangacollec_api.box.entity.box_volume import BoxVolume
from mangacollec_api.edition.entity.edition import Edition
from mangacollec_api.genre.entity.genre import Genre
from mangacollec_api.job.entity.job import Job
from mangacollec_api.kind.entity.kind import Kind
from mangacollec_api.publisher.entity.publisher import Publisher
from mangacollec_api.serie.entity.serie import Serie
from mangacollec_api.serie.entity.serie_endpoint_entity import SerieEndpointEntity, BoxEdition
from mangacollec_api.task.entity.task import Task
from mangacollec_api.volume.entity.volume import Volume
from mangacollec_api.serie.endpoint.serie_endpoint_interface import ISerieEndpoint


class SerieEndpoint(ISerieEndpoint):
    """
    Classe pour interagir avec l'API MangaCollec concernant les séries.
    """

    ####################
    # V1
    ####################

    def get_all_series(self) -> Dict[str, Any]:
        """
        Récupère la liste complète des séries disponibles sur MangaCollec.

        :return: Liste des séries.
        """
        return self.client.get("/v1/series")

    def get_series_by_id(self, series_id: str) -> Dict[str, Any]:
        """
        Récupère une série spécifique à partir de son ID.

        :param series_id: Identifiant de la série
        :return: Détails de la série.
        """
        return self.client.get(f"/v1/series/{series_id}")

    ####################
    # V2
    ####################

    def get_series_by_id_v2(self, series_id: str) -> SerieEndpointEntity:
        """
        Récupère une série spécifique à partir de son ID.

        :param series_id: Identifiant de la série
        :return: Détails de la série.
        """
        result = self.client.get(f"/v2/series/{series_id}")

        if not result:
            raise ValueError(f"Aucune série trouvée pour l'ID: {series_id}")

        serie = result["series"][0]
        genre = result["types"][0]

        serie_endpoint: SerieEndpointEntity = SerieEndpointEntity(
            serie=Serie(**serie),
            type=Genre(**genre),
            kinds=[Kind(**kind) for kind in result["kinds"]],
            jobs=[Job(**job) for job in result["jobs"]],
            tasks=[Task(**task) for task in result["tasks"]],
            authors=[Author(**author) for author in result["authors"]],
            editions=[Edition(**edition) for edition in result["editions"]],
            publishers=[Publisher(**publisher) for publisher in result["publishers"]],
            volumes=[Volume(**volume) for volume in result["volumes"]],
            box_editions=[
                BoxEdition(**box_edition) for box_edition in result["box_editions"]
            ],
            boxes=[Box(**boxe) for boxe in result["boxes"]],
            box_volumes=[
                BoxVolume(**box_volume) for box_volume in result["box_volumes"]
            ],
        )

        return serie_endpoint

    def get_all_series_v2(self) -> List[Serie]:
        """
        Récupère la liste complète des séries disponibles sur MangaCollec.

        :return: Liste des séries.
        """
        result = self.client.get("/v2/series")

        series: List[Serie] = []

        for serie in result["series"]:
            series.append(
                Serie(
                    id=serie["id"],
                    title=serie["title"],
                    type_id=serie["type_id"],
                    adult_content=serie["adult_content"],
                    editions_count=serie["editions_count"],
                    tasks_count=serie["tasks_count"],
                )
            )

        return series
