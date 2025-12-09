from abc import ABC, abstractmethod

from mangacollec.application.dto.responses.get_all_publishers_v2_response import GetAllPublishersV2Response
from mangacollec.application.dto.responses.get_publisher_by_id_v2_response import GetPublisherByIdV2Response


class IPublisherRepository(ABC):
    @abstractmethod
    def get_all_v2(self) -> GetAllPublishersV2Response:
        pass

    @abstractmethod
    def get_by_id_v2(self, publisher_id: str) -> GetPublisherByIdV2Response:
        pass
