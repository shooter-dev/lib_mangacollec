"""Use cases pour la ressource Serie.

This module contains all use cases for Serie operations.
"""

from mangacollec.application.mappers import SerieMapper
from mangacollec.domain.entities import (Author, Box, BoxEdition, BoxVolume,
                                         Edition, Job, Kind, Publisher, Serie,
                                         SerieListItem, Task, TypeSerie,
                                         Volume)
from mangacollec.domain.repositories import ISerieRepository


class GetAllSeriesV2UseCase:
    """Cas d'utilisation : récupérer toutes les séries avec leurs types."""

    def __init__(self, repository: ISerieRepository) -> None:
        self.repository = repository

    def __call__(self) -> tuple[list[Serie], list[TypeSerie]]:
        """Exécute le use case.

        Returns:
            Tuple contenant:
                - list[Serie]: Liste des séries
                - list[TypeSerie]: Liste des types
        """
        response = self.repository.get_all_series_v2()
        return (response.series, response.types)


class GetSerieByIdV2UseCase:
    """Cas d'utilisation : récupérer une série par ID avec toutes ses relations."""

    def __init__(self, repository: ISerieRepository) -> None:
        self.repository = repository

    def __call__(self, serie_id: str) -> tuple[
        Serie,
        list[TypeSerie],
        list[Kind],
        list[Task],
        list[Job],
        list[Author],
        list[Edition],
        list[Publisher],
        list[Volume],
        list[BoxEdition],
        list[Box],
        list[BoxVolume],
    ]:
        """Exécute le use case.

        Args:
            serie_id: UUID de la série

        Returns:
            Tuple contenant:
                - Serie: La série
                - list[TypeSerie]: Liste des types
                - list[Kind]: Liste des genres
                - list[Task]: Liste des tâches
                - list[Job]: Liste des rôles/métiers
                - list[Author]: Liste des auteurs
                - list[Edition]: Liste des éditions
                - list[Publisher]: Liste des éditeurs
                - list[Volume]: Liste des volumes
                - list[BoxEdition]: Liste des box éditions
                - list[Box]: Liste des coffrets
                - list[BoxVolume]: Liste des volumes dans coffrets

        Raises:
            SerieNotFoundException: Si la série n'existe pas
        """
        response = self.repository.get_serie_by_id_v2(serie_id)
        return (
            response.series[0],
            response.types,
            response.kinds,
            response.tasks,
            response.jobs,
            response.authors,
            response.editions,
            response.publishers,
            response.volumes,
            response.box_editions,
            response.boxes,
            response.box_volumes,
        )


class GetListSeriesUseCase:
    """Cas d'utilisation : récupérer la liste simplifiée des séries."""

    def __init__(self, repository: ISerieRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[SerieListItem]:
        """Exécute le use case.

        Returns:
            Liste des entités SerieListItem (id + title)
        """
        response = self.repository.get_all_series_v2()
        return [SerieMapper.to_list_item(serie) for serie in response.series]
