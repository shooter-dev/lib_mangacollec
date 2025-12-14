"""Publisher use cases."""

from mangacollec.domain.entities import (
    Box,
    BoxEdition,
    Edition,
    Publisher,
    PublisherListItem,
    Serie,
    TypeSerie,
    Volume,
)
from mangacollec.domain.repositories.publisher_repository_interface import (
    IPublisherRepository,
)


class GetAllPublishersV2UseCase:
    """Get all publishers use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(self) -> list[Publisher]:
        """
        Execute the use case.

        Returns:
            Liste des éditeurs.
        """
        response = self.repository.get_all_v2()
        return response.publishers


class GetPublisherByIdV2UseCase:
    """Get publisher by id use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(
        self, publisher_id: str
    ) -> (tuple)[Publisher, list[Edition], list[BoxEdition], list[Serie], list[TypeSerie], list[Volume], list[Box]]:
        """
        Execute the use case.

        Args:
            publisher_id: The id of the publisher.

        Returns:
            Tuple contenant:
                - Publisher: L'éditeur
                - list[Edition]: Liste des éditions
                - list[BoxEdition]: Liste des éditions de coffrets
                - list[Serie]: Liste des séries
                - list[TypeSerie]: Liste des types de séries
                - list[Volume]: Liste des volumes
                - list[Box]: Liste des coffrets

        Raises:
            PublisherNotFoundException: Si l'éditeur n'existe pas
        """
        response = self.repository.get_by_id_v2(publisher_id)
        return (
            response.publishers[0],
            response.editions,
            response.box_editions,
            response.series,
            response.types,
            response.volumes,
            response.boxes,
        )


class GetListPublishersUseCase:
    """Get list publishers use case."""

    def __init__(self, repository: IPublisherRepository):
        """
        Initialize the use case.

        Args:
            repository: The publisher repository.
        """
        self.repository = repository

    def __call__(self) -> list[PublisherListItem]:
        """
        Execute the use case.

        Returns:
            A list of PublisherListItem.
        """
        return self.repository.get_list()
