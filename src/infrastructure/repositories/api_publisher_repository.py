import requests

from src.application.dto.responses.get_all_publishers_v2_response import GetAllPublishersV2Response
from src.application.dto.responses.get_publisher_by_id_v2_response import GetPublisherByIdV2Response
from src.application.mappers.box_edition_mapper import BoxEditionMapper
from src.application.mappers.box_mapper import BoxMapper
from src.application.mappers.edition_mapper import EditionMapper
from src.application.mappers.publisher_mapper import PublisherMapper
from src.application.mappers.serie_mapper import SerieMapper
from src.application.mappers.type_serie_mapper import TypeSerieMapper
from src.application.mappers.volume_mapper import VolumeMapper
from src.domain.execptions.publisher_exceptions import PublisherNotFoundException
from src.domain.repositories.i_publisher_repository import IPublisherRepository


class ApiPublisherRepository(IPublisherRepository):
    def __init__(self, base_url: str = "https://api.mangacollec.com"):
        self.base_url = base_url

    def get_all_v2(self) -> GetAllPublishersV2Response:
        response = requests.get(f"{self.base_url}/v2/publishers")
        response.raise_for_status()
        data = response.json()
        publishers = [PublisherMapper.from_dict(item) for item in data["publishers"]]
        return GetAllPublishersV2Response(publishers=publishers)

    def get_by_id_v2(self, publisher_id: str) -> GetPublisherByIdV2Response:
        response = requests.get(f"{self.base_url}/v2/publishers/{publisher_id}")
        if response.status_code == 404:
            raise PublisherNotFoundException(publisher_id)
        response.raise_for_status()
        data = response.json()

        publishers = [PublisherMapper.from_dict(p) for p in data.get("publishers", [])]
        editions = [EditionMapper.from_dict(e) for e in data.get("editions", [])]
        box_editions = [BoxEditionMapper.from_dict(be) for be in data.get("box_editions", [])]
        series = [SerieMapper.from_dict(s) for s in data.get("series", [])]
        types = [TypeSerieMapper.from_dict(t) for t in data.get("types", [])]
        volumes = [VolumeMapper.from_dict(v) for v in data.get("volumes", [])]
        boxes = [BoxMapper.from_dict(b) for b in data.get("boxes", [])]

        return GetPublisherByIdV2Response(
            publishers=publishers,
            editions=editions,
            box_editions=box_editions,
            series=series,
            types=types,
            volumes=volumes,
            boxes=boxes,
        )
