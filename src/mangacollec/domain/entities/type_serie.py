"""TypeSerie entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TypeSerie:
    """Entité TypeSerie du domaine.

    Représente un type de série (Manga, Manhwa, Manhua, BD, Comics, etc.).

    Attributes:
        id: Identifiant unique du type de série
        title: Titre du type de série
        to_display: Indicateur de visibilité pour l'affichage
    """

    id: str
    title: str
    to_display: bool
