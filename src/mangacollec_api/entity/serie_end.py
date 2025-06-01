from typing import List

from mangacollec_api.entity.author import Author
from mangacollec_api.entity.box import Box
from mangacollec_api.entity.box_edition import BoxEdition
from mangacollec_api.entity.box_volume import BoxVolume
from mangacollec_api.entity.edition import Edition
from mangacollec_api.entity.genre import Genre
from mangacollec_api.entity.job import Job
from mangacollec_api.entity.kind import Kind
from mangacollec_api.entity.publisher import Publisher
from mangacollec_api.entity.serie import Serie
from mangacollec_api.entity.task import Task
from mangacollec_api.entity.volume import Volume


class SerieEndpointEntity:

    def __init__(self, serie: Serie, type: Genre, kinds: List[Kind], tasks: List[Task], jobs: List[Job], authors: List[Author], editions: List[Edition], publishers: List[Publisher], volumes: List[Volume], box_editions: List[BoxEdition], boxes: List[Box], box_volumes: List[BoxVolume]):
        self.serie: Serie = serie
        self.type: Genre = type
        self.kinds: List[Kind] = kinds
        self.tasks: List[Task] = tasks
        self.jobs: List[Job] = jobs
        self.authors: List[Author] = authors
        self.editions: List[Edition] = editions
        self.publishers: List[Publisher] = publishers
        self.volumes: List[Volume] = volumes
        self.box_editions: List[BoxEdition] = box_editions
        self.boxes: List[Box] = boxes
        self.box_volumes: List[BoxVolume] = box_volumes