"""DTOs de réponse pour les opérations Serie.

Ce module contient les Data Transfer Objects utilisés pour structurer
les réponses des endpoints de l'API Serie.
"""

from dataclasses import dataclass

from mangacollec.domain.entities import (Author, Box, BoxEdition, BoxVolume,
                                         Edition, Job, Kind, Publisher, Serie,
                                         Task, TypeSerie, Volume)


@dataclass(frozen=True)
class GetAllSeriesV2Response:
    """Réponse de l'endpoint GET /v2/series/.

    Contient la liste de toutes les séries avec leurs types associés.

    Attributes:
        series: Liste de toutes les séries
        types: Liste de tous les types de séries
    """

    series: list[Serie]
    types: list[TypeSerie]


@dataclass(frozen=True)
class GetSerieByIdV2Response:
    """Réponse de l'endpoint GET /v2/series/{serie_id}.

    Contient la série demandée avec toutes ses relations (types, genres, tâches,
    métiers, auteurs, éditions, éditeurs, volumes, coffrets, etc.).

    Attributes:
        series: Liste contenant la série (normalement 1 élément)
        types: Liste des types de séries associés
        kinds: Liste des genres associés à la série
        tasks: Liste des tâches (relations auteur-rôle-série)
        jobs: Liste des rôles/métiers des auteurs
        authors: Liste des auteurs impliqués dans la série
        editions: Liste des éditions de la série
        publishers: Liste des éditeurs
        volumes: Liste des volumes disponibles
        box_editions: Liste des box éditions
        boxes: Liste des coffrets
        box_volumes: Liste des volumes dans les coffrets
    """

    series: list[Serie]
    types: list[TypeSerie]
    kinds: list[Kind]
    tasks: list[Task]
    jobs: list[Job]
    authors: list[Author]
    editions: list[Edition]
    publishers: list[Publisher]
    volumes: list[Volume]
    box_editions: list[BoxEdition]
    boxes: list[Box]
    box_volumes: list[BoxVolume]
